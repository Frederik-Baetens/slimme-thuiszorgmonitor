tijd = 32;
sample_rate = 128;
lengte = tijd;
pauze = 0;
xste_keer_doorlopen = 0;
vier_laatste_pieken = [];
tijdstip_laatste_piek = -10;

g = fopen('popipe','r')

while xste_keer_doorlopen ~= 20312
    
    disp(xste_keer_doorlopen)
    
    ECG_new = fscanf(g,'%f',[1,32])
    
    result = TEST_24_11_eenlijnecg(ECG_new,tijd,sample_rate,lengte,xste_keer_doorlopen,vier_laatste_pieken,tijdstip_laatste_piek);
    
    nr_hartslag = result(1);
    hartslag = result(2);
    
    if hartslag == -1
        tijdstip_laatste_piek = result(3);

        vier_laatste_pieken = result(4:end);
        
        xste_keer_doorlopen = xste_keer_doorlopen + 1;
        continue
    end
    
    tijdstip_laatste_piek = result(3);

    vier_laatste_pieken = result(4:end);
    
    disp([nr_hartslag hartslag])
    
    xste_keer_doorlopen = xste_keer_doorlopen + 1;
    
    pause(pauze);
          
end



