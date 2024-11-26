from tkinter.ttk import Frame
from PIL import Image, ImageTk
import tkinter as tk

from logics.dragon import DragonsLogic


class DragonRiddlePage:
    
    def __init__(self):
        self.riddle_bg_img_path = 'assets/images/riddle_background.png'
        self.riddles_path = 'assets/riddles/'
        
        self.riddles = DragonsLogic(self.riddles_path)
        
    
    def frame(self, app, frame: Frame):
        frame.pack()
        
        msg = self.riddles.riddles[app.getState('riddle')]['riddle']

        img = Image.open(self.riddle_bg_img_path)
        img = img.resize((800, 800))
        photo = ImageTk.PhotoImage(img)

        frame.photo = photo

        canvas = tk.Canvas(frame, width=800, height=800)
        canvas.pack(fill='both', expand=True)
        canvas.create_image(0, 0, image=photo, anchor='nw')

        question_label = tk.Label(
            frame, text=msg, bg='#fff', )
        canvas.create_window(300, 50, window=question_label)

        answer_entry = tk.Entry(frame)
        canvas.create_window(300, 100, window=answer_entry)
