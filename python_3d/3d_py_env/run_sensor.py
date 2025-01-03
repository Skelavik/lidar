import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import time

# Общее количество точек (не используется как лимит, а скорее как параметр для генерации)
num_points = 1068
data_points = []

# Функция для генерации данных (имитация датчика)
def data_generator():
    while True: # Бесконечный цикл
        for i in range(num_points):
          r = np.random.uniform(250,300)  # r (дистанция от центра до точки)
          theta = i * (2 * np.pi / num_points) # theta (угол по оси XY)
          phi = np.random.uniform(0, np.pi) # phi (угол по оси ZX)
          yield r, theta, phi
          time.sleep(0.001)  # Задержка для имитации поступления данных

# Функция для преобразования в декартовы координаты
def to_cartesian(r, theta, phi):
    x = r * np.cos(phi) * np.cos(theta)
    y = r * np.cos(phi) * np.sin(theta)
    z = r * np.sin(phi)
    return x, y, z

# Функция обновления графика
def update(frame):
  try:
    r, theta, phi = next(data_iter) # Получаем данные из генератора
    data_points.append((r, theta, phi)) # Добавляем данные к списку

    # Ограничиваем количество отображаемых точек (при необходимости)
    if len(data_points) > 2000:  # Например, если хранить 2000 точек
        data_points.pop(0)  # Удаляем первую точку

    x_vals, y_vals, z_vals = zip(*[to_cartesian(r, theta, phi) for r, theta, phi in data_points]) # Преобразовываем в декартовы

    ax.clear() # Очищаем предыдущий кадр
    ax.scatter(x_vals, y_vals, z_vals, s=1, c='orange') # Отрисовываем точки
    ax.set_title('3D Sphere from Points (Live)') # Заголовок
    ax.axis('off') # Выключаем оси
  except StopIteration:
    pass # Никогда не должен происходить
  return ax,


# Настройка графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

data_iter = data_generator() # Инициализируем генератор
ani = animation.FuncAnimation(fig, update, interval=1, repeat = True) # Устанавливаем repeat = True

plt.show()

