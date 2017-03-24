function[ToBeAdded,SampleNumber] = stappenteller(STAP_SearchInterval,StartSample,PrevSampleNumber)
% function which returns the samplenumber of the minimum value in the
% signal and if the value has to be added



[~,SampleNumber] = min(STAP_SearchInterval);
SampleNumber = SampleNumber + StartSample;

PossibleStepPerSecond = 3; %determined by experiments
SampleRate = 32;
ToBeAdded = true;

if SampleNumber - PrevSampleNumber < SampleRate*2/PossibleStepPerSecond
    ToBeAdded = false;
end

% counter = 1;
% while counter <= length(STAP_SearchInterval)
%     if STAP_SearchInterval(counter) > ThresholdValue
%         return
%     end
%     if counter == length(STAP_SearchInterval)
%         STAP_SearchInterval = [];
%         return
%     end
%     counter = counter + 1;
% end
end


    