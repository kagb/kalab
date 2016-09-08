# -*- coding: utf-8 -*-

import redis
from conf import REDIS_HOST, REDIS_PORT


POOL = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT)


class KaRedis(redis.StrictRedis):

    def hset_or_incr(self, name, key, amount):
        if self.hexists(name, key):
            self.hincrby(name, key, amount)
        else:
            self.hset(name, key, amount)
        return self.hget(name, key)


redis_store = KaRedis(connection_pool=POOL)
