# lidar_udp_receiver.py
import socket
import struct

UDP_IP = "0.0.0.0"
UDP_PORT = 8888
BUFFER_SIZE = 1  # Должно совпадать с ESP32

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Жду данные от LiDAR...")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE * 2)  # uint16_t = 2 байта
    if len(data) == BUFFER_SIZE * 2:
        # Распаковываем как 100 целых чисел (беззнаковых, 2 байта)
        distances = struct.unpack('<' + 'H' * BUFFER_SIZE, data)  # '<' = little-endian
        for d in distances:
            print(d)  # Каждое значение в отдельной строке
    else:
        print(f"Неверный размер пакета: {len(data)} байт")
