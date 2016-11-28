function minstert = minster(graf,tijd,sigma,delta)
prev_min = 0;
for t = 1:tijd
    x = graf(t);
    if tijd == 0
       prev_min = x;
    elseif x < prev_min
        prev_min = prev_min - sigma * delta;
    else
        prev_min = prev_min + delta;
    end
end
minstert = prev_min;
end