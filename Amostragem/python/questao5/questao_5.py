import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from numpy import pi
from sklearn.metrics import mean_squared_error
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['font.size'] = 30
plt.rcParams['figure.figsize'] = [30,14]
path = '/home/rosinante/PDS/PDS_UFCG/python/questao5/'
#%% Function
t = sp.symbols('t')
f = sp.cos(2*np.pi*3200*t) + 0.5*sp.cos(2*np.pi*600*t) + 0.01*sp.cos(2*np.pi*300*t)
x = sp.lambdify(t,f,'numpy')
#%% Continuous
Fs = 28800
Ts = 1/Fs
t_sampled = np.linspace(0,1,Fs)
x_sampled = x(t_sampled)

#%% Sampled
F = 10*6400
T = 1/F
t_continuous = np.linspace(0,1,F)
x_continuous = x(t_continuous)

#%%
x_interpol = np.interp(t_continuous,t_sampled,x_sampled)
rmse = np.round( np.sqrt( mean_squared_error( x_continuous,x_interpol ) ),2 )

#%%
fig = plt.figure()
plt.plot(t_continuous,x_continuous,'k-')
plt.step(t_sampled,x_sampled,'r-o',where='mid',markersize=15)
plt.xlim([0,0.01])
plt.xticks([0, 0.002, 0.004, 0.006, 0.008, 0.01])
plt.legend(['Continuous','Sampled - RMSE = '+str(rmse)])
plt.xlabel('time (s)')
plt.title('Continuous and Sampled time functions with Fs = '+str(Fs)+' Hz')
plt.grid(True)
plt.show()
fig.savefig(path+'Functions_Fs_'+str(Fs)+'Hz.png')
