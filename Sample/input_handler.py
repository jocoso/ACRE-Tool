from typing import Callable, Dict
from pynput import keyboard
from pynput.keyboard import Controller, Key


# Dealing with python poor design
class InputHandler:
    def __init__(self, name: str):
        self.name = name
        self.key_functions: Dict[str, Callable] = {}
        self.keyboard = Controller()
        self.listener = None

    def add_key_function(self, key: str, function: Callable):
        self.key_functions[key] = function

    def on_release(self, key):  # Changed on_release to handle_input
        try:
            if hasattr(key, 'char') and key.char:  # For character keys
                char = key.char
                if char in self.key_functions:
                    self.key_functions[char]()
            elif key == Key.esc:  # Handling the escape key
                if 'esc' in self.key_functions:
                    self.key_functions['esc']()
            return False  # Return False to stop listener (optional)
        except AttributeError:
            pass
        return False

    def integrate_sectioninput(self):
        with keyboard.Listener(on_release=self.on_release) as listener:
            listener.start()
    def severe_sectioninput(self):
    	if self.listener:
    		self.listener.stop()
    		print("Listener stopped")

