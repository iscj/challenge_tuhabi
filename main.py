from fastapi import FastAPI

from app.services import property_services


def get_application():
    _app = FastAPI()
    _app.include_router(property_services.router)

    return _app


app = get_application()