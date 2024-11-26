from tkinter.ttk import Frame
from routes.main import createRoutes


class Router:
    def __init__(self, app):
        self.app = app
        self.routes = {}
        self.currentFrame = None
        self.currentRoute = ''
        
        createRoutes(self)

        
    def addRoute(self, name: str, pageClass):
        self.routes[name] = pageClass

    def rerender(self):
        self.push(self.currentRoute)
        
    def push(self, newRoute: str):
        self.currentRoute = newRoute

        page = self.routes[newRoute]()

        if self.currentFrame is not None:
            self.currentFrame.destroy()
        
        frame = Frame(self.app.root)
        page.frame(self.app, frame)

        self.currentFrame = frame
