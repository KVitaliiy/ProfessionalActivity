Res = dlmread('pireg180_.txt');
Res = Res';
Angle = Res(1,:);
Time = Res(2,:); 
plot(Time, Angle);
Angeln = pi;
ke = 0.48756937411725393;
km = ke;
J = 0.002437632;
L = 0.0047;
Kn = 1.25;
R = 8.183683911882799;
U = 14.644499694385809*0.48756937411725393;
Kn = Kn*U*180/100/pi;
TimeM = out.yout{1}.Values.Time;
AngleM = out.yout{1}.Values.Data;
hold on
plot(TimeM,AngleM);