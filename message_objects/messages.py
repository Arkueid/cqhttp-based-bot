import json
import random
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
        if '翻译@' in self.raw_message:
            word = self.raw_message.split('@')[-1]
            self.raw_message = '翻译@'
        elif '学习@' in self.raw_message:
            x = self.raw_message.split('@')
            m_keyword = x[1]
            m_reply = x[2]
            self.raw_message = '学习@'
        r = self.core.match_keyword(self.raw_message)
        if not r:
            return
        if "&" in r:
            if r == "&today-in-history":
                r = api.whatstoday()
            elif r == "&date":
                r = time.strftime("现在时间：%Y年%m月%d %H时%M分%S秒", time.localtime(time.time()))
            elif r == "&feed":
                conn = sqlite3.connect('friendliness.db')
                cursor = conn.cursor()
                cursor.execute('select user_id from user_friendliness;')
                if self.user_id not in tuple(map(lambda x: x[0], cursor.fetchall())):
                    cursor.execute('insert into user_friendliness (user_id, friendliness) values(%s, %d);' % (self.user_id, 50))
                cursor.execute('select friendliness from user_friendliness where user_id=%d' % self.user_id)
                r = cursor.fetchall()
                add_int = random.randint(-5, 5)
                friendliness = r[0][0] + add_int if r[0][0] <= 100 else 100
                cursor.execute('update user_friendliness set friendliness=%d where user_id=%d' % (friendliness, self.user_id))
                cursor.close()
                conn.commit()
                conn.close()
                if add_int > 0:
                    r = 'Yum！yum！好感度+%d' % add_int
                elif add_int < 0:
                    r = '不要再喂啦~好感度%d\n[CQ:image,file=https://image.9game.cn/2019/12/9/127411150.png]' % add_int
                else:
                    r = '嗯~什么都没有发生！'
            elif r == "&trans":
                r = api.youdao.trans(word)
            elif r == "&learn":
                if m_keyword in self.core.keywords or m_keyword in self.core.replies:
                    r = '学习失败！该条目已存在！'
                else:
                    self.core.keywords[m_keyword] = m_keyword
                    self.core.replies[m_keyword] = m_reply
                    with open('data/keywords.json', 'w', encoding='utf-8-sig') as f:
                        f.write(json.dumps(self.core.keywords, ensure_ascii=False, indent=2))
                    with open('data/replies.json', 'w', encoding='utf-8-sig') as f:
                        f.write(json.dumps(self.core.replies, ensure_ascii=False, indent=2))
                    r = '学习成功！'
            elif r == "&friendliness":
                conn = sqlite3.connect('friendliness.db')
                cursor = conn.cursor()
                cursor.execute('select user_id from user_friendliness;')
                if self.user_id not in tuple(map(lambda x: x[0], cursor.fetchall())):
                    cursor.execute('insert into user_friendliness (user_id, friendliness) values(%s, %d);' % (self.user_id, 50))
                cursor.execute('select friendliness from user_friendliness where user_id=%d' % self.user_id)
                r = 'Aki对%s的好感度为：%d' % (self.sender['nickname'], cursor.fetchall()[0][0])
                cursor.close()
                conn.close()

        else:
            ls = r.split("|")
            r = random.choice(ls)
        api.send_private_msg(self.user_id, '', r)

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
        if '翻译@' in self.raw_message:
            word = self.raw_message.split('@')[-1]
            self.raw_message = '翻译@'
        elif '学习@' in self.raw_message:
            x = self.raw_message.split('@')
            m_keyword = x[1]
            m_reply = x[2]
            self.raw_message = '学习@'
        r = self.core.match_keyword(self.raw_message)
        if not r:
            return
        if "&" in r:
            if r == "&today-in-history":
                r = api.whatstoday()
            elif r == "&date":
                r = time.strftime("现在时间：%Y年%m月%d %H时%M分%S秒", time.localtime(time.time()))
            elif r == "&feed":
                conn = sqlite3.connect('friendliness.db')
                cursor = conn.cursor()
                cursor.execute('select user_id from user_friendliness;')
                if self.user_id not in tuple(map(lambda x: x[0], cursor.fetchall())):
                    cursor.execute('insert into user_friendliness (user_id, friendliness) values(%s, %d);' % (self.user_id, 50))
                cursor.execute('select friendliness from user_friendliness where user_id=%d' % self.user_id)
                r = cursor.fetchall()
                add_int = random.randint(-5, 5)
                friendliness = r[0][0] + add_int if r[0][0] <= 100 else 100
                cursor.execute('update user_friendliness set friendliness=%d where user_id=%d' % (friendliness, self.user_id))
                conn.commit()
                conn.close()
                if add_int > 0:
                    r = 'Yum！yum！好感度+%d' % add_int
                elif add_int < 0:
                    r = '不要再喂啦~好感度%d\n[CQ:image,file=https://image.9game.cn/2019/12/9/127411150.png]' % add_int
                else:
                    r = '嗯~什么都没有发生！'
            elif r == "&trans":
                r = api.youdao.trans(word)
            elif r == "&learn":
                if m_keyword in self.core.keywords or m_keyword in self.core.replies:
                    r = '学习失败！该条目已存在！'
                else:
                    self.core.keywords[m_keyword] = m_keyword
                    self.core.replies[m_keyword] = m_reply
                    with open('data/keywords.json', 'w', encoding='utf-8-sig') as f:
                        f.write(json.dumps(self.core.keywords, ensure_ascii=False, indent=2))
                    with open('data/replies.json', 'w', encoding='utf-8-sig') as f:
                        f.write(json.dumps(self.core.replies, ensure_ascii=False, indent=2))
                    r = '学习成功！'
            elif r == "&friendliness":
                conn = sqlite3.connect('friendliness.db')
                cursor = conn.cursor()
                cursor.execute('select user_id from user_friendliness;')
                if self.user_id not in tuple(map(lambda x: x[0], cursor.fetchall())):
                    cursor.execute('insert into user_friendliness (user_id, friendliness) values(%s, %d);' % (self.user_id, 50))
                cursor.execute('select friendliness from user_friendliness where user_id=%d' % self.user_id)
                r = 'Aki对%s的好感度为：%d' % (self.sender['nickname'], cursor.fetchall()[0][0])
                cursor.close()
                conn.close()
        else:
            ls = r.split("|")
            r = random.choice(ls)
        api.send_group_msg(self.group_id, f"[CQ:at,qq={self.user_id}]\n" + r)




