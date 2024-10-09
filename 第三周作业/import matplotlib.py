import matplotlib.pylab as plt
import numpy
import random
tot=10000
nu=3.0
N=12
'''consider first six dynodes'''
n_out=[]
for _ in range(tot):
    n_0=1
    for i in range(6):
        n=0
        if i==0:
            for _ in range(0,n_0):
                n+=numpy.random.poisson(6.0)
        else:
            for _ in range(0, n_0):
                n+=numpy.random.poisson(nu)
        n_0=n
    n_out.append(n_0)
'''
Now we have a distribution, and we want to generate random numbers to fit this distribution 
So, we use ARM
'''  
'''first we want to fit a distribution of 6 dynodes'''
n_out_1=[]
for _ in range(tot):
    n_0=1
    for _ in range(6):
        n=0
        for _ in range(0, n_0):
            n+=numpy.random.poisson(nu)
        n_0=n
    n_out_1.append(n_0)

'''histogram is the ditribution function that we search for'''

'''Monte Carlo simulation'''
def random_generate(s):
    l=len(s)
    p=random.randint(0,l-1)
    return s[p]
n_out_final=[]
for i in range(tot):
    n_transient=0
    for j in range(0,n_out[i]):
        n_transient+=random_generate(n_out_1)
    n_out_final.append(n_transient)

'''Plot it'''
plt.hist(n_out_final, bins=50, density=True)
plt.show()
plt.cla()
print(sum(n_out_final)/len(n_out_final))
#######