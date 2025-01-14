import numpy as np
from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

num_points = 10068
data_points = []

# Функция для генерации данных
def data_generator():
    while True:
        for i in range(num_points):
            r = 100  # Фиксированный радиус для сферы
            theta = i * (2 * np.pi / num_points)
            
            # Зависимость phi от theta
            phi =  (i % (num_points // 144)) * (np.pi / (num_points // 144) ) # Делаем так, чтобы было несколько кругов

            x = r * np.cos(phi) * np.cos(theta)
            y = r * np.cos(phi) * np.sin(theta)
            z = r * np.sin(phi)
            
            socketio.emit('data', {'x': x, 'y': y, 'z': z})
            time.sleep(0.01)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=data_generator).start()
    socketio.run(app, host='0.0.0.0')

