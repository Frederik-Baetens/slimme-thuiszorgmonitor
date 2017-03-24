function [POM_SearchInterval, StartSample] = POM_GetSearchInterval(InputList)
% function which returns the first array of values which are greater than
% the threshold value, working from the end of the inputlist to the
% beginning

ConversedInterval = [];
ThresholdValue = 0; % determined by signal from sensor
POM_SearchInterval = [];

ItemNumber = 0;
while length(InputList) > ItemNumber && InputList(end - ItemNumber) < ThresholdValue;
    ItemNumber = ItemNumber + 1;
end
FilteredValAtStart = ItemNumber - 1;

while length(InputList) > ItemNumber && InputList(end - ItemNumber) >= ThresholdValue;
    ConversedInterval(end+1) = InputList(end-ItemNumber);
    ItemNumber = ItemNumber + 1;
end

LengthIntervalToInverse = length(ConversedInterval);
while LengthIntervalToInverse > 0;
    POM_SearchInterval(end + 1) = ConversedInterval(LengthIntervalToInverse);
    LengthIntervalToInverse = LengthIntervalToInverse - 1;
end 

StartSample = length(InputList) - FilteredValAtStart - length(POM_SearchInterval);
end
    
