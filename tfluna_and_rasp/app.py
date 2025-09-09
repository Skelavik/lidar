# app.py
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# Переменная для хранения последнего значения расстояния
# В реальном приложении лучше использовать базу данных или Redis
latest_distance = "Нет данных"

# HTML-шаблон для отображения данных
HTML_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Данные с LiDAR</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
    $(document).ready(function(){
        function updateDistance() {
            $.ajax({
                url: '/get_distance',
                type: 'GET',
                success: function(data) {
                    $('#distance').text(data.distance);
                },
                error: function() {
                    $('#distance').text('Ошибка получения данных');
                }
            });
        }
        // Обновляем данные каждые 500 мс
        setInterval(updateDistance, 500);
        // Инициализируем при загрузке страницы
        updateDistance();
    });
    </script>
</head>
<body>
    <h1>Расстояние с LiDAR:</h1>
    <p id="distance">{{ latest_distance }}</p>
</body>
</html>
"""

@app.route('/')
def index():
    """Главная страница, отображающая данные."""
    # Передаем текущее значение в шаблон при первой загрузке
    return render_template_string(HTML_TEMPLATE, latest_distance=latest_distance)

@app.route('/update_distance', methods=['POST'])
def update_distance():
    """Конечная точка для получения данных от ESP32."""
    global latest_distance
    try:
        distance_str = request.form.get('distance')
        if distance_str is not None:
            latest_distance = distance_str
            print(f"Получено новое расстояние: {latest_distance} см")
            # Возвращаем успешный ответ
            return jsonify({"status": "success", "received_distance": distance_str}), 200
        else:
             print("Ошибка: Не получено значение 'distance' в запросе")
             return jsonify({"status": "error", "message": "Missing 'distance' parameter"}), 400
    except Exception as e:
        print(f"Ошибка при обработке запроса: {e}")
        return jsonify({"status": "error", "message": "Internal Server Error"}), 500

@app.route('/get_distance', methods=['GET'])
def get_distance():
    """Конечная точка для получения текущего значения расстояния браузером."""
    global latest_distance
    return jsonify({"distance": latest_distance})

if __name__ == '__main__':
    # Запуск сервера Flask. 0.0.0.0 означает, что сервер будет доступен по любому IP на RPi.
    # debug=False важно при использовании global переменных и потоков.
    app.run(host='0.0.0.0', port=5000, debug=False)

