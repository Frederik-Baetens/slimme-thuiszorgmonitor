import matplotlib
import matplotlib.pyplot as plt
datafile = input('datafile: ')
f= open(datafile,'r')
lines1=f.readlines()
f.close()
lines2=[eval(i)//16 for i in lines1]

plt.plot(lines1)
plt.show()
