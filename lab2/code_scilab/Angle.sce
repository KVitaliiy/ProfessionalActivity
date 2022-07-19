results = read ("C:\Users\vital\itmo\professionalActivity\lab2\data_for__6.283185307179586_.txt", -1, 2) // Считывание файла
angle = results(:,1)*%pi/180 // Создание матрицы с данными об угле поворота
time = results(:,2) // Создание матрицы с данными об времени
time = time - time(1)
plot2d(time, angle, 2) // Построение графика на основе считанных данных
m = 16/1000
r = 2.30/100/2
i = 48
j = i*i*r*r*m/2
aim=[time,angle] // Формирование матрицы для аппроксимации
aim=aim' // Транспонирование матрицы (замена столбцов на строки)
deff('e=func(k,z)','e=z(2)-k(1)*(z(1)-k(2)*(1-exp(-z(1)/k(2))))') // Объявление функции, чьи коэффициенты будут определяться при аппроксимации
att=[15;0.06] // Для отрицательных указать отрицательное значение на первой позиции
[koeffs,errs] = datafit(func,aim,att) //
Wnls = koeffs(1)
Tm = koeffs(2)
Mst = j*Wnls/Tm
model=Wnls*(time-Tm*(1-exp(-time/Tm)))
plot2d(time,model,3)
//plot2d(T.time, T.values, 5)
//plot2d(A.time, A.values, 6)
legend('Experiment','$\theta(t)=\omega_{nls}t-\omega_{nls}T_m+ \omega_{nls}T_m\,exp\bigl(-\frac{t}{T_m}\bigr)$','Model',2)
// plot2d(I.time, I.values, 3) строим зависимость
