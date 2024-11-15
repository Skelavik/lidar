import socket
import time
import random
import serial,time
import numpy as np


ser = serial.Serial("/dev/serial0", 115200,timeout=0) # mini UART serial device
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def read_tfluna_data():
    while True:
        counter = ser.in_waiting # count the number of bytes of the serial port
        if counter > 8:
            bytes_serial = ser.read(9) # read 9 bytes
            ser.reset_input_buffer() # reset buffer

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # check first two bytes
                distance = bytes_serial[2] + bytes_serial[3]*256 # distance in next two bytes
                strength = bytes_serial[4] + bytes_serial[5]*256 # signal strength in next two bytes
                temperature = bytes_serial[6] + bytes_serial[7]*256 # temp in next two bytes
                temperature = (temperature/8.0) - 256.0 # temp scaling and offset
                return distance/100.0,strength,temperature


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        i = 0
        while True:
            if i < 360:

                if ser.isOpen() == False:
                    ser.open()  # open serial port if not open

                distance, strength, temperature = read_tfluna_data()  # read values
                print('Distance: {0:2.2f} m, Strength: {1:2.0f} / 65535 (16-bit), Chip Temperature: {2:2.1f} C'. \
                      format(distance, strength, temperature))  # print sample data
                ser.close()  # close serial port

                time.sleep(0.02)  # Sleep for 1 second
                data = f"{i}:{distance}"  # Строка с углом и расстоянием
                conn.sendall(data.encode('utf-8'))
                i = i + 1
		#ser.close()
            else:
                i = 0


