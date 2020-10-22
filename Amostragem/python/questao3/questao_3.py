import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from numpy import pi
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['font.size'] = 30
plt.rcParams['figure.figsize'] = [30,14]
path = '/home/rosinante/PDS/PDS_UFCG/python/questao3/'
#%% Function
t = sp.symbols('t')
f = sp.cos(2*np.pi*3200*t) + 0.5*sp.cos(2*np.pi*600*t) + 0.01*sp.cos(2*np.pi*300*t)
x = sp.lambdify(t,f,'numpy')
#%% Continuous
L = 10
Fs = int(6000/L)
Ts = 1/Fs
t_sampled = np.linspace(0,1,Fs)
x_sampled = x(t_sampled)

#%% Sampled
F = 20*6400
T = 1/F
t_continuous = np.linspace(0,1,F)
x_continuous = x(t_continuous)

# %% FFT continuous
y_continuous = np.fft.fft(x_continuous)
y_continuous = np.abs(y_continuous)/np.max(np.abs(y_continuous))
nc = x_continuous.size
freq_continuous = np.fft.fftfreq(nc,d=T)#*T*2*pi

# %% FFT sampled
y_sampled = np.fft.fft(x_sampled)
y_sampled = np.abs(y_sampled)/np.max(np.abs(y_sampled))
n = x_sampled.size
freq_sampled = np.fft.fftfreq(n,d=Ts)#*Ts*2*pi

#%% plot FFT continuous
fig = plt.figure()
labels = ['-pi','-pi/2','0','pi/2','pi']
plt.plot(freq_continuous,y_continuous)
#plt.xticks(np.arange(-pi,pi+1,pi/2),labels)
plt.xlim([-3200-100,3200+100])
plt.xlabel('frequency (Hz)')
plt.title('Continuous Fourier transformed function')
fig.savefig(path+'fft_continuous.png')

#%% plot FFT sampled
fig = plt.figure()
plt.stem(freq_sampled,y_sampled)
#plt.xticks(np.arange(-pi,pi+1,pi/2),labels)
#plt.xlim([-3200-100,3200+100])
plt.grid(True)
plt.xlabel('frequency (Hz)')
plt.title('Sampled Fourier transformed function')
plt.legend(['Fs = '+str(Fs)+' Hz'])
fig.savefig(path+'fft_sampled_Fs_'+str(Fs)+'Hz.png')
#%%
fig = plt.figure()
plt.plot(freq_continuous,y_continuous,'k-')
plt.stem(freq_sampled,y_sampled,'r--')
#plt.xticks(np.arange(-pi,pi+1,pi/2),labels)
plt.xlim([-3200-100,3200+100])
plt.xlabel('frequency (Hz)')
plt.title('Continuous and Sampled Fourier transformed functions')
plt.grid(True)
plt.legend(['Continuous','Sampled - Fs = '+str(Fs)+' Hz'])
fig.savefig(path+'fft_both_Fs_'+str(Fs)+'Hz.png')