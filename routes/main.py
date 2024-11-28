from pages.secondPage import SecondPage
from routes.dragon import create_dragon_routes
from routes.hat import create_hat_routes


def create_routes(router):
    create_dragon_routes(router)
    create_hat_routes(router)
