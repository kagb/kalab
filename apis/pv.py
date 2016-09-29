# -*- coding: utf-8 -*-

from flask import abort, request
from flask_restful import Resource

from lib.redis_store import redis_store

__all__ = ['PagePV']


REDIS_PAGES_PV_KEY = 'reids-pages-pv-key-v1'
ALLOW_PAGES = [u'index']


class PagePV(Resource):

    def get(self):
        page = request.args.get('page', u'index')
        if page not in ALLOW_PAGES:
            abort(400)
        name = REDIS_PAGES_PV_KEY
        pv = redis_store.hset_or_incr(name, page, 1)
        return {'page': page, 'pv': int(pv)}
