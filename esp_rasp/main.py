from flask import Flask, request
import threading

app = Flask(__name__)
current_distance = 0

@app.route('/data', methods=['POST'])
def handle_data():
    global current_distance
    current_distance = int(request.form['distance'])
    return 'OK', 200

@app.route('/')
def show_distance():
    return f'Current Distance: {current_distance} cm'

def run_server():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    # Запуск сервера в отдельном потоке
    server_thread = threading.Thread(target=run_server)
    server_thread.start()
    
    # Основной поток может выполнять другие задачи
    try:
        while True:
            # Здесь можно добавить другую логику
            pass
    except KeyboardInterrupt:
        print("Server stopped")
