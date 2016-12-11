import matplotlib, os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
datafile = open('ekgpipe','r')

fig, ax = plt.subplots()

xlist = []
ylist = []

line, = ax.plot(xlist, ylist)

def animate(i):
	line.set_ydata(update())
	xlist.append(i)
	return line,

def update():
	data = (datafile.readline()).rstrip('\n')
	return data

def init():
	line.set_ydata(np.ma.array(xlist, mask=True))
	return line

ani = animation.FuncAnimation(fig, animate, init_func=init, interval = 100)

plt.show()

"""
#plotting
fig = plt.figure()
ax = plt.axes(xlim=(0,600), ylim=(0,256))
anim = animation.FuncAnimation(fig, update, fargs=None, interval=100)
plt.show()
"""

"""
while True:
	xlst.append(i)
	i+=1

	datalst.append((datafile.readline()).rstrip('\n'))
	
	plt.plot(xlst,datalst)
	plt.pause(0.005)
"""
