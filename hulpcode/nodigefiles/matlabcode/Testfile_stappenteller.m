Colgate = csvread('stappenteller_data.csv');
plot(Colgate)
Colgate = Colgate(1:67440);
plot(Colgate)
[STAP_SearchInterval, StartSample] = STAP_GetSearchInterval(Colgate,2500);
[tba, samp] = stappenteller(STAP_SearchInterval,StartSample,0);
