"""
VW Platform Application Package Constructor
"""

from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

from wcwave_adaptors import default_vw_client

moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

vw_client = default_vw_client()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .share import share as share_blueprint
    app.register_blueprint(share_blueprint, url_prefix='/share')

    from .processing import processing as processing_blueprint
    app.register_blueprint(processing_blueprint, url_prefix='/processing')

    from .visualization import visualization as visualization_blueprint
    app.register_blueprint(visualization_blueprint, url_prefix='/visualization')

    return app
