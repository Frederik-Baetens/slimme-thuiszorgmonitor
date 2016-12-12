import time
i=0
pijp=open('ekgpipe','w')
while True:
	dat=100-i
	pijp.write(str(dat)+'\n')
	pijp.flush()
	i+=1
	time.sleep(1/120)
