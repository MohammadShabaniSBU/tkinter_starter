from pages.secondPage import SecondPage
from routes.dragon import create_dragon_routes


def createRoutes(router):
    create_dragon_routes(router)
    
    router.addRoute('mammad', SecondPage)

    router.push('dragon.home')
