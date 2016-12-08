import matplotlib.pyplot as plt
import numpy as np
plt.ion() ## Note this correction
fig=plt.figure()
plt.axis([i-1000,i,0,1])
ekgfile = open('ekgpipe','r')
pofile = open('popipe','r')

i=0
x=list()
y=list()

while True:
	i+=1
    x.append(i);
    y.append();
    plt.scatter(i,);
    i+=1;
    plt.show()


