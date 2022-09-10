from message_objects.messages import *
from message_objects.requests import *
from message_objects.notices import *
from message_objects.base_objects import Meta_Event, Base


def parsePost(p, core):
    post_type = p["post_type"]
    # meta_type
    if post_type == "meta_event":
        return Meta_Event(p)
    # message
    if post_type == "message":
        msg_type = p["message_type"]
        if msg_type == "private":
            return PrivateMessage(p, core)
        elif msg_type == "group":
            return GroupMessage(p)
    # request
    if post_type == "request":
        req_type = p["request_type"]
        if req_type == "friend":
            return FriendAddRequest(p)
        elif req_type == "group":
            return GroupJoinRequest(p)
    # notice
    if post_type == "notice":
        notice_type = p["notice_type"]
        if notice_type == "group_upload":
            return GroupFileNotice(p)
        elif notice_type == "group_admin":
            return GroupAdminNotice(p)
        elif notice_type == "group_decrease":
            return GroupDecreaseNotice(p)
        elif notice_type == "group_increase":
            return GroupIncreaseNotice(p)
        elif notice_type == "group_ban":
            return GroupBanNotice(p)
        elif notice_type == "friend_add":
            return FriendAddNotice(p)
        elif notice_type == "group_recall":
            return GroupRecallNotice(p)
        elif notice_type == "friend_recall":
            return FriendRecallNotice(p)
        elif notice_type == "notify":
            sub_type = p["sub_type"]
            if sub_type == "poke":
                if "group_id" in p:
                    return GroupPokeNotice(p)
                else:
                    return FriendPokeNotice(p)
            elif sub_type == "lucky_king":
                return GroupLuckyKingNotice(p)
            elif sub_type == "honor":
                return GroupHonorNotice(p)
        elif notice_type == "group_card":
            return GroupCardNotice(p)
        elif notice_type == "offline_file":
            return OfflineFileNotice(p)
        elif notice_type == "client_status":
            return ClientStatusNotice(p)
        elif notice_type == "essence":
            return EssenceNotice(p)
        else:
            return Base(p)


