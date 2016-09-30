# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource

from lib.redis_store import redis_store
from utils import url_hash
from utils.weibo_cloud import weibo_article_word_cloud

__all__ = ['WeiboWordCloud']


REDIS_WEIBO_WORD_CLOUD_KEY = 'reids-weibo-word-cloud-key-v1'


class WeiboWordCloud(Resource):

    def post(self):
        data = request.get_json(force=True)
        url = data.get('weibo_url', u'')
        name = REDIS_WEIBO_WORD_CLOUD_KEY
        ret = {'status': 1, 'msg': u'失败'}
        if url:
            hash_url = url_hash(url)
            filename = hash_url + '.jpg'
            img_path = redis_store.hget(name, hash_url)
            if img_path:
                status, msg = 0, u'获取成功'
                ret['img_path'] = img_path
            else:
                status, msg, attachment = weibo_article_word_cloud(url, filename)
                if status == 0:
                    ret['img_path'] = attachment
            ret['status'], ret['msg'] = status, msg
        return ret
