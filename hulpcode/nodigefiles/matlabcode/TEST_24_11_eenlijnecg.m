function result = eenlijnecg(ECG_new,tijd,sample_rate,lengte,xste_keer_doorlopen,vier_laatste_pieken,tijdstip_laatste_piek)

nr_hartslag = xste_keer_doorlopen;
nieuwe_pieken = vier_laatste_pieken;
tijdstip_buitenbrengen = tijdstip_laatste_piek; % Wordt na doorlopen buitengebracht. Indien niet gewijzigd, dan blijft tijdstip behouden.

H = hoogfilter(tijd,ECG_new,lengte);

N = laagfilter(tijd,ECG_new,lengte,H);
    
G = g_pieken(tijd,lengte,N);

if length(nieuwe_pieken) == 4;
    vier_gevuld = true;
else
    vier_gevuld = false;
end

for t = 1:tijd
    g  = G(t);
    if g > 0
        
        tijdstip_nieuwe_piek = t + lengte * xste_keer_doorlopen;
        
        if  ( tijdstip_nieuwe_piek - tijdstip_buitenbrengen ) > 0.27*sample_rate  
            
            tijdstip_buitenbrengen = tijdstip_nieuwe_piek;
            
            if vier_gevuld == false
                nieuwe_pieken(end+1) = tijdstip_buitenbrengen;
            
            else
                nieuwe_pieken(1) = vier_laatste_pieken(2);
                nieuwe_pieken(2) = vier_laatste_pieken(3);
                nieuwe_pieken(3) = vier_laatste_pieken(4);
                nieuwe_pieken(4) = tijdstip_buitenbrengen;

            end
            
        %else
            
        end
    end
end

if vier_gevuld == true
    nb_beats = length(vier_laatste_pieken) - 1; %Eerste piekwaarde is beginwaarde voor interval
    sample_interval = vier_laatste_pieken(4) - vier_laatste_pieken(1);
    gemiddelde_hartslag = round( nb_beats/((sample_interval/sample_rate)/60) );
else
    gemiddelde_hartslag = -1;
end
    
result = [nr_hartslag gemiddelde_hartslag tijdstip_buitenbrengen nieuwe_pieken];


end