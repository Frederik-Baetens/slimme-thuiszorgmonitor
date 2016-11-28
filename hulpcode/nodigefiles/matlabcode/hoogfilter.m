function H = hoogfilter(tijd,graf,lengte)
H = zeros([1 lengte]);
for t = 1:tijd
    H(t) = graf(t)-(maxster(graf,t,2,2)-minster(graf,t,2,2))/2;
end
end
