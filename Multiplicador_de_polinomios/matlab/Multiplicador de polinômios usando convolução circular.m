%% Insira os coeficientes de x1 e x2

x1 = [1 1 1];
x2 = [-1 -1 2];

% apenas modifique até a linha anterior
%
%
%
%
%
%
%
%%
N = length(x2)+length(x1)-1;
%%
if length(x1) > N
    error("N deve ser maior ou igual ao tamanho de x1");
end
if length(x2) > N
    error("N deve ser maior ou igual ao tamanho de xs");
end
%%
x1 = [x1 zeros(1,N-length(x1))];
x2 = [x2 zeros(1,N-length(x2))];
m = 0:1:N-1;
x2 = x2(mod(-m,N)+1);
H = zeros(N,N);
for n  = 1:1:N
    H(n,:) = cirshftt(x2,n-1,N);
end

y = x1*H';
p = poly2sym(y)
%%
function y = cirshftt(x,m,N)
    if length(x) > N
        error("N deve ser maior ou igual ao tamanho de x");
    end
    x = [x zeros(1,N-length(x))];
    n = 0:1:(N-1);
    n = mod(n-m,N);
    y = x(n+1);
end