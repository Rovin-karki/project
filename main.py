from kivy.app import App
import webview
class SimpleApp(App):
    def build(self):
            return
def change_title(window):
  window.change_title('pywebview whoa')

window = webview.create_window('pywebview wow', 'https://pywebview.flowrl.com')
webview.start(change_title, window)
    
# Run the app
if __name__ == '__main__':
    SimpleApp().run()
