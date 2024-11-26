from tkinter.ttk import Frame, Label, Button

import tkinter as tk
import tkinter.font as tkFont
from tkinter import font
from PIL import Image, ImageTk
# from .dragons_logic import DragonsLogic


class DragonHomePage:
    
    def __init__(self):
        self.voice_path = 'assets/voices/dragon voice.mp3'
        self.main_img_path = 'assets/images/3headDragon.png'

        self.riddles = {}
        # self.riddles = DragonsLogic(self.riddles_path)

        # mixer.init()
        # mixer.music.load(self.voice_path)

        self.is_pressed = True

        self.mute_image = ImageTk.PhotoImage(
            Image.open('assets/images/mute.png'))
        self.vol_image = ImageTk.PhotoImage(
            Image.open('assets/images/volume.png'))
        self.voice_btn_color = '#081c1e'

        self.challenge_img = ImageTk.PhotoImage(
            Image.open('assets/images/challenges.png')
        )
        self.challenge_btn_color = '#fefd89'

    def frame(self, app, frame: Frame):
        frame.grid()
        frame.pack()
        
        self.defaultFont = tkFont.Font(
            family="DragonHunter", weight=font.BOLD, size=20)
        self.titleFont = tkFont.Font(
            family="DragonHunter", weight=font.BOLD, size=20)
        self.btnFont = tkFont.Font(family="DragonHunter", size=16)
        self.inputFont = tkFont.Font(family="DragonHunter", size=16)

        # self.play_voice()


        # Load and display the image
        img = Image.open(self.main_img_path)
        img = img.resize((800, 800))
        photo = ImageTk.PhotoImage(img)
        frame.photo = photo

        self.canvas = tk.Canvas(frame, width=800, height=800)
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=photo, anchor='nw')

        self.challenge_btn1 = self.create_btn(
            235, 150, self.challenge_img, lambda event: self.goToRiddle(app, 0))

        self.challenge_btn2 = self.create_btn(
            380, 60, self.challenge_img, lambda event: self.goToRiddle(app, 1))

        self.challenge_btn2 = self.create_btn(
            530, 150, self.challenge_img, lambda event: self.goToRiddle(app, 2))

        self.voice_btn = self.create_btn(
            20, 20, self.vol_image, self.on_voice_button_press)

    def goToRiddle(self, app, riddle):
        app.setState('riddle', riddle)
        app.push('dragon.riddle')

    def create_btn(self, width, height, icon, func):
        btn = self.canvas.create_image(width, height, image=icon)
        self.canvas.tag_bind(btn, "<Button-1>", func=func)
        return btn

    def play_voice(self):
        try:
            # mixer.music.play()
            self.is_playing = True
        except Exception as e:
            print(f'Error playing music: {e}')

    def pause_voice(self):
        try:
            # mixer.music.pause()
            self.is_playing = False
        except Exception as e:
            print(f'Error pausing music: {e}')

    def on_voice_button_press(self, event):
        if self.is_pressed:
            self.pause_voice()
            self.canvas.itemconfig(self.voice_btn, image=self.mute_image)
        else:
            self.play_voice()
            self.canvas.itemconfig(self.voice_btn, image=self.vol_image)
            # self.voice_btn.configure(image=self.vol_image)
        self.is_pressed = not self.is_pressed

    def render_riddle(self, event, msg):
        riddle_diolog = tk.Toplevel()

        # Set window size
        riddle_diolog.geometry("600x600")
        riddle_diolog.resizable(0, 0)

        # Load and display the image
        img = Image.open(self.riddle_bg_img_path)
        img = img.resize((600, 600))
        photo = ImageTk.PhotoImage(img)

        riddle_diolog.photo = photo

        canvas = tk.Canvas(riddle_diolog, width=600, height=600)
        canvas.pack(fill='both', expand=True)
        canvas.create_image(0, 0, image=photo, anchor='nw')

        question_label = tk.Label(
            riddle_diolog, text=msg, bg='#fff', font=self.titleFont)
        canvas.create_window(300, 50, window=question_label)

        answer_entry = tk.Entry(riddle_diolog, font=self.inputFont)
        canvas.create_window(300, 100, window=answer_entry)

