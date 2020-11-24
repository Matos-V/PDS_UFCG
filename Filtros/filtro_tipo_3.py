#%%
import numpy as np
import matplotlib.pyplot as plt
from numpy import ones,zeros
# %%
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['font.size'] = 20
plt.rcParams['figure.figsize'] = [16,12]
#%%
M = 64
N = M + 1

omega_p = 10
omega_s = 100
shift = (int(N/2)-kp)//2

kp = int(np.floor(N*omega_p/omega_s))

A = zeros(N)
#A[:kp] = ones(kp)
#A[N-kp:] = ones(kp)
A[int(N/2)-kp-shift:int(N/2)+kp-shift] = ones(len(A[int(N/2)-kp:int(N/2)+kp]))
A
#%%
A[0] = 0
k = np.arange(1,int(M/2)+1)
h = np.zeros(N)
# %%
for n in range(N):
    aux = (-1)**(k+1) * A[k] * np.sin((k*np.pi*(1+2*n))/N)
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

# %%
