Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... import numpy as np              
... import matplotlib.pyplot as plt
... 
... t0 = 0
... tn = 700
... ndata = 10000
... 
... t = np.linspace(t0,tn,ndata)
... h = t[2]-t[1]
... 
... N = 1000            #rakyat
... I0 = 1
... R0 = 0
... S0 = N - I0 - R0
... 
... I = np.zeros(ndata)
... S = np.zeros(ndata)
... R = np.zeros(ndata)
... 
... I[0] = I0
... S[0] = S0
... R[0] = R0
... 
... Beta = 0.2
... Gamma = 0.1
... 
... for v in range(0, ndata-1):
...     S[v+1] = S[v] - h*Beta/N*S[v]*I[v]
...     I[v+1] = I[v] + h*Beta/N*S[v]*I[v] - h*Gamma*I[v]
...     R[v+1] = R[v] + h*Gamma*I[v]
... 
... plt.plot(t,S,label='S')
... plt.plot(t,I,label='I')
... plt.plot(t,R,label='R')
... 
... plt.legend()
