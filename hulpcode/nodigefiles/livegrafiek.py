import matplotlib, os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
datafile = open('ekgpipe','r')

datalst=[]
xlst=[]
i=0

#plotten
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	dataArray = 
"""
while True:
	xlst.append(i)
	i+=1

	datalst.append((datafile.readline()).rstrip('\n'))
	
	plt.plot(xlst,datalst)
	plt.pause(0.005)
"""
