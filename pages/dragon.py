from tkinter.ttk import Frame, Label, Button


class DragonPage:
    
    def frame(self, app, frame: Frame):
        frame.grid()
        
        label = Label(frame, text=app.getState('counter', 1))
        label.grid(column=0, row=0)
        
        Button(frame, text="inc", command=lambda: app.setState('counter', app.getState('counter') + 1)).grid(column=1, row=0)
        
        Button(frame, text="next", command=lambda: app.push('mammad')).grid(column=2, row=0)
