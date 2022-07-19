results = read ("C:\Users\vital\itmo\professionalActivity\lab2\Wnls.txt", -1, 2) // Считывание файла
volt = results(:,1) // Создание матрицы с данными об угле поворота
wnls = results(:,2) // Создание матрицы с данными об времени
plot2d(wnls, volt, 2) // Построение графика на основе считанных данных
aim=[wnls,volt] // Формирование матрицы для аппроксимации
aim=aim' // Транспонирование матрицы (замена столбцов на строки)
sum1 = 0
sum2 = 0
for i=1:10
    sum1 = sum1 + wnls(i)*volt(i)
    sum2 = sum2 + wnls(i)*wnls(i)
end
ke = sum1/sum2
model = ke*wnls
plot2d(wnls, model, 3)
legend('Experiment','E(ω) = ke*ω',4)
k1 = 0.47734614856993474
k2 =  0.4977925996645731
k = (k1+k2)/2
