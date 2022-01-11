import threading
import time

import pygame
joysticks = []
pygame.init()


def get_joystics():
	global joysticks
	joysticks = []
	for i in range(pygame.joystick.get_count()):
		joysticks.append(pygame.joystick.Joystick(i))

pressed_button = None

def get_presed_button():
	print(pressed_button)

buttons = {
	0: "x",
	1: "circle",
	2: "square",
	3: "triangle",
	4: "share",
	5: "PS",
	6: "options",
	7: "left_stick_click",
	8: "right_stick_click",
	9: "L1",
	10: "R1",
	11: "up_arrow",
	12: "down_arrow",
	13: "left_arrow",
	14: "right_arrow",
	15: "touchpad"
}

#0 left analog horizontal
#1 left analog vertical
#2 right analog horizontal
#3 right analog vertical
#4 left trigger
#5 rigth trigger
analog_buttons = {0:0, 1:0, 2:0, 3:0, 4:-1, 5:-1}


def check_for_button_press():
	for event in pygame.event.get():
		if event.type == pygame.JOYBUTTONDOWN:
			print(buttons[event.button] + ' pressed')				

		if event.type == pygame.JOYBUTTONDOWN:
			if event.button == 5:
				print('PS btn pressed. exiting...')

		if event.type == pygame.JOYBUTTONUP:
			print(buttons[event.button] + ' released')	

		if event.type == pygame.JOYAXISMOTION:
			analog_buttons[event.axis] = event.value
			# print(analog_buttons)
# class for ps4 controller
class Ps4Controller(threading.Thread):

	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.name = name
		self.threadID = threadID
		self.counter = counter
		self.break_flag = True

	def run(self):
		print("Starting thread for ps4 controller: " + self.name)
		self.execute_controller_thread()
		print("Exiting thread for ps4 controller: " + self.name)

# 	# 1. checks if controller is connected
# 	def check_connection(self):
# 		return True

# 	# 2. checks id button is pressed
# 	def listen_for_inputs(self):
# 		pass

# 	# 3. runs 1 and 2
	def execute_controller_thread(self):
		while self.break_flag:
			for event in pygame.event.get():
				if event.type == pygame.JOYBUTTONDOWN:
					print(buttons[event.button] + ' pressed')				

				if event.type == pygame.JOYBUTTONDOWN:
					if event.button == 5:
						self.break_flag = False
						print('PS btn pressed. exiting...')

				if event.type == pygame.JOYBUTTONUP:
					print(buttons[event.button] + ' released')	

				if event.type == pygame.JOYAXISMOTION:
					analog_buttons[event.axis] = event.value
					print(analog_buttons)

			time.sleep(0.1)

