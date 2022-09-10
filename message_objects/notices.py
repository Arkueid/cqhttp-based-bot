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


class GroupPokeNotice(Notice):

    def __init__(self, d: dict):
        super(GroupPokeNotice, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "group_id" in d:
            self.__dict__["sender_id"] = d["sender_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "target_id" in d:
            self.__dict__["target_id"] = d["target_id"]


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