Angeln = pi;
ke = 0.48756937411725393;
km = ke;
J = 0.002437632;
L = 0.0047;
R = 8.183683911882799;
U = 14.644499694385809*0.48756937411725393;
Kn = km*ke*ke/4/J/R + 0.01;
TimeM = out.yout{1}.Values.Time;
AngleM = out.yout{1}.Values.Data;
hold on
plot(TimeM,AngleM);