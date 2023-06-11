from tkinter import ttk
from tkinter import *

from intro import Splash

class Main_Principal(Splash):
    def __init__(self):
        global b
        if b == 0:
            super().__init__()

if __name__ == "__mains__":
    b = 0
    w = Main_Principal()