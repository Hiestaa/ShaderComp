#!/usr/bin/kivy
import kivy
kivy.require('1.7.2') # replace with your current kivy version !
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty


class Controller(FloatLayout):
    '''Create a controller that receives a custom widget from the kv lang file.

    Add an action to be called from the kv lang file.
    '''
    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = 'My label after button press'
        self.info = 'New info text'

class NestedWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.spinner = Spinner(text='Home',values=('Home', 'Work', 'Other', 'Custom'),size_hint=(None, None),size=(100, 44), pos_hint={'center_x': .5, 'center_y': .5})
        self.spinner.bind(text=show_selected_value)

	def show_selected_value(spinner, text):
	    print('The spinner', spinner, 'have text', text)

		


class SCGuiApp(App):

    def build(self):
        return Controller(info='Hello world')

if __name__ == '__main__':
    SCGuiApp().run()