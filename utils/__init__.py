# -*- coding: utf-8 -*-

from md5 import md5


def url_hash(url):
    if isinstance(url, unicode):
        url = url.encode('utf-8')
    return md5(url).hexdigest()
