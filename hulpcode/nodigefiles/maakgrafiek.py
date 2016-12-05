import matplotlib
import matplotlib.pyplot as plt
f= open('datafile.txt','r')
lines=f.readlines()
f.close()
lines2=[eval(i)//16 for i in lines]

plt.plot(lines)
plt.show()
