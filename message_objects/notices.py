import api
from .base_objects import Notice


class GroupFileNotice(Notice):

    def __init__(self, d: dict):
        super(GroupFileNotice, self).__init__(d)
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "file" in d:
            self.__dict__["file"] = d["file"]


class GroupAdminNotice(Notice):

    def __init__(self, d: dict):
        super(GroupAdminNotice, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]


class GroupDecreaseNotice(Notice):

    def __init__(self, d: dict):
        super(GroupDecreaseNotice, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "operator_id" in d:
            self.__dict__["operator_id"] = d["operator_id"]

    def __eq__(self, other):
        return other == "GroupDecreaseNotice"

    def react(self):
        api.send_group_msg(self.group_id, "有人退群了￣へ￣")


class GroupIncreaseNotice(Notice):

    def __init__(self, d: dict):
        super(GroupIncreaseNotice, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "operator_id" in d:
            self.__dict__["operator_id"] = d["operator_id"]

    def react(self):
        api.send_group_msg(self.group_id, f"[CQ:at,qq={self.user_id}]\n"
                                          f"欢迎萌新入群！要好好遵守群规哦！\n"
                                          f"[CQ:image,file=https://i0.hdslb.com/bfs/article/12de0f4778b664a5d8f096e89931c90a91ef60e4.jpg@564w_533h_progressive.webp]")

    def __eq__(self, other):
        return other == "GroupIncreaseNotice"


class GroupBanNotice(Notice):

    def __init__(self, d: dict):
        super(GroupBanNotice, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "operator_id" in d:
            self.__dict__["operator_id"] = d["operator_id"]
        if "duration" in d:
            self.__dict__["duration"] = d["duration"]


class FriendAddNotice(Notice):

    def __init__(self, d: dict):
        super(FriendAddNotice, self).__init__(d)
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]


class GroupRecallNotice(Notice):

    def __init__(self, d: dict):
        super(GroupRecallNotice, self).__init__(d)
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "operator_id" in d:
            self.__dict__["operator_id"] = d["operator_id"]
        if "message_id" in d:
            self.__dict__["message_id"] = d["message_id"]


class FriendRecallNotice(Notice):

    def __init__(self, d: dict):
        super(FriendRecallNotice, self).__init__(d)
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "message_id" in d:
            self.__dict__["message_id"] = d["message_id"]


class FriendPokeNotice(Notice):

    def __init__(self, d: dict):
        super(FriendPokeNotice, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "sender_id" in d:
            self.__dict__["sender_id"] = d["sender_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "target_id" in d:
            self.__dict__["target_id"] = d["target_id"]

    def __eq__(self, other):
        return other == "FriendPokeNotice"

    def react(self):
        api.send_private_msg(self.sender_id, '', "好痛！不要再戳啦！\n[CQ:image,file=https://i0.hdslb.com/bfs/article/9d828e830cfddb578c98f5a25f128f6e463a5bc9.jpg@750w_750h_progressive.webp]")


class GroupPokeNotice(Notice):

    def __init__(self, d: dict):
        super(GroupPokeNotice, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "target_id" in d:
            self.__dict__["target_id"] = d["target_id"]

    def __eq__(self, other):
        return other == "GroupPokeNotice"

    def react(self):
        api.send_group_msg(self.group_id, f"[CQ:at,qq={self.user_id}]好痛！不要再戳啦！\n[CQ:image,file=https://i0.hdslb.com/bfs/article/9d828e830cfddb578c98f5a25f128f6e463a5bc9.jpg@750w_750h_progressive.webp]")


class GroupLuckyKingNotice(Notice):

    def __init__(self, d: dict):
        super(GroupLuckyKingNotice, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "group_id" in d:
            self.__dict__["sender_id"] = d["sender_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "target_id" in d:
            self.__dict__["target_id"] = d["target_id"]


class GroupHonorNotice(Notice):

    def __init__(self, d: dict):
        super(GroupHonorNotice, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "group_id" in d:
            self.__dict__["sender_id"] = d["sender_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "honor_type" in d:
            self.__dict__["honor_type"] = d["honor_type"]


class GroupCardNotice(Notice):

    def __init__(self, d: dict):
        super(GroupCardNotice, self).__init__(d)
        if "card_new" in d:
            self.__dict__["card_new"] = d["card_new"]
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "card_old" in d:
            self.__dict__["card_old"] = d["card_old"]


class OfflineFileNotice(Notice):

    def __init__(self, d: dict):
        super(OfflineFileNotice, self).__init__(d)
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "file" in d:
            self.__dict__["file"] = d["file"]


class ClientStatusNotice(Notice):

    def __init__(self, d: dict):
        super(ClientStatusNotice, self).__init__(d)
        if "online" in d:
            self.__dict__["online"] = d["online"]
        if "client" in d:
            self.__dict__["client"] = d["client"]


class EssenceNotice(Notice):

    def __init__(self, d: dict):
        super(EssenceNotice, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "message_id" in d:
            self.__dict__["message_id"] = d["message_id"]
        if "sender_id" in d:
            self.__dict__["sender_id"] = d["sender_id"]
        if "operator_id" in d:
            self.__dict__["operator_id"] = d["operator_id"]