from tkinter import Tk

from core.router import Router

class App:
    def __init__(self):
        self.root = Tk()
        self.states = {}
        
        self.initWindow()
        
        self.router = Router(self)

    def initWindow(self):
        self.root.geometry("800x800")
        self.root.resizable(0, 0)

    def updateGeometry(self, a):
        self.root.geometry(a)

    def updateTitle(self, title):
        self.root.title(title)

    def push(self, route: str):
        self.router.push(route)

    def getState(self, key: str, defaultValue=None):
        if key in self.states:
            return self.states[key]
        else:
            self.states[key] = defaultValue
            return defaultValue
        
    def setState(self, key: str, value):
        self.states[key] = value

        self.router.rerender()
        
    def run(self):
        self.root.mainloop()
