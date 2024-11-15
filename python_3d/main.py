import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

num_points = 1068  # Количество точек
data = np.zeros((num_points, 3))  # Матрица: [r, theta, phi]

# Заполнение данных случайными значениями
for i in range(num_points):
    data[i][0] = 300  # r (дистанция от центра до точки)
    data[i][1] = i * (2 * np.pi / num_points)  # theta (угол по оси XY)
    data[i][2] = np.random.uniform(0, np.pi)  # phi (угол по оси ZX)

# Преобразование в декартовы координаты
x = data[:, 0] * np.cos(data[:, 2]) * np.cos(data[:, 1])
y = data[:, 0] * np.cos(data[:, 2]) * np.sin(data[:, 1])
z = data[:, 0] * np.sin(data[:, 2])

# Отрисовка сферы
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s=1, c='orange')  # Отрисовка точек

# Настройка графика
ax.set_title('3D Sphere from Points')  # Убрали оси
ax.axis('off')  # Отключение отображения осей

plt.show()
