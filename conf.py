# -*- coding: utf8 -*-


DEVELOP_MODE = False
MYSQL_DB_NAME = 'kalab'
MYSQL_HOST = 'localhost'
MYSQL_USER = 'ka'
MYSQL_PASSWD = ''


PC_USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
PC_HEADERS = {
    'User-Agent': PC_USER_AGENT,
}


try:
    from local_conf import *
except ImportError:
    pass
