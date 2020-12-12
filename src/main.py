from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object("default_settings.app_config")

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    from controllers import registable_controllers
    for controller in registable_controllers:
        app.register_blueprint(controller)

    return app