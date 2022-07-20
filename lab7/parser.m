Res = dlmread('C:\Users\vital\itmo\2sem\professionalActivity\lab7\data\ozk\test_7_0.txt');
Res = Res';
T = Res(1,:);
tetta1 = Res(2,:);
tetta2 = Res(3,:);
tetta3 = Res(4,:);

hold on

plot(T, tetta3);

xlabel('t, с'); 

ylabel('dθ/dt, °/c');

legend('dθ0 = 10°/c','dθ0 = 25°/c', 'dθ0 = 50°/c');