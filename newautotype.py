import keyboard
import time

def auto_type(text):
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(1)  # Adjust the delay as needed

text_to_type = "ello, World!"
auto_type(text_to_type)