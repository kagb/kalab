# -*- coding: utf-8 -*-

import redis
from conf import REDIS_HOST, REDIS_PORT


POOL = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT)
redis_store = redis.StrictRedis(connection_pool=POOL)
