import matplotlib, os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
datafile = open('ekgpipe','r')

def update():
	data = (datafile.readline()).rstrip('\n')
	return data

#plotting
fig = plt.figure()
ax = plt.axes(xlim=(0,600), ylim=(0,256))
anim = animation.FuncAnimation(fig, update, interval=100)
plt.show()


"""
while True:
	xlst.append(i)
	i+=1

	datalst.append((datafile.readline()).rstrip('\n'))
	
	plt.plot(xlst,datalst)
	plt.pause(0.005)
"""
