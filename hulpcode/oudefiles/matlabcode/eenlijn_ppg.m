function [inputlist] = eenlijn_ppg(inputlist,new_data)
%UNTITLED5 Summary of this function goes here
%   Detailed explanation goes here

if isempty(new_data)
    return
end

for new_element = new_data(1:length(new_data))
    
    plaats = length(inputlist_red) + length(inputlist_infrared);
    if mod(plaats,2) == 0
        inputlist_red(end+1) = new_element;
    else
        inputlist_infrared(end+1) = new_element;
    end
end