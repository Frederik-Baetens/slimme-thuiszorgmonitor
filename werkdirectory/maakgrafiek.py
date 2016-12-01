import matplotlib.pyplot as plt
f= open('ectgrafiek.txt','r')
lines=f.readlines()
f.close()

plt.plot(lines)
plt.show()

