from core.app import App


app = App('dragon.home')
app.run()
print(app.get_state('solved'))
