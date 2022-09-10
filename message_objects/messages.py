import random

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
        r = self.core.match_keyword(self.raw_message)
        if "&" in r:
            if r == "&today-in-history":
                r = api.whatstoday()
        else:
            ls = r.split("|")
            r = random.choice(ls)
        api.send_private_msg(self.user_id, '', r)

    def __eq__(self, other):
        return other == "PrivateMessage"

class GroupMessage(Message):

    def __init__(self, d: dict):
        super(GroupMessage, self).__init__(d)
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "anonymous" in d:
            self.__dict__["anonymous"] = d["anonymous"]




