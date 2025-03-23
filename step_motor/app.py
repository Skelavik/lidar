import RPi.GPIO as GPIO
import time

LED_PIN_2 = 22
LED_PIN = 27
DELAY_SECONDS = 0.0005

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)

# Функция для безопасной остановки моторов
def stop_motors():
    # Убедимся, что пины настроены как выходы
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.setup(LED_PIN_2, GPIO.OUT)
    # Установим LOW и дадим время на реакцию
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(LED_PIN_2, GPIO.LOW)
    time.sleep(0.1)  # Короткая задержка для стабилизации

try:
    print("Программа запущена. Для выхода нажмите Ctrl+C")
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        GPIO.output(LED_PIN_2, GPIO.HIGH)
        time.sleep(DELAY_SECONDS)
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.output(LED_PIN_2, GPIO.LOW)
        time.sleep(DELAY_SECONDS)

except KeyboardInterrupt:
    print("\nПрограмма остановлена")

finally:
    stop_motors()  # Явно останавливаем моторы
    GPIO.cleanup()
    print("GPIO очищены")
