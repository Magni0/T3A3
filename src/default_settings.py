import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI")

        if not value:
            raise ValueError("DB_URI not set in .env")

        return value

class DevelopmentConfig(Config):
    @property
    def JWT_SECRET_KEY(self):
        value = os.environ.get("JWT_SECRET_KEY")

        if not value:
            raise ValueError("JWT Secret Key not set")
        
        return value
    

class ProductionConfig(Config):
    @property
    def JWT_SECRET_KEY(self):
        value = os.environ.get("JWT_SECRET_KEY")

        if not value:
            raise ValueError("JWT Secret Key not set")
        
        return value
        
class TestingConfig(Config):
    TESTING = True

env = os.environ.get("FLASK_ENV")

if env == "production":
    app_config = ProductionConfig()
elif env == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()