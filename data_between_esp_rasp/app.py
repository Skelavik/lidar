# lidar_udp_receiver.py
import socket
import struct

UDP_IP = "0.0.0.0"
UDP_PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Жду данные от LiDAR...")

while True:
    data, addr = sock.recvfrom(2)  # uint16_t = 2 байта
    if len(data) == 2:
        # Распаковываем как 100 целых чисел (беззнаковых, 2 байта)
        dist = struct.unpack('<' + 'H', data)[0]  # '<' = little-endian
        print(dist)  # Каждое значение в отдельной строке
    else:
        print(f"Неверный размер пакета: {len(data)} байт")
