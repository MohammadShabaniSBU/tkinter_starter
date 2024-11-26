from tkinter.ttk import Frame, Label, Button


class SecondPage:

    def __init__(self):
        self.label = None
    
    def frame(self, app, frame: Frame):
        frame.grid()
        
        label = Label(frame, text=app.getState('counter', 1))
        label.grid(column=0, row=0)
        
        Button(frame, text="inc", command=lambda: app.setState('counter', app.getState('counter') + 1)).grid(column=1, row=0)
        
        Button(frame, text="back", command=lambda: app.push('dragon')).grid(column=2, row=0)
