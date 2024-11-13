from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.routes.routes import routers as v1_routers 

def init_routers(_app: FastAPI):
    _app.include_router(v1_routers)
    logging.info("Routers initialized")


def create_app() -> FastAPI:
    _app = FastAPI()
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  
        allow_credentials=True,
        allow_methods=["*"],  
        allow_headers=["*"],
    )
    
    init_routers(_app=_app)
    return _app


app = create_app()
