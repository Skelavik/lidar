import numpy as np
from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app)

num_points = 1068
data_points = []

# Функция для генерации данных
def data_generator():
    while True:
        for i in range(num_points):
            r = np.random.uniform(300, 300)
            theta = i * (2 * np.pi / num_points)
            phi = np.random.uniform(0, np.pi)
            socketio.emit('data', {'r': r, 'theta': theta, 'phi': phi})
            time.sleep(0.001)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    threading.Thread(target=data_generator).start()
    socketio.run(app, debug=True)

