from pages.dragon.home import DragonHomePage
from pages.dragon.riddle import DragonRiddlePage


def create_dragon_routes(router):
    router.addRoute('dragon.home', DragonHomePage)
    router.addRoute('dragon.riddle', DragonRiddlePage)
