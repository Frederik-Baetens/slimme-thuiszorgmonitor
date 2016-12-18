import matplotlib, os, collections
matplotlib.use('qt4agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
datafile = open('ekgpipe','r')

NB=600
MAX=256

ylst = collections.deque([0]*NB,NB)

fig, ax = plt.subplots()
line, = ax.plot([0,]*NB)
ax.set_ylim(0,MAX)



def update(data):
        line.set_ydata(data)
        return line,

def data_gen():
        while True:
                ylst.append(eval((datafile.readline()).rstrip('\n')))
                ylst.append(eval((datafile.readline()).rstrip('\n')))
                yield ylst


ani = animation.FuncAnimation(fig,update,data_gen,interval=0, blit=True)
plt.show()

"""
def animate(i):
        line.set_ydata(update(i)[0])
        line.set_xdata(update(i)[1])
        ylist.append(update(i)[0])
        xlist.append(update(i)[1])
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
