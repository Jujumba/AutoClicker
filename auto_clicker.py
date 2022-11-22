from pyautogui import click, position
from time import sleep
from keyboard import is_pressed
from threading import Thread

class Clicker:
    def on_exit(self):
        if is_pressed("q"): exit(0)

    def start_clicker_on_current_pos(self):
        while True:
            point = position()
            click(x=point.x, y=point.y, clicks=20)
            self.on_exit()

    def start_clicker(self, x: int, y: int):
        while True:
            click(x=x, y=y,clicks=20)
            self.on_exit()

    def thread_clicker(self, x: int = None, y: int = None, amount: int = 1):
        [Thread(self.start_clicker_on_current_pos()).start() if x is None or y is None else Thread(self.start_clicker(x, y)).start() for _ in range(amount)]

    def get_current_position(self):
        while True:
            point = position()
            print(f'x = {point.x}, y = {point.y}')
            sleep(1)


if __name__ == '__main__':
    sleep(5)
    clicker = Clicker()
    clicker.thread_clicker(amount=12)
