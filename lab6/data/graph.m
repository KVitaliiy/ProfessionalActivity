Res = dlmread('tp=0.27\perfect.txt');
Res = Res';
U = Res(1,:);
Angle = Res(2,:);
RotationAngle = Res(3,:);
TettaAngle = Res(4,:);
Time = Res(5,:);
plot(Time, Angle);
hold on
plot(U,Time);