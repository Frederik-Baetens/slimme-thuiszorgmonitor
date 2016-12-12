import matplotlib
import matplotlib.pyplot as plt
f= open('voetdata.txt','r')
lines1=f.readlines()
f.close()
lines2=[eval(i)//16 for i in lines1]

plt.plot(lines1)
plt.show()
