import time
f= open('voorbeeld_ecg.txt','r')
lines=f.readlines()
f.close()
i=0
pijp=open('ekgpipe','w')

while True:
    pijp.write(lines[i])
    pijp.flush()
    i+=1
    time.sleep(0.01)
