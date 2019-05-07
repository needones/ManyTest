from flask_bootstrap import Bootstrap
from flask_cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_session import Session

from App.models import db


#flask-script  flask-blueprint  flask-session  flask-sqlalchemy flask-migrate
from App.views import blue, cache


def init_ext(app):
    app.register_blueprint(blueprint=blue)
    #密钥 SECRET_KEY   SESSION_TYPE=‘redis’
    Session(app=app)
    #SQLALCHEMY_DATABASE_URI  SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app=app)
    migrate = Migrate()
    migrate.init_app(app=app,db=db)
    Bootstrap(app=app)
    debugtoolbar = DebugToolbarExtension()
    debugtoolbar.init_app(app=app)
    cache.init_app(app=app)


