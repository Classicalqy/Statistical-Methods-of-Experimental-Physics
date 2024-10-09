##############################################################
#week 10 homework  Statistical Methods in Experimental Physics#
##############################################################
#author Qiyu Chen
#date 2024.4.21
import random
import math
import numpy
import matplotlib.pyplot as plt

'''A plot function to plot hist'''
def plot(list, title, filename):
    plt.hist(list, bins=100, density=True)
    plt.title(title)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig('Desktop/{0}.jpg'.format(filename))
    plt.cla()

#exer6.7 part 1 started
tau=[]
for i in range(1000):
    t=[numpy.random.exponential(1) for _ in range(10)]
    tau.append(sum(t)/len(t))
plot(tau, 'distribution of hat{tau}', 'part1')
print(sum(tau)/len(tau))

#part2 started
lamb=[]
for i in range(1000):
    t=[numpy.random.exponential(1) for _ in range(10)]
    tau.append(len(t)/sum(t))
plot(tau, 'distribution of hat{lambda}', 'part2')
print(sum(tau)/len(tau))