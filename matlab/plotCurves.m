figure();
Fn = Fs/2;
fn = (-nFFT/2:nFFT/2-1)*(2*pi*Fs/Fn/nFFT); 
subplot(2,2,1);
plot(fn,m,"LineWidth",2)
ylabel('Magnitude')
xlabel('Frequency (Hz)'),
title("F_s=6000Hz");
xlim([-2*pi 2*pi])
xticks([-2*pi -1.5*pi -pi -0.5*pi 0.0 0.5*pi pi 1.5*pi 2*pi]);
xticklabels({'-2\pi','-1.5\pi','-\pi','-0.5\pi','0.0','0.5\pi','\pi','1.5\pi','2\pi'});
grid;

Fn = Fs/4;
fn = (-nFFT/2:nFFT/2-1)*(2*pi*Fs/Fn/nFFT); 
subplot(2,2,2);
plot(fn,m,"LineWidth",2)
xlim([-4*pi 4*pi])
ylabel('Magnitude')
xlabel('Frequency (Hz)'),
title("F_s=3000Hz");
xticks([-4*pi -3*pi -2*pi -pi 0.0 pi 2*pi 3*pi 4*pi]);
xticklabels({'-4\pi','-3\pi','-2\pi','-\pi','0.0','\pi','2\pi','3\pi','4\pi'});
grid;

Fn = Fs/10;
fn = (-nFFT/2:nFFT/2-1)*(2*pi*Fs/Fn/nFFT); 
subplot(2,2,3);
plot(fn,m,"LineWidth",2)
xlim([-8*pi 8*pi])
ylabel('Magnitude')
xlabel('Frequency (Hz)'),
title("F_s=1200Hz");
xticks([-8*pi -6*pi -4*pi -2*pi 0.0 2*pi 4*pi 6*pi 8*pi]);
xticklabels({'-8\pi','-6\pi','-4\pi','-2\pi','0.0','2\pi','4\pi','6\pi','8\pi'});
grid;

Fn = Fs/20;
fn = (-nFFT/2:nFFT/2-1)*(2*pi*Fs/Fn/nFFT); 
subplot(2,2,4);
plot(fn,m,"LineWidth",2)
xlim([-12*pi 12*pi])
ylabel('Magnitude')
xlabel('Frequency (Hz)'),
title("F_s = 600Hz")
xticks([-12*pi -10*pi -8*pi -6*pi -4*pi -2*pi 0.0 2*pi 4*pi 6*pi 8*pi 10*pi 12*pi]);
xticklabels({'-12\pi','-10\pi','-8\pi','-6\pi','-4\pi','-2\pi','0.0','2\pi','4\pi','6\pi','8\pi','10\pi','12\pi'});
grid;


figure();
Fn = Fs/2;
fn = (-nFFT/2:nFFT/2-1)*(2*pi*Fs/Fn/nFFT); 
subplot(2,2,1);
plot(fn,m,"LineWidth",2)
ylabel('Magnitude')
xlabel('Frequency (Hz)'),
title("F_s=6kHz");
xlim([-2*pi 2*pi])
xticks([-2*pi -1.5*pi -pi -0.5*pi 0.0 0.5*pi pi 1.5*pi 2*pi]);
xticklabels({'-2\pi','-1.5\pi','-\pi','-0.5\pi','0.0','0.5\pi','\pi','1.5\pi','2\pi'});
grid;

Fn = Fs;
fn = (-nFFT/2:nFFT/2-1)*(2*pi*Fs/Fn/nFFT); 
subplot(2,2,2);
plot(fn,m,"LineWidth",2)
ylabel('Magnitude')
xlabel('Frequency (Hz)'),
title("F_s=12kHz");
xlim([-2*pi 2*pi])
xticks([-2*pi -1.5*pi -pi -0.5*pi 0.0 0.5*pi pi 1.5*pi 2*pi]);
xticklabels({'-2\pi','-1.5\pi','-\pi','-0.5\pi','0.0','0.5\pi','\pi','1.5\pi','2\pi'});
grid;

Fn = Fs*5/2;
fn = (-nFFT/2:nFFT/2-1)*(2*pi*Fs/Fn/nFFT); 
subplot(2,2,3);
plot(fn,m,"LineWidth",2)
ylabel('Magnitude')
xlabel('Frequency (Hz)'),
title("F_s=30kHz");
xlim([-pi pi])
xticks([-pi -0.75*pi -0.5*pi -0.25*pi 0.0 0.25*pi 0.5*pi 0.75*pi pi]);
xticklabels({'-\pi','-0.75\pi','-0.5\pi','-0.25\pi','0.0','0.25\pi','0.5\pi','0.75\pi','\pi'});
grid;

Fn = Fs*5;
fn = (-nFFT/2:nFFT/2-1)*(2*pi*Fs/Fn/nFFT); 
subplot(2,2,4);
plot(fn,m,"LineWidth",2)
ylabel('Magnitude')
xlabel('Frequency (Hz)'),
title("F_s = 60kHz")
xlim([-pi pi])
xticks([-pi -0.75*pi -0.5*pi -0.25*pi 0.0 0.25*pi 0.5*pi 0.75*pi pi]);
xticklabels({'-\pi','-0.75\pi','-0.5\pi','-0.25\pi','0.0','0.25\pi','0.5\pi','0.75\pi','\pi'});
grid;