import matplotlib.pyplot as plt
import numpy as np
file = open("examp2.txt") #Открытие файла
lines = file.readlines() #Чтение данных из файла
Geom = [] #массив для даннных о положении робота
Lidar = [] #массив для данных о положении препятсвий
for line in lines: #Сортировка данныхдвижения робота
    geom = line.strip().split(";")[0]
    lidar = line.strip().split(";")[1]
    Geom.append(geom.split(","))
    Lidar.append(lidar.split(","))
file.close() #Закрытие файла после чтения
Geom = np.array(Geom, float)
for i in range(len(Lidar)): #Отсортирровка данных с лидара робота
    Lidar[i]=Lidar[i][80:len(Lidar[i])-40]
Lidar = np.array(Lidar, float)
x = [] #Координаты движения робота
y = []
for i in Geom:
    x.append(i[0])
    y.append((i[1]))
X = [] #Координаты препятствий
Y = []
i = 0
for a, b, phi in Geom:# вычисляем самую левую точку
    phi0 = phi + 2-0.0061*80
    for l in Lidar[i]:
        if l <= 4:
            X.append(round(((l * np.cos(phi0)) + a + 0.3 * np.cos(phi)), 2))
            Y.append(round(((l * np.sin(phi0)) + b + 0.3 * np.sin(phi)), 2))
        phi0 -= 0.0061
    i += 1
phi, ax = plt.subplots()
ax.scatter(X, Y, s=2, color="red") #Параметры графического окна
plt.show()
