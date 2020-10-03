rng('default');
clear all;
close all;

%% Global parameters
Fs = 12000;
ns = 0:Fs;

% Continous ploting
F = 20*Fs;
n = 0:F;

% Resample
M = 2;
L = 1;
%% Sampled function  
xHandle =  @(t) cos(2*pi*3200*t) ...
            + 0.5*cos(2*pi*600*t) ...
            + 0.01*cos(2*pi*300*t);
xContinuous = xHandle(n/F);
x = xHandle(ns/Fs);

%% Plotting
figure();
fplot(xHandle,"LineWidth",1.5,'Color',[0.985 0.727 0.258])
hold on
stem(ns/Fs,x,"filled");
xlim([0 0.01]); grid on;
xticks([0 0.002 0.004 0.006 0.008 0.01])
xlabel("t [s]", "Interpreter","latex")

legend("Sinal contínuo","Amostrado","Location","northoutside",...
    "Orientation","horizontal")

%% FFT
y = fft(x);                               
nFFT = length(x);      

% double sided FFT
y0 = fftshift(y);

m = abs(y0); 
f = (-nFFT/2:nFFT/2-1)*(2*pi/nFFT); 

% FFT continuous
yC = fft(xContinuous);                               
nFFTC = length(xContinuous);      

% double sided FFT
y0C = fftshift(yC);

mC = abs(y0C); 
fC = (-nFFTC/2:nFFTC/2-1)*(2*pi*F/Fs/nFFTC); 

%
figure();
plot(fC,mC,"LineWidth",2), hold on,
plot(f,m,"LineWidth",2)
ylabel('Magnitude')
xlabel('Frequency (Hz)'),
grid;
%% Resampling
Fn = Fs/M*L;
fn = (-nFFT/2:nFFT/2-1)*(2*pi*Fs/Fn/nFFT); 
plot(fn,m,"LineWidth",2)
%xlim([-10000 10000])
legend("Sinal contínuo", "Amostrado","Reamostrado", ...
    "Location","northoutside","Orientation","horizontal")
xlim([-2*pi 2*pi])
xticks([-2*pi -1.5*pi -pi -0.5*pi 0.0 0.5*pi pi 1.5*pi 2*pi]);
xticklabels({'-2\pi','-1.5\pi','-\pi','-0.5\pi','0.0','0.5\pi','\pi','1.5\pi','2\pi'});

%% In continuous time
nn = 0:Fn;
xn = interp1(ns/Fs,x,nn/Fn);

figure();
fplot(xHandle,"LineWidth",1.5,'Color',[0.985 0.727 0.258]); hold on
stem(ns/Fs,x,"filled");
xlim([0 0.01]); grid on;
xticks([0 0.002 0.004 0.006 0.008 0.01])
xlabel("t [s]", "Interpreter","latex")

stem(nn/Fn,xn,'k');
legend("Sinal contínuo","Amostrado","Reamostrado","Location","northoutside",...
    "Orientation","horizontal")

%% Interpolation

interp = 0;
for i = 1:length(ns)
     interp = interp + x(i)*sinc((n/F-(i-1)/Fs)*Fs);
end

interpn = 0;
for i = 1:length(nn)
     interpn = interpn + xn(i)*sinc((n/F-(i-1)/Fn)*Fn);
end

figure();
fplot(xHandle,"LineWidth",3,'Color',[0.985 0.727 0.258]); hold on
plot(n/F,interp,"LineWidth",1);
xlim([0 0.01]); grid on;
xticks([0 0.002 0.004 0.006 0.008 0.01])
xlabel("t [s]", "Interpreter","latex")

plot(n/F,interpn,'k');
legend("Sinal contínuo","Amostrado","Recuperado","Location","northoutside",...
    "Orientation","horizontal")

%%
Fa = round(16e6/128/13);
% Fa = 3200*4;
na = 0:Fa;
xa = xHandle(na/Fa) + 2.5;

nBits = 10;
levels = linspace(0,5,2^nBits);
qData = discretize(xa,levels);
quant = levels(qData) - 2.5;

figure();
fplot(xHandle,"LineWidth",1.5,'Color',[0.985 0.727 0.258])
hold on
stem(na/Fa,xa-2.5,"filled");
stairs(na/Fa,quant,'k',"LineWidth",1);
xlim([0 0.006]); grid on;
xticks([0 0.002 0.004 0.006])
xlabel("t [s]", "Interpreter","latex")
ylabel("x(t)", "Interpreter","latex")
legend("Sinal contínuo","Amostrado","Quantizado","Location","northoutside",...
    "Orientation","horizontal")