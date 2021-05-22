import json
import logging

import teslapy
from flask import Flask, request
from utils import res_error, res_ok, gen_key_code, encrypt, decrypt
from cache import save_token, get_key_code_by_email
import config as conf
from flask_cors import CORS

app = Flask(__name__)
if conf.is_dev():
    CORS(app)

# todo
SECRET_KEY = b'qaOMUbtW4M31PDU8p0LdwTdgE22coHm00RGOFK-FSQs='


@app.route('/api/auth/login', methods=['POST'])
def auth_tesla():
    email = request.values.get('email')
    password = request.values.get('password')
    valid_seconds = request.values.get('valid_seconds', type=int) or 3600 * 6
    if not email or not password:
        return res_error(msg='参数错误')
    token = None
    try:
        with teslapy.Tesla(email, password) as tesla:
            tesla.fetch_token()
            token = tesla.token
    except Exception as e:
        print(e)
    if not token:
        return res_error(msg='登陆 Tesla 出错，请检查您的输入')
    # 生成一个随机码，将数据加密之后，存储到 Redis，返回该随机码
    key_code = gen_key_code()
    token_str = json.dumps(token)
    token_encrypted = encrypt(SECRET_KEY, token_str)
    save_token(email, key_code, token_encrypted, valid_seconds)
    print(token_encrypted)
    return res_ok(data={'code': key_code})
