import datetime
import json
import random
import re
import sqlite3
import time
from .base_objects import Message
from core import Core
import api


class PrivateMessage(Message):

    def __init__(self, d: dict, core: Core):
        super(PrivateMessage, self).__init__(d)
        if "temp_source" in d:
            self.__dict__["temp_source"] = d["temp_source"]
        self.core = core

    def reply(self):
        rm = self.raw_message.split('@', 1)[0]
        r = self.core.match_keyword(rm)
        # @Aki学习kw=关键词,rpid=0,rp=回复1|回复2|回复3
        if r == 'opt-learn':
            rmsg = self.raw_message.strip('[CQ:at,qq=%d]' % self.core.config['self_id'])
            x = re.findall(r'kw=(.*?)[,，;]rpid=(\d*?)[,，;]rp=(.*)', rmsg)
            if x:
                x = x[0]
                conn = sqlite3.connect('data/data.db')
                cursor = conn.cursor()
                cursor.execute('select keyword, reply_id from keywords')
                dic = cursor.fetchall()
                if 'opt' in x[2]:
                    r = '学习失败！rp="%s"不被允许！' % x[2]
                else:
                    if x[0] not in map(lambda x: str(x[0]), dic):
                        cursor.execute('insert into keywords (keyword, reply_id) values("%s", %s)' % (x[0], x[1]))
                    if x[1] in map(lambda x: str(x[1]), dic):
                        cursor.execute('select reply from replies where id=%s' % x[1])
                        rpls = cursor.fetchall()[0][0]
                        if x[2] not in rpls.split('|'):
                            cursor.execute('update replies set reply="%s" where id=%s' % (rpls + '|' + x[2], x[1]))
                        else:
                            pass
                        r = '学习成功！'
                    else:
                        cursor.execute('insert into replies values("%s", "%s")' % (x[1], x[2]))
                        r = '学习成功！'
                cursor.close()
                conn.commit()
                conn.close()
            else:
                r = '什么都没学到！'
        elif r == 'opt-TiH':
            r = api.whatstoday()
        elif r == 'opt-date':
            r = time.strftime('%Y/%m/%d', time.localtime(time.time()))
        elif r == 'opt-time':
            r = time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time()))
        elif r == 'opt-kwlist':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select keyword from keywords')
            r = '可触发关键词：\n' + '\n'.join([*map(lambda x: str(x[0]), cursor.fetchall())])
        elif r == 'opt-rplist':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select * from replies')
            r = '已有回复：\n' + '\n'.join(map(lambda x: ' '.join(map(str, x)), cursor.fetchall()))
            cursor.close()
            conn.close()
        elif r == 'opt-feed':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            random.seed(time.time())
            add_int = random.randint(-5, 5)
            cursor.execute('select user_id from user_assets')
            if self.user_id not in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('insert into user_assets (user_id) values(%d)' % self.user_id)
            cursor.execute('select friendliness from user_assets where user_id=%d' % self.user_id)
            pre_fln = cursor.fetchall()[0][0]
            cursor.execute('update user_assets set friendliness=%d where user_id=%d' % (pre_fln+add_int, self.user_id))
            cursor.close()
            conn.commit()
            conn.close()
            if add_int > 0:
                r = '谢谢你陪我聊天！好感度+%d' % add_int
            elif add_int == 0:
                r = '什么都没有发生！'
            else:
                r = '你做的食物好难吃啊！好感度%d' % add_int
        elif r == 'opt-sign':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select user_id from user_assets')
            if self.user_id not in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('insert into user_assets (user_id) values(%d)' % self.user_id)
            cursor.execute('select last_sign from user_assets')
            last_sign_time = cursor.fetchall()[0][0]
            td = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            if last_sign_time != td:
                cursor.execute('select money from user_assets where user_id=%d' % self.user_id)
                money = cursor.fetchall()[0][0]
                random.seed(time.time())
                add_int = random.randint(5, 250)
                cursor.execute(
                    'update user_assets set money=%d where user_id=%d' % (money + add_int, self.user_id))
                cursor.execute(
                    'update user_assets set last_sign="%s" where user_id=%d' % (td, self.user_id))
                cursor.close()
                conn.commit()
                conn.close()
                r = '签到成功！获得了%d个签到币' % add_int
            else:
                cursor.close()
                conn.commit()
                conn.close()
                r = '已经签到过了！'
        elif r == 'opt-jrrp':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select user_id from user_assets')
            if self.user_id not in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('insert into user_assets (user_id) values(%d)' % self.user_id)
            cursor.execute('select last_jrrp from user_assets')
            last_jrrp = cursor.fetchall()[0][0]
            td = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            if last_jrrp != td:
                random.seed(time.time())
                jrrp = random.randint(0, 100)
                cursor.execute('update user_assets set jrrp=%s, last_jrrp="%s" where user_id=%s' % (jrrp, td, self.user_id))
                cursor.close()
                conn.commit()
                conn.close()
                r = '今天%s的人品值为：%d' % (self.sender['nickname'], jrrp)
            else:
                cursor.execute('select jrrp from user_assets where user_id=%d' % self.user_id)
                r = '今天%s的人品值为：%d' % (self.sender['nickname'], cursor.fetchall()[0][0])
                cursor.close()
                conn.commit()
                conn.close()
        elif r == 'opt-money':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select user_id from user_assets')
            if self.user_id not in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('insert into user_assets (user_id) values(%d)' % self.user_id)
            cursor.execute('select money from user_assets where user_id=%d' % self.user_id)
            r = '%s的签到币数量为：%d' % (self.sender['nickname'], cursor.fetchall()[0][0])
            cursor.close()
            conn.commit()
            conn.close()
        elif r == 'opt-myfln':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select user_id from user_assets')
            if self.user_id not in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('insert into user_assets (user_id) values(%s)' % self.user_id)
            cursor.execute('select friendliness from user_assets where user_id=%s' % self.user_id)
            r = 'Aki对%s的好感度为：%s' % (self.sender['nickname'], cursor.fetchall()[0][0])
            cursor.close()
            conn.commit()
            conn.close()
        elif r == 'opt-trans':
            r = api.youdao.trans(self.raw_message.split('@', 1)[-1])
        elif r == 'opt-help':
            r = '查看口令表请回复：查看口令\n\n学习功能请使用：\n学习@kw=关键词,rpid=回复id,rp=回复1|回复2|回复3\n\n翻译功能请使用：\n翻译@要翻译的内容'
        api.send_private_msg(self.user_id, self.group_id if 'group_id' in self.__dict__ else '', r)

    def __eq__(self, other):
        return other == "PrivateMessage"


