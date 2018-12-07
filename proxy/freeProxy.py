import redis
import sys
sys.path.append('..')
from spiders import *


class FreeProxy(object):
    def __init__(self):
        return super(FreeProxy, self).__init__()

    def fetch_proxy(self):
        pass
        redis.sadd('raw_proxy',*p)