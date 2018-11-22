#!/usr/bin/python
from math import exp
import numpy as np
import sys

def binomial_tree(type,F, K, r, sigma, D, N=2):   
    deltaT = float(D/365) / N
    u = np.exp(sigma * np.sqrt(deltaT))
    d = 1.0 / u
    
    tmp_arr =  np.asarray([0.0 for i in range(N + 1)])   
    tmp_F_arr = np.asarray([(F * u**i * d**(N - i)) for i in range(N + 1)])
    tmp_K_arr = np.asarray( [float(K) for i in range(N + 1)])

    p = (1 - d)/ (u - d)
    q = 1.0 - p
    discount = np.exp(-r * deltaT)

    if type =="C":
        tmp_arr[:] = np.maximum(tmp_F_arr-tmp_K_arr, 0.0)
    else:
        tmp_arr[:] = np.maximum(-tmp_F_arr+tmp_K_arr, 0.0)
    
    #for i in range(N-1, -1, -1):
    #   tmp_arr[:-1]= discount * (p * tmp_arr[1:] + q * tmp_arr[:-1])
    #   tmp_F_arr[:]=tmp_F_arr[:]*u
    #   if type =="C":
    #        tmp_arr[:]=np.maximum(tmp_arr[:],tmp_F_arr[:]-tmp_K_arr[:])
    #   else:
    #        tmp_arr[:]=np.maximum(tmp_arr[:],-tmp_F_arr[:]+tmp_K_arr[:])
            
    for i in range(1, N+1, 1):
       b=(N+2-i)
       tmp_arr[:-i]= discount * (p * tmp_arr[1:b] + q * tmp_arr[:-i])
       tmp_F_arr[:b]=tmp_F_arr[:b]*u
       if type =="C":
            tmp_arr[:b]=np.maximum(tmp_arr[:b],tmp_F_arr[:b]-tmp_K_arr[:b])
       else:
            tmp_arr[:b]=np.maximum(tmp_arr[:b],-tmp_F_arr[:b]+tmp_K_arr[:b])
    
    return round(tmp_arr[0],4)

def handle_line(line):
    paraList = line.split(",")
    if len(paraList) == 7 :
        N = int(paraList[0])
        O = paraList[1]
        K = float(paraList[2])
        D = int(paraList[3])
        F = float(paraList[4])
        sigma = float(paraList[5])
        r = float(paraList[6])
        print("%.4f" % binomial_tree(O,F,K,r,sigma,D,N))
    
if __name__ == '__main__':
    paraStr = sys.argv[1]
    handle_line(paraStr)
    
    #handle_line("10000,C,98.700,60,98.695,0.2,0.035")
    #handle_line("2,C,98.700,60,98.695,0.2,0.035")
    #handle_line("1,C,98.700,60,98.695,0.2,0.035")
    #handle_line("128,C,98.700,60,98.695,0.2,0.035")
    #handle_line("4096,C,98.700,60,9.695,0.2,0.035")
    #handle_line("4096,C,98.700,60,9.695,0.1,0.035")
    #handle_line("4096,C,98.700,1000,9.695,0.1,0.035")
    #handle_line("4096,C,8.700,1000,9.695,0.1,0.035")
    #handle_line("4096,C,8.700,1000,8.700,0.1,0.035")
    #handle_line("4096,C,8.700,1000,8.700,0.1,0.005")
    #handle_line("4096,C,8.700,1000,8.700,0.9,0.005")
    #handle_line("10000,P,98.700,60,98.695,0.2,0.035")
    #handle_line("2,P,98.700,60,98.695,0.2,0.035")
    #handle_line("1,P,98.700,60,98.695,0.2,0.035")
    #handle_line("128,P,98.700,60,98.695,0.2,0.035")
    #handle_line("4096,P,98.700,60,9.695,0.2,0.035")
    #handle_line("4096,P,98.700,60,9.695,0.1,0.035")
    #handle_line("4096,P,98.700,1000,9.695,0.1,0.035")
    #handle_line("4096,P,8.700,1000,9.695,0.1,0.035")
    #handle_line("4096,P,8.700,1000,8.700,0.1,0.035")
    #handle_line("4096,P,8.700,1000,8.700,0.1,0.005")
    #handle_line("4096,P,8.700,1000,8.700,0.9,0.005")
    #handle_line("10000,P,98.700,60,98.695,0.9,0.035")
    #handle_line("50000,C,98.700,60,98.695,0.2,0.035")
    #handle_line("50000,C,98.700,60000,98.695,0.2,0.035")
    #handle_line("100000,C,98.700,10000,438.695,0.2,0.035")
    #handle_line("50000,C,98.700,10000,438.695,0.2,0.1")
    #handle_line("50000,C,98.700,10000,438.695,0.2,1000")
    