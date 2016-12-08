function [ToBeAdded, SampNbNewPeak, SampNbExtraPeak, NewHR, CorrNewHR] = ...
    POM_GetIntervalAnalysis2(InputSignal, SampNbPrevPeak,...
    PreviousHR)

% Function that analyses intervals composed by the POM_GetSearchInterval
% function.
% Its arguments are the values of the interval in which a new peak could 
% be found, the sample number of the first item of this interval, the
% sample number of the previous detected peak, a list of previous
% calculated heart rhythms (of which the length can be chosen by the user).
% It returns whether if the interval contains a peak, the samplenumber of 
% this peak, the newly calculated heart rhythm, the corrigated new heart 
% rhythm and the point on which an extra peak should be inserted if the
% need of this extra peak is detected.


%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% FUNCTION SETUP %%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%

% constants
MinPulse = 2.5;
SampleRate = 64;
PrevToCompare = 5;
MaxDeltaHR = 20;
ButterFilterOrder = 5;
LowestPPGFreq = 0.5;
HighestPPGFreq = 5;
MinHeartRate = 30;
MaxHeartRate = 200;
CutOffSampleNb = 0;

% constants which are possibly adjusted during execution
MinSampDifference = SampleRate * 60 / MaxHeartRate;
MaxSampDifference = SampleRate * 60 / MinHeartRate;
ToBeAdded = true;
SampNbNewPeak = 0;
NewHR = 0;
CorrNewHR = 0;
SampNbExtraPeak = 0;
SampNbExtraPeakInFiltered = 0;

% Only the last part of the signal is used for this analysis. Before the
% exact interval of search is determined, the input signal is filtered. It
% would be a waste of time to filter the entire signal, so before the
% filter is applied, the samples before the last 300 samples are cut off of
% the signal.
if length(InputSignal) > 400;
    CutOffSampleNb = length(InputSignal)-300;
    InputSignal = InputSignal(end-300: end);
    SampNbPrevPeak = SampNbPrevPeak - CutOffSampleNb;
end

                                                                                    %disp(InputSignal)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% APPLY BUTTERWORTH FILTER %%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% apply Butterworth filter (bandpass 0.5 to 5 Hz) on the input signal if
% the length of this signal allows filtering
[b,a] = butter(ButterFilterOrder, [LowestPPGFreq]/(SampleRate/2),'high');
[d,c] = butter(ButterFilterOrder, [HighestPPGFreq]/(SampleRate/2),'low');

HighFiltSignal = filter(b,a,InputSignal);
HighLowFiltSignal = filter(d,c,HighFiltSignal);

% these filters add a delay to the signal. This delay is needed to locate
% the peaks in the original signal. As the delay depends on the frequency,
% this delay is an approximated value
delayhigh = grpdelay(b,a);
delaylow = grpdelay(d,c);
Delay = median(delayhigh) + median(delaylow);

                                                                                    %disp(Delay)

SampNbPrevPeakInFiltered = SampNbPrevPeak + Delay;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% CONTINUATION FUNCTION SETUP %%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% search for the interval from the filtered signal in which the latest 
% maximum should be found
                                                                                    %disp(HighLowFiltSignal)

[InputInterval, NbFirstSampleInFiltered] = POM_GetSearchInterval(HighLowFiltSignal);
% due to the filter delay, the last part of this search interval is
% disturbed and 

                                                                                    %disp(InputInterval)
                                                                                    %disp(NbFirstSampleInFiltered)

% evaluation whether filters which depend on previous values (given in the
% input) can be used (they will not be sufficiently extended for the first 
% few analysed intervals)
ComparisonFilters = true;
if length(PreviousHR) < PrevToCompare
    ComparisonFilters = false;
end

                                                                                    %disp(ComparisonFilters)

% evaluation of control variables based on previous values or inputs
if ComparisonFilters == true;
    MinSampDifference = SampleRate*60*0.4/median(PreviousHR);
    MaxSampDifference = SampleRate*60*1.8/median(PreviousHR);
end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% LOCALISATION AND EVALUATION OF MAXIMUM %%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Localisation maximum of the fiven interval
[MaxOnInterval, MaxPositionInFiltered] = max(InputInterval);
SampNbNewPeakInFiltered = MaxPositionInFiltered + NbFirstSampleInFiltered;

% Filter: maximum value exceeds minimum value for a peak
if MaxOnInterval < MinPulse
    ToBeAdded = false;
    return
end

                                                                                    %disp('ok')

% Filter: the time between the previous peak and the current maximum should
% be longer than a minimum which is set based on the previous heart rhythms
% If not, the peak would cause an unrealistic increase in the heart rhythm.
if SampNbNewPeakInFiltered - SampNbPrevPeakInFiltered < MinSampDifference...
        && not(isempty(PreviousHR))
    ToBeAdded = false;
    return
end

                                                                                    %disp('ok')

% Filter: the time between the previous peak and the current maximum should 
% be shorter than a maximum set based on the previous heart rhythms. If
% not, there is a drop in the heart rhythm which is probably caused by
% an undetected peak in the region between the previous and the current
% maximum. To solve this issue, an extra peak is set on the sample which is
% to be found in the middle between the current and the previous peak.
if SampNbNewPeakInFiltered - SampNbPrevPeakInFiltered > MaxSampDifference
    SampNbExtraPeakInFiltered = (SampNbNewPeakInFiltered + SampNbPrevPeakInFiltered)/2;
end

                                                                                    %disp('ok')


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% CALCULATION AND EVALUATION HEART RHYTHM %%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Calculation of the Heart Rhythm
% in case of the addition of an extra peak, the heart rhythm will have the
% same value twice as the extra peak is placed in the middle between the
% previous and the detected (current) peak.
if SampNbExtraPeakInFiltered == 0;
    NewHR = SampleRate*60/(SampNbNewPeakInFiltered-SampNbPrevPeakInFiltered);
else
    NewHR = SampleRate*60/(SampNbNewPeakInFiltered-SampNbExtraPeakInFiltered);
end

% Filter: the heart rhythm cannot vary too quickly. The criteria which
% determine whether if the detected maximum is a peak, filter the 
if ComparisonFilters == true;
    if NewHR - median(PreviousHR) > MaxDeltaHR;
        CorrNewHR = median(PreviousHR);
    else
        CorrNewHR = NewHR;
    end
else
    CorrNewHR = NewHR;
end    


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%% TAKING THE FILTER DELAY IN ACCOUNT %%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% The peaks are currently located on the peaks of the filtered signal.
% To be able to mark these peaks on the signal in the visualising tool, the
% sample number of the peak has to get addapted to the delay which occures
% as a  result of filtering.
SampNbNewPeak = CutOffSampleNb + SampNbNewPeakInFiltered - Delay;
if not(SampNbExtraPeakInFiltered == 0);
    SampNbExtraPeak = CutOffSampleNb + SampNbExtraPeakInFiltered - Delay;
end

end