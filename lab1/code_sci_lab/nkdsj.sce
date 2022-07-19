results = read ("C:\Users\vital\itmo\professional_activity\laba1\data_for_voltage_20_.txt", -1, 2) // Считывание файла

angle = results(:,1)*%pi/180 // Создание матрицы с данными об угле поворота

time = results(:,2) // Создание матрицы с данными об времени

plot2d(time, angle, 2) // Построение графика на основе считанных данных

aim=[time,angle] // Формирование матрицы для аппроксимации

aim=aim' // Транспонирование матрицы (замена столбцов на строки)

deff('e=func(k,z)','e=z(2)-k(1)*(z(1)-k(2)*(1-exp(-z(1)/k(2))))') // Объявление функции, чьи коэффициенты будут определяться при аппроксимации

att=[15;0.06] // Для отрицательных указать отрицательное значение на первой позиции

[koeffs,errs] = datafit(func,aim,att) //

Wnls = koeffs(1)

Tm = koeffs(2)

j = 0.0023

Mst = j*Wnls/Tm

model=Wnls*(time-Tm*(1-exp(-time/Tm)))

plot2d(time,model,3)
