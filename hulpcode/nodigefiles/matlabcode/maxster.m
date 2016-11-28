function maxstert = maxster(graf,tijd,sigma,delta)
prev_max = 0;
for t = 1:tijd
    x = graf(t);
    if tijd == 0
       prev_max = x;
    elseif x > prev_max
        prev_max = prev_max + sigma * delta;
    else
        prev_max = prev_max - delta;
    end
end
maxstert = prev_max;
end
        