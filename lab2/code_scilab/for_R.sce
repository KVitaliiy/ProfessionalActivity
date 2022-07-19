results = read("C:\Users\vital\itmo\professionalActivity\lab2\power_of_energy_positive.txt", -1, 2)
energy = results(:,1)
voltage = results(:,2)
plot2d(energy, voltage,1)
// Далее апроксимация (метод  наименьших квадратов)
sum1 = 0
sum2 = 0
qlines = size(results,1)
for i=1 : qlines
    sum1 = sum1 + energy(i)*voltage(i)
    sum2 = sum2 + energy(i)*energy(i)
end
R = sum1/sum2
model = R*energy
plot2d(energy, model, 2)
legend('Experiment','U = R*I', 4)
