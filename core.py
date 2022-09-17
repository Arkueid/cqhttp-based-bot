import json
import random
import re
import sqlite3
import time


class Core:

    def __init__(self, config_path):
        self.config = json.loads(open('data/config.json', 'r', encoding='utf-8-sig').read())

    def match_keyword(self, raw_message: str):
        if '[CQ:at,qq=%d]' % self.config['self_id'] in raw_message or '@%s' % self.config['self_nickname'] in raw_message:
            # 执行命令操作
            raw_message = raw_message.strip('[CQ:at,qq=%d]@%s' % (self.config['self_id'], self.config['self_nickname']))
            conn = sqlite3.connect(self.config['database'])
            cursor = conn.cursor()
            cursor.execute('select keyword from keywords')
            if raw_message in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('select reply_id from keywords where keyword="%s"' % raw_message)
                reply_id = cursor.fetchall()[0][0]
                cursor.execute('select reply from replies where id=%s' % reply_id)
                r = cursor.fetchall()[0][0]
            else:
                r = '你在说什么啊？'
            conn.close()
        else:
            # 执行自动回复
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select keyword from keywords')
            for i in map(lambda x: x[0], cursor.fetchall()):
                if i == raw_message:
                    match_word = i
                    break
            else:
                return
            cursor.execute('select reply_id from keywords where keyword="%s"' % match_word)
            r = cursor.fetchall()[0][0]
            cursor.execute('select reply from replies where id=%s' % r)
            r = cursor.fetchall()[0][0]
            random.seed(time.time())
            r = random.choice(r.split('|'))
        return r


if __name__ == '__main__':
    c = Core('data/config.json')
    c.match_keyword('[CQ:at,qq=3515950251]时间')