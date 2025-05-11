import RPi.GPIO as GPIO
import time
import threading

# Настройка пинов GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Конфигурация двигателей
MOTOR1_PINS = [4, 17, 27, 22]  # Пин-контакты первого мотора
MOTOR2_PINS = [26, 19, 13, 6]  # Пин-контакты второго мотора

# Настройка всех пинов
all_pins = MOTOR1_PINS + MOTOR2_PINS
for pin in all_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Последовательность шагов
STEP_SEQUENCE = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1]
]

# Параметры моторов
MOTOR1_DELAY = 0.0014
MOTOR2_DELAY = 0.001
STEPS_PER_REVOLUTION = 200

# Флаги для управления потоками
run_motors = True

def motor_worker(motor_pins, delay, direction):
    step_index = 0
    seq = STEP_SEQUENCE[::direction]
    seq_len = len(seq)
    
    while run_motors:
        for pin in range(4):
            GPIO.output(motor_pins[pin], seq[step_index][pin])
        
        step_index = (step_index + 1) % seq_len
        time.sleep(delay)

try:
    # Создаем и запускаем потоки
    thread1 = threading.Thread(
        target=motor_worker, 
        args=(MOTOR1_PINS, MOTOR1_DELAY, 1)
    )
    thread2 = threading.Thread(
        target=motor_worker, 
        args=(MOTOR2_PINS, MOTOR2_DELAY, 1)
    )
    
    thread1.start()
    thread2.start()
    print("Оба мотора запущены одновременно!")

    # Главный поток просто ждет
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Остановка...")
    run_motors = False
    thread1.join()
    thread2.join()

finally:
    GPIO.cleanup()
    print("GPIO очищены")
