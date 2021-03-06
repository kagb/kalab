# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from conf import *


def create_app(app_name):
    app = Flask(app_name)

    from views.index import BP_SITE
    app.register_blueprint(BP_SITE, url_prefix='')

    from views.lab import BP_LAB
    app.register_blueprint(BP_LAB, url_prefix='/lab')

    api = Api(app)

    from apis.pv import PagePV
    api.add_resource(PagePV, '/api/pv')

    from apis.lab import WeiboWordCloud
    api.add_resource(WeiboWordCloud, '/api/word_cloud/weibo')

    return app


app = create_app(__name__)
app.debug = DEVELOP_MODE
