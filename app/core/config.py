import os
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    DB_URL: str = "mysql+aiomysql://fastapi:fastapi@localhost:3306/fastapi"
    
class DevConfig(Config):
    ENV: str = "dev"
    APP_PORT: int = 8000
    DEBUG: bool = True

class ProductionConfig(Config):
    ENV:str = "prod"
    APP_PORT: int = 443
    DEBUG: bool = False
    
def get_config():
    env = os.getenv("ENV")
    config_type = {
        "dev": DevConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]

