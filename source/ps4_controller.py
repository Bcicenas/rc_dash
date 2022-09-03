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
pressed_buttons = None

def check_for_button_press():
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.JOYAXISMOTION:
			print(event.value)
			analog_buttons[event.axis] = event.value


