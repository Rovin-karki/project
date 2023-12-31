from kivy.app import App
from kivy.uix.button import Button

class SimpleApp(App):
    def build(self):
        # Create a button with a callback function
        button = Button(text='Hello, Kivy!', on_press=self.on_button_press)
        return button

    def on_button_press(self, instance):
        # Define the action when the button is pressed
        print('Button pressed!')

# Run the app
if __name__ == '__main__':
    SimpleApp().run()
