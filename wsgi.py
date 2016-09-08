# -*- coding: utf-8 -*-

from flask import Flask
from conf import *


def create_app(app_name):
    app = Flask(app_name)

    from views.index import BP_SITE
    app.register_blueprint(BP_SITE, url_perfix='')

    return app


app = create_app(__name__)
app.debug = DEVELOP_MODE
