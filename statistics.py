# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy
print("Give the type of distribution B for binomial and H for hypergeometric N for normal ")
ans=input()
array=list()
numpy.random.seed(1)
num=int();
size=[]
if ans=="N":
    print("Give the mean of the distribution")
    loc=float(input())
    print("Give standard deviation")
    scale=float(input())
    print("Give shape, two numbers")
    size.append(int(input()))
    size.append(int(input()))
    array=numpy.random.normal(loc,scale,size)
    print (array)
    num=loc+(3*scale)
elif ans=="B":
    
    print("Give number of trials")
    n=int(input())
    num=n
    print("Give probabilty")
    p=float(input())
    print("Give shape")
    size.append(int(input()))
    size.append(int(input()))
    array=numpy.random.binomial(n,p,size)
    print (array)
elif ans=="H":
    print("Give the number of good selection")
    good=int(input())
    print("Give the number of bad selection")
    bad=int(input())
    print("Give number of samples")
    sample=int(input())
    if sample>good:
        num=good
    else:
        num=sample
    print("Give shape, two numbers")
    size.append(int(input()))
    size.append(int(input()))
    array=numpy.random.hypergeometric(good,bad,sample,size)
    print (array)

    
import matplotlib.pyplot as plt
#print("Something")
plt.plot(array,'ro')
plt.ylabel('Some numbers')
plt.axis([0,num,0,num])
plt.show()
