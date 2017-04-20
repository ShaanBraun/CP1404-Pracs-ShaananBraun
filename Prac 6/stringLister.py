from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label

STRINGS = ["Hello", "Why whello there old friend", "How are you these days?",
           "Well apart from being dead I am doing quite well thank you.", "How about you old friend?"]


class StringLister(App):
    def build(self):
        Window.size = (200, 100)
        self.title = "String Lister"
        self.root = Builder.load_file('stringLister.kv')
        return self.root

    def handle_string_printing(self):
        for string in STRINGS:
            label = Label(text=string)
            self.root.ids.base_layout.add_widget(label)
            #TODO Fix error caused here that crashes on start of program


StringLister().run()
