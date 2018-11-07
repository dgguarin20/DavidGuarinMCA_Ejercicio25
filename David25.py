import numpy as np
import matplotlib.pyplot as plt

myarray = np.fromfile('sample.dat', dtype=float)

l = []
miu = myarray[0]
std = myarray[1]

for i in range(0,len(myarray)-2):
    l.append(myarray[i+2])

l = np.asarray(l)
fig=plt.figure()
a,b,c =plt.hist(l, normed=1)
plt.show()
fig.savefig('grafia.pdf')
