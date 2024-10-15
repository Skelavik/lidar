import socket
import time
import random

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        i = 0
        mas = []
        while True:
            if i < 360:
                time.sleep(0.02)  # Sleep for 1 second
                #d = random.uniform(55,60)  # Example value
                #conn.sendall(i.encode('utf-8'))
                #conn.sendall(d.encode('utf-8'))
                data = f"{i}:{random.uniform(55, 60)}"  # Строка с углом и расстоянием
                conn.sendall(data.encode('utf-8'))
                i = i + 1
            else:
                i = 0
