# Importing Libraries
import serial
import time
import ps4_controller
import struct
ps4_controller.get_joystics()
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)
def write_read(x):
	arduino.write(struct.pack("BBB", x[0], x[1], x[2]))
	
	data = arduino.readline()
	return data

def remap_value(x):
	if x == -1:
		return 1
	if x == 1:
		return 3

	return 2

while True:
	ps4_controller.check_for_button_press()

	# num = input("Enter a number: ") # Taking input from user
	# value = write_read(str(int(ps4_controller.analog_buttons[0])))
	# print(ps4_controller.analog_buttons[0])	
	#-1*int(ps4_controller.analog_buttons[5])
	control_array = [remap_value(int(ps4_controller.analog_buttons[0])), remap_value(int(ps4_controller.analog_buttons[5])), remap_value(int(ps4_controller.analog_buttons[4]))]
	value = write_read(control_array)
	# print(int(ps4_controller.analog_buttons[0]), int(ps4_controller.analog_buttons[5]))
	# print(control_array)
	print(remap_value(int(ps4_controller.analog_buttons[0])))
	
	time.sleep(0.1)


