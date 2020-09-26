#%%
from matplotlib.pyplot import legend
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from numpy import pi
from scipy import signal
from scipy.fft import fftshift
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['font.size'] = 30
plt.rcParams['figure.figsize'] = [30,14]
#%% Function
t = sp.symbols('t')
f = sp.cos(2*np.pi*3200*t) + 0.5*sp.cos(2*np.pi*600*t) + 0.01*sp.cos(2*np.pi*300*t)
x = sp.lambdify(t,f,'numpy')
#%% Continuous
F = 1000000
T = 1/F
t_continuous = np.linspace(0,1,F)
x_continuous = x(t_continuous)
#%% Sampled
Fs = 2*3200
Ts = 1/Fs
t_sampled = np.linspace(0,1,Fs)
x_sampled = x(t_sampled)
# %% Plotting continuous signal
fig = plt.figure()
plt.plot(t_continuous,x_continuous,'-k')
plt.plot(t_sampled,x_sampled,'r-o')
plt.xlim([0,0.01])
plt.xticks([0, 0.002, 0.004, 0.006, 0.008, 0.01])
plt.legend(['Continuous','Sampled'])
plt.xlabel('time (s)')
plt.title('Continuous and Sampled time functions')
plt.grid(True)
plt.show()
fig.savefig('Func.png')
# %% FFT continuous
y_continuous = np.fft.fft(x_continuous)
y_continuous = np.abs(y_continuous)/np.max(np.abs(y_continuous))
nc = x_continuous.size
freq_continuous = np.fft.fftfreq(nc,d=T)#*T*2*pi

#%% plot FFT continuous
fig = plt.figure()
labels = ['-pi','-pi/2','0','pi/2','pi']
plt.plot(freq_continuous,y_continuous)
#plt.xticks(np.arange(-pi,pi+1,pi/2),labels)
plt.xlim([-3200-100,3200+100])
plt.xlabel('frequency (Hz)')
plt.title('Continuous Fourier transformed function')
fig.savefig('fft_continuous.png')

# %% FFT sampled
y_sampled = np.fft.fft(x_sampled)
y_sampled = np.abs(y_sampled)/np.max(np.abs(y_sampled))
n = x_sampled.size
freq_sampled = np.fft.fftfreq(n,d=Ts)#*Ts*2*pi

#%% plot FFT sampled
fig = plt.figure()
plt.stem(freq_sampled,y_sampled)
#plt.xticks(np.arange(-pi,pi+1,pi/2),labels)
#plt.xlim([-3200-100,3200+100])
plt.grid(True)
plt.xlabel('frequency (Hz)')
plt.title('Sampled Fourier transformed function')
fig.savefig('fft_sampled.png')
#%%
fig = plt.figure()
plt.plot(freq_continuous,y_continuous,'k-')
plt.stem(freq_sampled,y_sampled,'r--')
#plt.xticks(np.arange(-pi,pi+1,pi/2),labels)
plt.xlim([-3200-100,3200+100])
plt.xlabel('frequency (Hz)')
plt.title('Continuous and Sampled Fourier transformed functions')
plt.grid(True)
plt.legend(['sampled','continuous'])
fig.savefig('fft_both.png')

#%% Interpolação
x_interpol = np.interp(t_sampled,t_continuous,x_continuous)
fig = plt.figure()
plt.plot(t_continuous,x_continuous,'k-')
plt.plot(t_sampled,x_sampled,'go',markersize=18)
plt.plot(t_sampled,x_interpol,'r--')
plt.xlim([0,0.01])
plt.xlabel('time (s)')
plt.title('Continuous, Sampled and Interpolated time functions')
plt.grid(True)
plt.legend(['continuous','sampled','Interpoled'])
plt.xticks([0, 0.002, 0.004, 0.006, 0.008, 0.01])
fig.savefig('func_interp.png')