from dotenv import load_dotenv
import os


class Config:
    load_dotenv()

    SECRET_KEY = os.getenv('SECRET_KEY')


class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = os.getenv('DATABASE_URL')
    DATABASE = os.getenv('DATABASE')


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = os.getenv('DEV_DATABASE_URL')
    DATABASE = os.getenv('DEV_DATABASE')


class TestingConfig(Config):
    TESTING = True
    DATABASE_URI = os.getenv('DEV_DATABASE_URL')
    DATABASE = os.getenv('DEV_DATABASE')


def get_config():
    """Use a flask env to define your app config"""

    env = os.getenv("FLASK_ENV", "production")
    if env == "development":
        return DevelopmentConfig()
    elif env == "staging":
        return TestingConfig()
    else:
        return ProductionConfig()
