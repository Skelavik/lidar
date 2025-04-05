import RPi.GPIO as GPIO
import time

# Настройка пинов GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Определяем пины для управления L298N
IN1 = 4  # Input 1
IN2 = 17  # Input 2
IN3 = 27  # Input 3
IN4 = 22  # Input 4

# Настраиваем пины как выходы
pins = [IN1, IN2, IN3, IN4]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Последовательность шагов для полношагового режима
STEP_SEQUENCE = [
    [1, 0, 1, 0],  # Шаг 1: A+ B+
    [0, 1, 1, 0],  # Шаг 2: A- B+
    [0, 1, 0, 1],  # Шаг 3: A- B-
    [1, 0, 0, 1]   # Шаг 4: A+ B-
]

# Параметры управления
STEP_DELAY = 0.001  # Задержка между шагами (регулирует скорость)
STEPS_PER_REVOLUTION = 200  # Количество шагов на полный оборот (зависит от мотора)

def rotate_steps(steps, direction=1):
    """Вращение на указанное количество шагов"""
    for _ in range(steps):
        for step in STEP_SEQUENCE[::direction]:
            GPIO.output(IN1, step[0])
            GPIO.output(IN2, step[1])
            GPIO.output(IN3, step[2])
            GPIO.output(IN4, step[3])
            time.sleep(STEP_DELAY)

try:
    # Пример использования
    while True:
        print("Вращение по часовой стрелке")
        rotate_steps(STEPS_PER_REVOLUTION, direction=1)
        
        #print("Пауза 2 секунды")
        #time.sleep(2)
        
        #print("Вращение против часовой стрелки")
        #rotate_steps(STEPS_PER_REVOLUTION, direction=-1)
        
        #print("Пауза 2 секунды")
        #time.sleep(2)

except KeyboardInterrupt:
    print("Программа остановлена пользователем")

finally:
    # Очистка GPIO
    GPIO.cleanup()
    print("GPIO очищены")
