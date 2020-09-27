rng('default');
clear all;
close all;
%% Global parameters
Fs = 3200*2;
Ts = 0:1/Fs:1-1/Fs;


%% Continous ploting
F = 1e5;
t = 0:1/F:1-1/F;

%% Sampled function  
xHandle =  @(t) cos(2*pi*3200*t) ...
            + 0.5*cos(2*pi*600*t) ...
            + 0.01*cos(2*pi*300*t);
xContinuous = xHandle(t);
x = xHandle(Ts);

%% Plotting
figure();
fplot(xHandle,"LineWidth",1.5,'Color',[0.985 0.727 0.258])
hold on
stem(Ts,x,"filled");
xlim([0 0.01]); grid on;
xticks([0 0.002 0.004 0.006 0.008 0.01])
xlabel("t [s]", "Interpreter","latex")

legend("Sinal contínuo","Amostrado","Location","northoutside",...
    "Orientation","horizontal")

%% FFT
y = fft(x);                               
n = length(x);      

%% double sided FFT
y0 = fftshift(y);

m = abs(y0); 
f = (-n/2:n/2-1)*(2*pi/n); 

%% FFT continuous
yC = fft(xContinuous);                               
nC = length(xContinuous);      

%% double sided FFT
y0C = fftshift(yC);

mC = abs(y0C); 
fC = (-nC/2:nC/2-1)*(F*2*pi/nC/Fs); 

figure();
plot(fC,mC,"LineWidth",2), hold on,
plot(f,m,"LineWidth",2)
ylabel('Magnitude')
xlabel('Frequency (Hz)'),
grid;
legend("Sinal contínuo", "Amostrado","Location","northoutside","Orientation","horizontal")
xlim([-5000 5000])
xlim([-2*pi 2*pi])
xticks([-2*pi -1.5*pi -pi -0.5*pi 0.0 0.5*pi pi 1.5*pi 2*pi]);
xticklabels({'-2\pi','-1.5\pi','-\pi','-0.5\pi','0.0','0.5\pi','\pi','1.5\pi','2\pi'});
%% Resampling
%%
Fn = Fs*1;
Tn = 0:1/Fn:1-1/Fn;

xn = interp1(Ts,x,Tn,'spline');

figure();
fplot(xHandle,"LineWidth",1.5,'Color',[0.985 0.727 0.258]); hold on
stem(Ts,x,"filled");
xlim([0 0.01]); grid on;
xticks([0 0.002 0.004 0.006 0.008 0.01])
xlabel("t [s]", "Interpreter","latex")

stem(Tn,xn,'k');
legend("Sinal contínuo","Amostrado","Reamostrado","Location","northoutside",...
    "Orientation","horizontal")

%% Interpolation
s = interp1(Tn,xn,t);

% interp = 0;
% for i = 1:length(Ts)
%     interp = interp + x(i)*sinc((t-(i-1)/Fs)*Fs);
% end

figure();
fplot(xHandle,"LineWidth",1.5,'Color',[0.985 0.727 0.258]); hold on
stem(Tn,xn,"filled");
xlim([0 0.01]); grid on;
xticks([0 0.002 0.004 0.006 0.008 0.01])
xlabel("t [s]", "Interpreter","latex")

plot(t,s,'k');
legend("Sinal contínuo","Amostrado","Recuperado","Location","northoutside",...
    "Orientation","horizontal")