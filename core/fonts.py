import tkinter.font as tkFont

from tkinter import font


class Fonts:
    def __init__(self, root):
        self.hat_default_font = tkFont.Font(
            family="Blomberg", weight=font.BOLD, size=20)
        self.hat_title_font = tkFont.Font(
            family="Blomberg", weight=font.BOLD, size=20)
        self.hat_btn_font = tkFont.Font(family="Blomberg", size=16)
        self.hat_input_font = tkFont.Font(family="Blomberg", size=16)
