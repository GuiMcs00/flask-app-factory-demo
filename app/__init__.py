from flask import Flask

"""Create your flask app factory."""


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    with app.app_context():
        from .models import ModelFactory
        ModelFactory.init_app(app.config['DATABASE_URI'], app.config['DATABASE'])
        from .routes import bp
        app.register_blueprint(bp)

    return app
