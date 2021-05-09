# -*- coding: utf-8 -*-
"""Entanglement.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W_GlyDRIfeJpjpjuXBvykki2KKvC547i
"""

from scipy import integrate
import scipy as scipy
import numpy as np
import matplotlib.pylab as plt
import math

def limt2(t2):
    return [0, t2]
def complexintegral1(func, lim, **kwargs):
    def real_func(x,y,z,t):
        return np.real(func(x,y,z,t))
    def imag_func(x,y,z,t):
        return np.imag(func(x,y,z,t))
    real_integral = integrate.nquad(real_func, lim, **kwargs)
    imag_integral = integrate.nquad(imag_func, lim, **kwargs)
    return (real_integral[0] + 1j*imag_integral[0])

def complexintegral2(func, lim, **kwargs):
    def real_func(x,y):
        return np.real(func(x,y))
    def imag_func(x,y):
        return np.imag(func(x,y))
    real_integral = integrate.nquad(real_func, lim, **kwargs)
    imag_integral = integrate.nquad(imag_func, lim, **kwargs)
    return (real_integral[0] + 1j*imag_integral[0])    


wa=1
gamma=0.05
rho=np.zeros((2,2),dtype=complex)
T=np.linspace(0,60,100)
Entanglement=np.zeros(len(T))
rho12 = np.loadtxt("rho12.txt", dtype = np.complex128)
rho22 = np.loadtxt("rho22.txt", dtype = np.complex128)
for i in range(len(T)):
  rho[0,1]=rho12[i]
  rho[1,0]=np.conjugate(rho12[i])
  rho[1,1]=rho22[i]
  func1= lambda w1,w2,t2,t1 : w1**2*w2**2*np.exp(-gamma*t2)*np.exp(gamma*t1)*np.exp(1j*(w2-wa)*t2)*np.exp(-1j*(w1-wa)*t1)*np.exp(-(w1-1)**2)\
  *np.exp(-w1**2)*np.exp(-(w2-1)**2)*np.exp(-w2**2) 
  func11= lambda w1,w2,t2,t1 : w1**2*w2**2*2*gamma*np.exp(-2*gamma*t2)*np.exp(gamma*t1)*np.exp(1j*(w2-wa)*t2)*np.exp(-1j*(w1-wa)*t1)*np.exp(-(w1-1)**2)\
  *np.exp(-w1**2)*np.exp(-(w2-1)**2)*np.exp(-w2**2) 
  func112= lambda w1,t1 : w1**2*np.exp(gamma*t1)*np.exp(-1j*(w1-wa)*t1)*np.exp(-(w1-1)**2)
  func12= lambda w1,w2,t2,t1 : w1**2*w2**2*np.exp(-gamma*t2)*np.exp(gamma*t1)*np.exp(1j*(w2-wa)*t2)*np.exp(-1j*(w1-wa)*t1)*np.exp(-(w1-1)**2)\
  *np.exp(-w1**2)*np.exp(-(w2-1)**2)*np.exp(-w2**2)
  rho11=np.exp(-2*gamma*T[i])-2*np.exp(-2*gamma*T[i])*4*(math.pi)*np.real(complexintegral1(func1, [[-10,10],[-10,10],limt2,[0,T[i]]]))\
  +np.exp(-2*gamma*T[i])-2*np.exp(-2*gamma*T[i])*4*(math.pi)*np.real(complexintegral1(func11, [[-10,10],[-10,10],limt2,[0,T[i]]])\
  *np.exp(-2*gamma*T[i])-2*np.exp(-2*gamma*T[i])*2*(math.pi)*complexintegral2(func112, [[-10,10],[0,T[i]]]))\
  +np.exp(-2*gamma*T[i])-2*np.exp(-2*gamma*T[i])*4*(math.pi)*np.absolute(complexintegral1(func12, [[-10,10],[-10,10],limt2,[0,T[i]]]))**2
  rho[0,0]=rho11
  print(rho11)
  print(rho11*rho22-rho12*rho21)
  N=1/(np.trace(rho))
  rho=N*rho
  Entanglement[i]=1-np.trace(np.dot(rho,rho))
  

plt.plot(T,Entanglement)
plt.xlabel("Time")
plt.ylabel("Entanglement")
plt.title("Entanglement vs T")
plt.show