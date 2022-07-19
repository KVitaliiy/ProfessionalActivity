
X = out.yout{1}.Values.Data;
Y = out.yout{2}.Values.Data;
V = out.yout{3}.Values.Data;
T = out.yout{3}.Values.Time;
a = out.yout{4}.Values.Data;
p = out.yout{5}.Values.Data;

plot(T,V);

ke = 0.48756937411725393;
km = ke;
J = 0.002437632;
L = 0.0047;
Kn = 0.95;
kI = 0.1;
kD = 10;
Moth = 0.02;
R = 8.183683911882799;
U = 14.644499694385809*0.48756937411725393;
Kn = Kn*U*180/100/pi;
ks = 80;
kr = 20;
B = 0.169;
r = 0.027;
Kf = 300;

xlabel('T, sec') 
ylabel('V, rad^2+m^2')