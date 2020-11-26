#%%
import numpy as np
import matplotlib.pyplot as plt
from numpy import ones,zeros, pi
# %%
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['font.size'] = 20
plt.rcParams['figure.figsize'] = [16,12]
#%%

M = 100
N = M + 1

wc1 = 500
wc2 = 1000
wc = np.sqrt(wc1*wc2)
ws = 3000

kp = int(N*wc1/ws)
kr = int(N*wc2/ws)

print(wc)
#%%
A = ones(N)
A[kp:kr] = zeros(kr-kp)
k = np.arange(1,int(M/2)+1)
h = np.zeros(N)
# %%
for n in range(N):
    aux = (-1)**k * A[k] * np.cos((k*pi*(1+2*n))/N)
    h[n] = A[0] + 2*np.sum(aux)
h = h/N
# %%
#janelamento
#h = h*np.hanning(N)
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
ax1.set_ylabel('potência (dB)',color = 'blue')
ax1.plot(freq*ws,10*np.log10(mod_H),color = 'blue',label='Ganho')
#plt.legend(['Ganho'])
ax1.tick_params(axis='y', labelcolor='blue')
ax1.grid(True)
ax2 = ax1.twinx()
ax2.set_ylabel('fase (rad)',color = 'red')
ax2.plot(freq*ws, phase, color='red',label='Fase')
ax2.tick_params(axis='y', labelcolor='red')
plt.xlim([0,1500])
plt.title('Resposta em Frequência do filtro implementado')
ax1.legend(loc='upper left')
ax2.legend(loc='center left')

# %%
