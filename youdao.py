# i: hi
# from: AUTO
# to: AUTO
# smartresult: dict
# client: fanyideskweb
# salt: 16463714786855
# sign: 87d4039f3fae258477ed9f01044efa67
# lts: 1646371478685
# bv: 56d33e2aec4ec073ebedbf996d0cba4f
# doctype: json
# version: 2.1
# keyfrom: fanyi.web
# action: FY_BY_REALTlME
import json
import pprint
import random
import time
import hashlib
import urllib.parse
import urllib.request

import fake_useragent


class Youdao_Trans:

    def __init__(self):
        self.ua = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        self.headers = {
            "User-Agent": self.ua,
            'Accept': "application/json, text/javascript, */*; q=0.01",
            'Cookie': "OUTFOX_SEARCH_USER_ID=754697480@10.110.96.157; JSESSIONID=aaaLu7nvOgJ0OgY3Qyt9x; OUTFOX_SEARCH_USER_ID_NCOO=481661678.70409644; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcK8pn0obmBacrTZyt9x; _ntes_nnid=5e18973414a30d70cb2357986d4416ec,1646371488168; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1646376137468",
            'Referer': "https://fanyi.youdao.com/",
        }

    def generate_url(self, e):
        l = time.time()
        l = f'{l:.3f}'.replace('.', '')
        i = l + str(random.randint(0, 10))
        md = hashlib.md5()
        sign_raw = md.update(('fanyideskweb' + e + i + "Ygy_4c=r#e#4EX^NUGUc5").encode())
        sign = md.hexdigest()
        salt = i
        lts = l
        md = hashlib.md5()
        md.update(self.ua.encode())
        bv = md.hexdigest()

        data2 = {
            'i': e,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'sign': sign,
            'salt': salt,
            'lts': lts,
            'bv': bv,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
        }
        return data2

    def trans(self, word):
        url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
        data = bytes(urllib.parse.urlencode(self.generate_url(word)), 'utf-8')
        req = urllib.request.Request(url, data=data, headers=self.headers)
        res = urllib.request.urlopen(req, timeout=5).read()
        data = json.loads(res)
        result = ''
        if data['errorCode'] == 0:
            for i in data['translateResult'][0]:
                src = i['src']
                tgt = i['tgt']
                result += f'原文：{src}\n译文：{tgt}'
        else:
            print('翻译失败! ')
            result = '翻译失败！'
        return result


if __name__ == '__main__':
    yd = Youdao_Trans()
    a = yd.trans('word')
    print(a)