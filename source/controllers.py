from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
import ps4_controller
import serial_control
import json
import threading
import time
Clock.max_iteration = 20

class DashboardController(FloatLayout):
	'''Create a controller that receives a custom widget from the kv lang file.
	
	Add an action to be called from the kv lang file.
	'''
	stop = threading.Event()

	def start_second_thread(self):
		threading.Thread(target=self.infinite_loop).start()

	def infinite_loop(self):
		while True:
			serial_control.send_data()
			if self.stop.is_set():
				# Stop running this thread so the main Python process can exit.
				return
			time.sleep(0.1)

class StatusController(BoxLayout):
	'''Create a controller that receives a custom widget from the kv lang file.
	Add an action to be called from the kv lang file.
	'''
	def __init__(self, **kwargs):
		self.start_status_update()
		super(StatusController, self).__init__(**kwargs)

	label_status_antena = ObjectProperty()
	label_status_controller = ObjectProperty()
	antena_status = StringProperty()
	controller_status = StringProperty()
	
	def start_status_update(self):
		Clock.schedule_interval(self.check_controller_status, 0.5)

	def check_controller_status(self, dt):
		ps4_controller.get_joystics()
		self.controller_status = 'Connected' if ps4_controller.joysticks else 'Not Connected'

	
class CameraController(BoxLayout):
	pass

class ConsoleController(BoxLayout):
	# text_input_id = ObjectProperty()
	
	def __init__(self, **kwargs):
		self.start_controller_update()
		super(ConsoleController, self).__init__(**kwargs)

	def start_controller_update(self):
		Clock.schedule_interval(self.check_for_controller_input, 0.2)
	
	label_id = ObjectProperty()
	text_input_id = ObjectProperty()
	def on_enter(self):
		self.update_console()

	def check_for_controller_input(self, dt):
		# print(ps4_controller.analog_buttons)
		pass

	def update_console(self, info_text = 'Command: ', value = ''):
		value = self.text_input_id.text if value == '' else value
		self.label_id.text += info_text + value + "\n"
		self.text_input_id.text = ''
