from pages.dragon import DragonPage
from pages.secondPage import SecondPage


def createRoutes(router):
    router.addRoute('dragon', DragonPage)
    router.addRoute('mammad', SecondPage)

    router.push('dragon')
