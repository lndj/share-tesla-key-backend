# !/usr/bin/env python
# -*- coding: utf-8 -*-


# todo redis-config
from redis import StrictRedis

redis_client = StrictRedis(host='localhost', port=6379)

TOKEN_CACHE_KEY_PREFIX = 'token:'
EMAIL_KEY_CODE_KEY_PREFIX = 'email:'


def save_token(email, key_code, value, expire_seconds):
    pipe = redis_client.pipeline()
    pipe.setex(TOKEN_CACHE_KEY_PREFIX + key_code, expire_seconds, value)
    pipe.setex(EMAIL_KEY_CODE_KEY_PREFIX + email, expire_seconds, key_code)
    pipe.execute()


def get_key_code_by_email(email):
    return redis_client.get(EMAIL_KEY_CODE_KEY_PREFIX + email)
