import time
f= open('voorbeeld_ecg.txt','r')
lines=f.readlines()
f.close()
i=0

while True:
    print (lines[i],flush=True)
    i+=1
    time.sleep(0.01)
