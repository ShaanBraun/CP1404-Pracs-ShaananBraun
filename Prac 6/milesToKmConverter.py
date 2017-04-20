from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class milesToKmConverter(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('milesToKmConverter.kv')
        return self.root

    def handle_increment(self, value):
        try:
            self.root.ids.text_input.text = str(int(self.root.ids.text_input.text)+ value)
            self.handle_conversion(self.root.ids.text_input.text)
        except ValueError:
            self.root.ids.text_input.text = str(0+value)
            self.handle_conversion(self.root.ids.text_input.text)

    def handle_conversion(self, value):
        try:
            miles = int(value)
            km = miles * 1.61
            self.root.ids.label_output.text = value + " miles is " + str(km) + " kilometers"
        except ValueError:
            self.root.ids.text_input.text = "0.0"
            self.root.ids.label_output.text = "Invalid number to convert"




milesToKmConverter().run()
