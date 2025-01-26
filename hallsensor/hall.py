import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

hallpin = 12

gpio.setup(hallpin, gpio.IN)
while True:
	if(gpio.input(hallpin) == False):
		print('1')
	else:
		print(0)