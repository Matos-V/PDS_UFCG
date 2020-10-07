#%%
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from numpy import pi
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['font.size'] = 30
plt.rcParams['figure.figsize'] = [30,14]
path = '/home/rosinante/PDS/PDS_UFCG/python/questao2/'

#%% Function
t = sp.symbols('t')
f = sp.cos(2*np.pi*3200*t) + 0.5*sp.cos(2*np.pi*600*t) + 0.01*sp.cos(2*np.pi*300*t)
x = sp.lambdify(t,f,'numpy')
#%% Sampled function
L = 4
Fs = int(6400/L)
Ts = 1/Fs
t_sampled = np.linspace(0,1,Fs)
x_sampled = x(t_sampled)

#%% Continuous function 
F = 20*6400
T = 1/F
t_continuous = np.linspace(0,1,F)
x_continuous = x(t_continuous)

# %% Plotting continuous signal
fig = plt.figure()
plt.plot(t_continuous,x_continuous,'-k')
plt.xlim([0,0.01])
plt.xticks([0, 0.002, 0.004, 0.006, 0.008, 0.01])
plt.legend(['x(t)'])
plt.xlabel('t (s)')
plt.title('Continuous time function')
plt.grid(True)
plt.show()
fig.savefig(path+'Func_continuos.png')

#%% Plotting sampled signal
fig = plt.figure()
plt.stem(t_sampled,x_sampled)
plt.xlim([0,0.01])
plt.xticks([0, 0.002, 0.004, 0.006, 0.008, 0.01])
plt.legend(['Sampled - Fs = '+str(Fs)+' Hz'])
plt.xlabel('time (s)')
plt.title('Sampled time function')
plt.grid(True)
plt.show()
fig.savefig(path+'Func_sampled_Fs_'+str(Fs)+'Hz.png')

#%% Plotting both signals
fig = plt.figure()
plt.plot(t_continuous,x_continuous,'-k')
plt.plot(t_sampled,x_sampled,'r-o',markersize = 15,alpha = 0.5)
plt.xlim([0,0.01])
plt.xticks([0, 0.002, 0.004, 0.006, 0.008, 0.01])
plt.legend(['Continuous','Sampled - Fs = '+str(Fs)+' Hz'])
plt.xlabel('time (s)')
plt.title('Continuous and Sampled time functions')
plt.grid(True)
plt.show()
fig.savefig(path+'Functions_Fs_'+str(Fs)+'Hz.png')