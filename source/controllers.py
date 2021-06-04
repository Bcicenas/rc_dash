from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.clock import Clock
import ps4_controller
Clock.max_iteration = 20

class DashboardController(FloatLayout):
	'''Create a controller that receives a custom widget from the kv lang file.
	
	Add an action to be called from the kv lang file.
	'''

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
	# Clock.schedule_interval(lambda dt: ps4_controller.check_for_button_press(), -1)
	label_id = ObjectProperty()
	text_input_id = ObjectProperty()
	def on_enter(self):
		self.label_id.text += 'Command:' + self.text_input_id.text + "\n"
		self.text_input_id.text = ''
