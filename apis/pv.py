# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
from lib.redis_store import redis_store

__all__ = ['BP_PV']

BP_PV = Blueprint('pv', __name__)
app = BP_PV


REDIS_PAGES_PV_KEY = 'reids-pages-pv-key-v1'


@app.route('/api/pv')
def pv():
    page = request.args.get('page', u'index')
    name = REDIS_PAGES_PV_KEY
    if redis_store.hexists(name, page):
        redis_store.hincrby(name, page, 1)
    else:
        redis_store.hset(name, page, 1)
    return jsonify({'count': int(redis_store.hget(name, page))})
