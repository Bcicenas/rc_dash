# Importing Libraries
import serial
import time
import ps4_controller
import struct

# Get active ps4 controllers
ps4_controller.get_joystics()

# Open serial connection beetwen PC and Arduino
arduino = serial.Serial(port='COM4', baudrate=9600, timeout=.1)

# function to send and read data from/to Arduino
def write_read(x):
	arduino.write(struct.pack("BBB", x[0], x[1], x[2]))
	data = arduino.readline()
	return data

# Remaps ps4 controller values to specific one
def remap_value(x):
	if x == -1:
		return 1
	if x == 1:
		return 3

	return 2

# Main loop for sending and receiving data
while True:
	ps4_controller.check_for_button_press()
	control_array = [remap_value(int(ps4_controller.analog_buttons[0])), remap_value(int(ps4_controller.analog_buttons[5])), remap_value(int(ps4_controller.analog_buttons[4]))]
	write_read(control_array)
	time.sleep(0.1)


