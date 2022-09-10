class Base:

    def __init__(self, d: dict):
        self.time = d["time"]
        self.self_id = d["self_id"]
        self.post_type = d["post_type"]


class Message(Base):

    def __init__(self, d: dict):
        super(Message, self).__init__(d)
        self.sub_type = d["sub_type"]
        self.message_id = d["message_id"]
        # 发送者QQ
        self.user_id = d["user_id"]
        self.raw_message = d["raw_message"]
        self.font = d["font"]
        # 发送者信息
        self.sender = d["sender"]


class Request(Base):

    def __init__(self, d: dict):
        super(Request, self).__init__(d)
        self.request_type = d["request_type"]


class Notice(Base):

    def __init__(self, d: dict):
        super(Notice, self).__init__(d)
        self.notice_type = d["notice_type"]


class Meta_Event(Base):

    def __init__(self, d):
        super(Meta_Event, self).__init__(d)
        self.meta_event_type = d["meta_event_type"]



