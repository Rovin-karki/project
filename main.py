import webview
from kivy.app import App


class BlankKivyApp(App):
    def build(self):
        # Create a Kivy button
      

        # Return the root widget of the application
        return 

def change_title(window):
  window.change_title('pywebview whoa')

window = webview.create_window('pywebview wow', 'https://pywebview.flowrl.com/')
webview.start(change_title, window)

if __name__ == '__main__':
    # Run the Kivy application
    BlankKivyApp().run()
