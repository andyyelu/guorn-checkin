# -*- coding: utf-8 -*-

import requests
from datetime import datetime

GUORN_USERNAME = ''
GUORN_PASSWORD = ''
base_headers = {'Host': 'guorn.com',
                'Origin': 'https://guorn.com',
                'Referer': 'https://guorn.com/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                }
session = requests.Session()
session.headers = base_headers
resp = session.get('https://guorn.com/')
resp = session.post('https://guorn.com/user/login', params={"account": GUORN_USERNAME, "passwd": GUORN_PASSWORD, "keep_login": "true"})
with open('./log.txt', 'a+') as f:
    try:
        r = session.post('https://guorn.com/score/signup')
        if r.json()['status'] == 'ok':
            print('今天签到成功。目前已经连续签到%s天。' % (r.json()['data']['week_count']))
            f.write('今天签到成功。目前已经连续签到%s天, 时间为%s.\n' % (r.json()['data']['week_count'], datetime.now()))
        else:
            print('今天已经签到过，无需再签到了！')
            f.write('今天已经签到过，无须再签到了！本次验证时间为%s\n' % datetime.now())
    except Exception as e:
        print('签到异常', e)
