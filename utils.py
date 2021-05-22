# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import make_response
import random
import string
from cryptography.fernet import Fernet


def res_error(code=100, msg=''):
    return {'code': code, 'msg': msg}


def res_ok(code=0, data=None, msg=''):
    return {'code': code, 'data': data, 'msg': msg}


def gen_key_code():
    return ''.join(random.sample(string.ascii_letters + string.digits, 12))


def encrypt(key, value):
    if type(value) == str:
        value = value.encode()
    f = Fernet(key)
    return f.encrypt(value)


def decrypt(key, value):
    if type(value) == str:
        value = value.encode()
    f = Fernet(key)
    return f.decrypt(value)
