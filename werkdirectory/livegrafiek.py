import matplotlib, os, collections
matplotlib.use('qt4agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
datafile = open('ekgpipe','r')

NB=1000
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
                ylst.append(eval((datafile.readline()).rstrip('\n')))
                ylst.append(eval((datafile.readline()).rstrip('\n')))
                yield ylst


ani = animation.FuncAnimation(fig,update,data_gen,interval=0, blit=True)
plt.show()

