function N = laagfilter(tijd,graf,lengte,H)
A = zeros([1 lengte]);
N = zeros([1 lengte]);
for t = 1:tijd
    A(t) = maxster(graf,t,2,2)-minster(graf,t,2,2);
    if A(t) <= abs(H(t))
            N(t) = sign(H(t)*(abs(H(t))-A(t)));
    else
            N(t) = 0;
    end
end