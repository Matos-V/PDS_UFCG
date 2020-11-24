#%%
import numpy as np
import matplotlib.pyplot as plt
from numpy import ones,zeros
# %%
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['font.size'] = 20
plt.rcParams['figure.figsize'] = [16,12]
#%%

M = 2**8
N = M + 1

omega_p = 5
omega_r = 3.5
omega_s = 30

kp = int(np.floor(N*omega_p/omega_s))
print(kp)
print(M//2 - kp + 1)
kr = int(np.floor(N*omega_r/omega_s))
#%%
passband = ones(kp)
stopband = zeros(M//2 - kp + 1)
#%%
A = np.concatenate([passband,stopband])
#A = np.concatenate([stopband,passband])
k = np.arange(1,M//2)
h = np.zeros(N)
# %%
for n in range(N):
    aux = (-1)**k * A[k] * np.cos((k*np.pi*(1+2*n))/N)
    h[n] = A[0] + 2*np.sum(aux)
h = h/N
# %%
time = np.arange(N)
plt.stem(time,h)
plt.grid(True)
# %%
H = np.fft.fftshift(np.fft.fft(h,))
freq = np.fft.fftshift(np.fft.fftfreq(N))
mod_H = np.abs(H)
phase = np.arctan2(np.imag(H),np.real(H))
phase = np.unwrap(phase)
# %%
fig, ax1 = plt.subplots()
ax1.set_xlabel('frequência (rad/s)')
ax1.set_ylabel('módulo',color = 'blue')
ax1.plot(freq,mod_H,color = 'blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True)
ax2 = ax1.twinx()
ax2.set_ylabel('fase (rad)',color = 'red')
ax2.plot(freq, phase, color='red')
ax2.tick_params(axis='y', labelcolor='red')
