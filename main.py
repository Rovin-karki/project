import webview
import gradio as gr
import threading
from kivy.app import App

# Define the Gradio program
def greet(name):
    return "Hello, " + name + "!"

iface = gr.Interface(greet, "text", "text", title="Greeting App", description="Enter your name to get a greeting")

# Define the function that launches the Gradio program in a PyWebView window
def launch_gradio():
    iface.launch(inbrowser=False)  # Set inbrowser to False to prevent opening in a browser

# Start the Gradio interface in a separate thread
gradio_thread = threading.Thread(target=launch_gradio)
gradio_thread.start()

# Create the PyWebView window
webview.create_window("Hello world", "http://127.0.0.1:7860/")
webview.start()





class BlankKivyApp(App):
    def build(self):
        # Create a Kivy button
      

        # Return the root widget of the application
        return 


if __name__ == '__main__':
    # Run the Kivy application
    BlankKivyApp().run()
