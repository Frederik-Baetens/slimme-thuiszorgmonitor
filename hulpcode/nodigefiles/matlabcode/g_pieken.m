function G = g_pieken(tijd,lengte,N)
beta = 15;
G = zeros([1 lengte]);
for t = 1:tijd
    n = N(t);

        %nbm = n_beta_min = n(t-beta)
        if n > beta
            nbm = N(t-beta);
        else 
            nbm = 0;
        end
        %nbp = n_beta_plus = n(t+beta)
        if t+beta <= tijd
            nbp = N(t+beta);
        else
            nbp = 0;
        end

        if (n > 0) && (nbm < n) && (nbp < n)
            G(t) = N(t) - max(nbp,nbm);
        elseif (n < 0) && (nbm > n) && (nbp > n)
            G(t) = N(t) + min(nbp,nbm);
        else
            G(t) = 0;
        end
end