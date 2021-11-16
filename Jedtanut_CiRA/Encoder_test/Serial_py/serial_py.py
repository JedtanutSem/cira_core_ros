import serial
arduino = serial.Serial('/dev/ttyACM2', 115200, timeout=.1)
while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		data = '{'+data+'}'
		print data
