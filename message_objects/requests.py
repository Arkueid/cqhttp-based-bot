from .base_objects import Request


class FriendAddRequest(Request):

    def __init__(self, d: dict):
        super(FriendAddRequest, self).__init__(d)
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "comment" in d:
            self.__dict__["comment"] = d["comment"]
        if "flag" in d:
            self.__dict__["flag"] = d["flag"]


class GroupJoinRequest(Request):

    def __init__(self, d: dict):
        super(GroupJoinRequest, self).__init__(d)
        if "sub_type" in d:
            self.__dict__["sub_type"] = d["sub_type"]
        if "group_id" in d:
            self.__dict__["group_id"] = d["group_id"]
        if "user_id" in d:
            self.__dict__["user_id"] = d["user_id"]
        if "comment" in d:
            self.__dict__["comment"] = d["comment"]
        if "flag" in d:
            self.__dict__["flag"] = d["flag"]