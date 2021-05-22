# !/usr/bin/env python
# -*- coding: utf-8 -*-
from os import environ

env = environ.get('FLASK_ENV', 'development')

if env == 'development':
    from .dev import *
elif env == 'production':
    from .prod import *
else:
    raise Exception('Not supported runtime env {}'.format(env))


def get(name, default=None):
    import config as this_module
    return getattr(this_module, name, default)


def is_dev():
    return env == 'development'


def is_prod():
    return env == 'production'


def get_env():
    return env
