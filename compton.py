#!/bin/python
import math
import numpy as np
import matplotlib.pyplot as plt

w=float(input())
theta= -math.pi
h=6.62607015*(1/(10**(34)))
m=9.109*(1/(10**(31)))
c=2.997*(10**8)

def solve():
    w1=w+((h/(m*c))*(1-math.cos(theta)))
    return(w1)


if __name__ == "__main__":
    l=[]
    lp=[]
    th=[]
    
    while theta<(math.pi):
        l.append(float(solve()))
        th.append(theta)
        lp.append(w)
        theta=theta+0.01
        
        
    data=np.array(l)
    data1=np.array(lp)
    angle=np.array(th)
    
    diff=[]

    for i in range(0,len(data)):
        diff.append(data[i]-data1[i])
        
    df=np.array(diff)
    
    plt.title("Line graph")
    plt.xlabel("X axis - delta theta ")
    plt.ylabel("Y axis - delta lambda")
   # plt.plot(angle,data, color ="red")
   # plt.plot(angle,data1, color="blue")
    plt.plot(angle,df, color="black")
    plt.show()