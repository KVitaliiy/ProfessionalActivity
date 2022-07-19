Res = dlmread('degree_rotation_180_.txt');
Res = Res';
Angle = Res(1,:);
Time = Res(2,:); 
Time = Time - Time(1);
plot(Time, Angle);

Angeln = pi;
ke = 0.48756937411725393;
km = ke;
J = 0.002437632;
L = 0.0047;
Moth = 0.023;
Kn = 1;
ki = 0;
kD = 1;
kD = kD/0.0005;
R = 8.183683911882799;
U = 14.644499694385809*0.48756937411725393;
Kn = Kn*U*180/100/pi;
TimeM = out.yout{1}.Values.Time;
AngleM = out.yout{1}.Values.Data;
hold on
plot(TimeM, AngleM);