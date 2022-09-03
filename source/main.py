'''
Application from a .kv in a Template Directory
==============================================

This example shows how you can change the directory for the .kv file. You
should see "Hello from template1/test.ky" as a button.

As kivy instantiates the TestApp subclass of App, the variable kv_directory
is set. Kivy then implicitly searches for a .kv file matching the name
of the subclass in that directory, finding the file template1/test.kv. That
file contains the root widget.


'''

import kivy
kivy.require('1.0.7')

from kivy.app import App
from controllers import DashboardController
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')

class DashboardApp(App):
	kv_directory = 'dashboard_templates'
	
	def build(self):
		Window.bind(on_request_close=self.on_request_close)
		return DashboardController()
	
	def on_request_close(self, *args):
		self.textpopup(title='Exit', text='Are you sure?')
		return True
		
	def on_start(self):
		self.root.start_second_thread()

	def on_stop(self):
		# The Kivy event loop is about to stop, set a stop signal;
		# otherwise the app window will close, but the Python process will
		# keep running until all secondary threads exit.
		self.root.stop.set()

	def textpopup(self, title='', text=''):
		"""Open the pop-up with the name.

		:param title: title of the pop-up to open
		:type title: str
		:param text: main text of the pop-up to open
		:type text: str
		:rtype: None
		"""
		box = BoxLayout(orientation='vertical')
		box.add_widget(Label(text=text))
		mybutton = Button(text='OK', size_hint=(1, 0.25))
		box.add_widget(mybutton)
		popup = Popup(title=title, content=box, size_hint=(None, None), size=(600, 300))
		mybutton.bind(on_release=self.stop)
		popup.open()

if __name__ == '__main__':
	DashboardApp().run()
	
# thread1 = Ps4Controller(1, "Thread-1", 1)
# thread1.start()

