Res = dlmread('lqr\edetpramo.txt');
Res = Res';
U = Res(1,:);
psi = Res(2,:);
psi = psi/pi*180;
dpsi = Res(3,:);
dpsi = dpsi/pi*180;
Dtetta = Res(4,:);
Dtetta = Dtetta/pi*180;
Time = Res(5,:);

Um = out.yout{1}.Values.Data;
Dtettam = out.yout{2}.Values.Data;
Dtettam = Dtettam/pi*180;
dpsim = out.yout{3}.Values.Data;
dpsim = dpsim/pi*180;
psim = out.yout{4}.Values.Data;
psim = psim/pi*180;
Timem = out.yout{1}.Values.Time;

hold on
plot(Timem, Dtettam);

xlabel('t, с') 

ylabel('dθ/dt, °/c')

legend('dθ0 = 10°/c','dθ0 = 25°/c', 'dθ0 = 50°/c')