class GroupMessage(Message):

    def __init__(self, d: dict, core: Core):
        super(GroupMessage, self).__init__(d)
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "anonymous" in d:
            self.__dict__["anonymous"] = d["anonymous"]
        self.core = core

    def __eq__(self, other):
        return other == "GroupMessage"

    def reply(self):
        rm = self.raw_message.split('@', 1)[0]
        r = self.core.match_keyword(rm)
        r = self.core.match_keyword(self.raw_message)
        # @Aki学习kw=关键词,rpid=0,rp=回复1|回复2|回复3
        if r == 'opt-learn':
            rmsg = self.raw_message.strip('[CQ:at,qq=%d]' % self.core.config['self_id'])
            x = re.findall(r'kw=(.*?)[,，;]rpid=(\d*?)[,，;]rp=(.*)', rmsg)
            if x:
                x = x[0]
                conn = sqlite3.connect('data/data.db')
                cursor = conn.cursor()
                cursor.execute('select keyword, reply_id from keywords')
                dic = cursor.fetchall()
                if 'opt' in x[2]:
                    r = '学习失败！rp="%s"不被允许！' % x[2]
                else:
                    if x[0] not in map(lambda x: str(x[0]), dic):
                        cursor.execute('insert into keywords (keyword, reply_id) values("%s", %s)' % (x[0], x[1]))
                    if x[1] in map(lambda x: str(x[1]), dic):
                        cursor.execute('select reply from replies where id=%s' % x[1])
                        rpls = cursor.fetchall()[0][0]
                        if x[2] not in rpls.split('|'):
                            cursor.execute('update replies set reply="%s" where id=%s' % (rpls + '|' + x[2], x[1]))
                        else:
                            pass
                        r = '学习成功！'
                    else:
                        cursor.execute('insert into replies values("%s", "%s")' % (x[1], x[2]))
                        r = '学习成功！'
                cursor.close()
                conn.commit()
                conn.close()
            else:
                r = '什么都没学到！'
        elif r == 'opt-TiH':
            r = api.whatstoday()
        elif r == 'opt-date':
            r = time.strftime('%Y/%m/%d', time.localtime(time.time()))
        elif r == 'opt-time':
            r = time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time()))
        elif r == 'opt-kwlist':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select keyword from keywords')
            r = '可触发关键词：\n' + '\n'.join([*map(lambda x: str(x[0]), cursor.fetchall())])
        elif r == 'opt-rplist':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select * from replies')
            r = '已有回复：\n' + '\n'.join(map(lambda x: ' '.join(map(str, x)), cursor.fetchall()))
            cursor.close()
            conn.close()
        elif r == 'opt-feed':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            random.seed(time.time())
            add_int = random.randint(-5, 5)
            cursor.execute('select user_id from user_assets')
            if self.user_id not in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('insert into user_assets (user_id) values(%d)' % self.user_id)
            cursor.execute('select friendliness from user_assets where user_id=%d' % self.user_id)
            pre_fln = cursor.fetchall()[0][0]
            cursor.execute(
                'update user_assets set friendliness=%d where user_id=%d' % (pre_fln + add_int, self.user_id))
            cursor.close()
            conn.commit()
            conn.close()
            if add_int > 0:
                r = '谢谢你陪我聊天！好感度+%d' % add_int
            elif add_int == 0:
                r = '什么都没有发生！'
            else:
                r = '你做的食物好难吃啊！好感度%d' % add_int
        elif r == 'opt-sign':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select user_id from user_assets')
            if self.user_id not in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('insert into user_assets (user_id) values(%d)' % self.user_id)
            cursor.execute('select last_sign from user_assets')
            last_sign_time = cursor.fetchall()[0][0]
            td = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            if last_sign_time != td:
                cursor.execute('select money from user_assets where user_id=%d' % self.user_id)
                money = cursor.fetchall()[0][0]
                random.seed(time.time())
                add_int = random.randint(5, 250)
                cursor.execute(
                    'update user_assets set money=%d where user_id=%d' % (money + add_int, self.user_id))
                cursor.execute(
                    'update user_assets set last_sign="%s" where user_id=%d' % (td, self.user_id))
                cursor.close()
                conn.commit()
                conn.close()
                r = '签到成功！获得了%d个签到币' % add_int
            else:
                cursor.close()
                conn.commit()
                conn.close()
                r = '已经签到过了！'
        elif r == 'opt-jrrp':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select user_id from user_assets')
            if self.user_id not in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('insert into user_assets (user_id) values(%d)' % self.user_id)
            cursor.execute('select last_jrrp from user_assets')
            last_jrrp = cursor.fetchall()[0][0]
            td = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            if last_jrrp != td:
                random.seed(time.time())
                jrrp = random.randint(0, 100)
                cursor.execute(
                    'update user_assets set jrrp=%s, last_jrrp="%s" where user_id=%s' % (jrrp, td, self.user_id))
                cursor.close()
                conn.commit()
                conn.close()
                r = '今天%s的人品值为：%d' % (self.sender['nickname'], jrrp)
            else:
                cursor.execute('select jrrp from user_assets where user_id=%d' % self.user_id)
                r = '今天%s的人品值为：%d' % (self.sender['nickname'], cursor.fetchall()[0][0])
                cursor.close()
                conn.commit()
                conn.close()
        elif r == 'opt-money':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select user_id from user_assets')
            if self.user_id not in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('insert into user_assets (user_id) values(%d)' % self.user_id)
            cursor.execute('select money from user_assets where user_id=%d' % self.user_id)
            r = '%s的签到币数量为：%d' % (self.sender['nickname'], cursor.fetchall()[0][0])
            cursor.close()
            conn.commit()
            conn.close()
        elif r == 'opt-myfln':
            conn = sqlite3.connect('data/data.db')
            cursor = conn.cursor()
            cursor.execute('select user_id from user_assets')
            if self.user_id not in map(lambda x: x[0], cursor.fetchall()):
                cursor.execute('insert into user_assets (user_id) values(%s)' % self.user_id)
            cursor.execute('select friendliness from user_assets where user_id=%s' % self.user_id)
            r = 'Aki对%s的好感度为：%s' % (self.sender['nickname'], cursor.fetchall()[0][0])
            cursor.close()
            conn.commit()
            conn.close()
        elif r == 'opt-help':
            r = '查看口令表请回复：查看口令\n\n学习功能请使用：\n学习@kw=关键词,rpid=回复id,rp=回复1|回复2|回复3\n\n翻译功能请使用：\n翻译@要翻译的内容'
        elif r == 'opt-trans':
            r = api.youdao.trans(self.raw_message.split('@', 1)[-1])
        r = '[CQ:at,qq=%s]\n' % self.user_id + r
        api.send_group_msg(self.group_id if 'group_id' in self.__dict__ else '', r)




