from core.app import App


# app = App('door.home', door='door0')
# app = App('matchstick.home')
app = App('exploration.home', key=True)
# app = App('dragon.home')
app.set_state('solved', False)
app.run()
print(app.get_state('solved'))
