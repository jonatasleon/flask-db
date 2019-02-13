"""Main module."""

from flask import Flask
from app.routes import api
from app.extensions import db


def create_app(config='development'):
    """Create and set up Flask app."""
    app = Flask(__name__)
    app.config.from_object(get_config(config))

    register_extensions(app)
    register_blueprints(app)

    return app


def get_config(config):
    config_dict = {
        'test': 'app.config.TestConfig',
    }
    return config_dict[config]


def register_blueprints(app):
    """Register blueprints."""
    app.register_blueprint(api)


def register_extensions(app):
    """Register extensions."""
    db.init_app(app)
