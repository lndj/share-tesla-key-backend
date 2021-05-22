# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import make_response, jsonify
import random
import string
from cryptography.fernet import Fernet
import config as conf
from flask import make_response


def res_error(code=100, msg=''):
    r = {'code': code, 'msg': msg}
    resp = make_response(jsonify(r), 200)
    return resp


def res_ok(code=0, data=None, msg=''):
    r = {'code': code, 'data': data, 'msg': msg}
    resp = make_response(jsonify(r), 200)
    return resp


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
