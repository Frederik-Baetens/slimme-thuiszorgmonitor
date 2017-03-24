import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

datafile = input('datafile: ')
f= open(datafile,'r')
lines1=f.readlines()
f.close()
lines2=[eval(i) for i in lines1]

plt.plot(lines2)
plt.ylabel('waarde')
plt.xlabel('samples')
plt.show()
