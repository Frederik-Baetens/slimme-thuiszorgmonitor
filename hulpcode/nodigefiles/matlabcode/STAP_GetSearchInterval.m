function [STAP_SearchInterval, StartSample] = STAP_GetSearchInterval(InputList,ThresholdValue)
% function which returns the first array of values which are smaller than
% the threshold value, working from the end of the inputlist to the
% beginning

% if the inputlist is too long to be filtered in a reasonable amount of
% time, the last part of the list is cut off and filtered

% constants
HighestFreq = 3;
FilterOrder = 3;
SampleRate = 32;
StartSampleNb = 0;

if length(InputList) > 400
    AnalysingList = InputList(end-300:end);
    StartSampleNb = length(InputList)-301;
else
    AnalysingList = InputList;
end

AnalysingSignal = AnalysingList;
% 
% [b,a] = butter(FilterOrder, HighestFreq/(SampleRate/2), 'high');
% Delay = round(median(grpdelay(b,a)));
% 
% AnalysingSignal = filter(b,a,AnalysingList);
% plot(AnalysingList); hold on
% plot(AnalysingSignal);
% 
ConversedInterval = [];
STAP_SearchInterval = [];

ItemNumber = 0;
while length(AnalysingSignal) > ItemNumber && AnalysingSignal(end - ItemNumber) < ThresholdValue;
    ItemNumber = ItemNumber + 1;
end
FilteredValAtStart = ItemNumber - 1;

while length(AnalysingSignal) > ItemNumber && AnalysingSignal(end - ItemNumber) >= ThresholdValue;
    ConversedInterval(end+1) = AnalysingSignal(end-ItemNumber);
    ItemNumber = ItemNumber + 1;
end

LengthIntervalToInverse = length(ConversedInterval);
while LengthIntervalToInverse > 0;
    STAP_SearchInterval(end + 1) = ConversedInterval(LengthIntervalToInverse);
    LengthIntervalToInverse = LengthIntervalToInverse - 1;
end

% StartSample = length(AnalysingSignal) - FilteredValAtStart - length(STAP_SearchInterval) - Delay + StartSampleNb;
StartSample = length(AnalysingSignal) - FilteredValAtStart - length(STAP_SearchInterval) + StartSampleNb;
end