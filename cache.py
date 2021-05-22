# !/usr/bin/env python
# -*- coding: utf-8 -*-
from redis import StrictRedis
import config as conf

redis_conf = conf.redis
redis_client = StrictRedis(host=redis_conf['host'], port=redis_conf['port'], password=redis_conf['pass'])

TOKEN_CACHE_KEY_PREFIX = 'token:'
EMAIL_KEY_CODE_KEY_PREFIX = 'email:'


def save_token(email, key_code, value, expire_seconds):
    pipe = redis_client.pipeline()
    pipe.setex(TOKEN_CACHE_KEY_PREFIX + key_code, expire_seconds, value)
    pipe.setex(EMAIL_KEY_CODE_KEY_PREFIX + email, expire_seconds, key_code)
    pipe.execute()


def get_key_code_by_email(email):
    return redis_client.get(EMAIL_KEY_CODE_KEY_PREFIX + email)
