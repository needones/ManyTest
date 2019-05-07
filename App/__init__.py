import os

from flask import Flask

from App import settings
from App.ext import init_ext


def create_app(ENV_NAME):
    print(settings.BASE_DIR)
    templates_folder = os.path.join(settings.BASE_DIR, 'templates')
    static_folder = os.path.join(settings.BASE_DIR,'static')
    print(static_folder)
    print(templates_folder)
    app = Flask(__name__,template_folder=templates_folder,static_folder=static_folder)
    app.config.from_object(settings.env.get(ENV_NAME))
    init_ext(app)
    return app
