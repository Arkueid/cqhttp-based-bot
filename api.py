# 发送私聊消息
from urllib.parse import urljoin
import requests
import time
import urllib.request
import urllib.parse
import lxml.etree
from youdao import Youdao_Trans

authorized_groups = [
    826422163,
    970293394,
    962617351
]

youdao = Youdao_Trans()


def urlAt(node):
    return urljoin("http://127.0.0.1:5700", node)


def whatstoday() -> str:
    td_in_history = []
    query = {"wd": "历史上的今天"}
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "cookie": 'BIDUPSID=F195DC616116B330BFFEB19F592B9149; PSTM=1636172469; BD_UPN=12314753; __yjs_duid=1_1acb4ec39e49c5893cf11aeb226694bd1636173906228; BDUSS=TJPanVhVH5FV3JuVGVxUm5vY2FJbWt3aXdxdE9VdnFidlNEcFA2T2d2WGFTYTloRVFBQUFBJCQAAAAAAAAAAAEAAABvoPmGVGhlR3JhcGVmcnVpdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANq8h2HavIdhO; BDUSS_BFESS=TJPanVhVH5FV3JuVGVxUm5vY2FJbWt3aXdxdE9VdnFidlNEcFA2T2d2WGFTYTloRVFBQUFBJCQAAAAAAAAAAAEAAABvoPmGVGhlR3JhcGVmcnVpdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANq8h2HavIdhO; H_WISE_SIDS=107311_110085_127969_176399_179347_184716_189256_189659_191068_191242_192384_193246_194085_194530_195329_195343_195467_195757_196051_196427_196514_197242_197711_197958_198271_198930_199023_199082_199152_199466_199490_199579_199842_200150_200350_200744_200993_201054_201108_201233_201549_201553_201702_201970_201978_202297_202476_202563_202759_202848_202906_203172_203195_203316_203495_203519_203525_203543_203605_203629_204100_204113_204131_204155_204265_204431_204667_204816_204908_204966_205009_205218_205220_205238_205239; BAIDUID=C43AC3FA7408D87D73CEB4B0D20A490E:SL=0:NR=10:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=C43AC3FA7408D87D73CEB4B0D20A490E:SL=0:NR=10:FG=1; BA_HECTOR=a40004252l2g808k3d1h6ibku0r; channel=baidusearch; COOKIE_SESSION=34_1_5_5_17_13_0_2_5_5_8_2_33_0_5_0_1651117011_1651116976_1651117006|9#247292_53_1651116972|9; BD_HOME=1; H_PS_PSSID=36184_36309_31660_34813_35912_36165_34584_36339_35978_35802_36234_26350_36349_36311_36061; delPer=1; BD_CK_SAM=1; PSINO=1; sug=0; sugstore=0; ORIGIN=2; bdime=0; H_PS_645EC=ba9doKUMhcK643hMqAKtT6or8OH2E7+Zg3M8TnaqciK5bqzY/NJ6q3sbC4A; baikeVisitId=a62d9ad6-cc7e-43e8-8cd1-2b26fb2baff8; ab_sr=1.0.1_ZmU1ZGQwMTVmYWZmN2RhZGE1NjMzY2QwNjA2YjliYzJjM2Q5MDY3MTEyMTVhMzcwODczYTQ1NDg2MmEzYTMxZGE1OTY1MTQwZTg3MTUyNTg2NjI5NzkxMmU1MDMwYjcwMDVjMmRkZTMxZGJhMmUyY2RkMGRmMTlhNTIyN2FmYTFhMDg5NDIyMDMwNTA4ZGM0ODRmOGU0MjBiNGFjNDI5YjdhYmM2ZTJiOTk2MjI1ZThjYWUxMTIwZmFhNGIyZThh; RT="z=1&dm=baidu.com&si=pcbdyazod3&ss=l2ih1azg&sl=0&tt=0&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ul=26i&hd=28f"'
    }
    url = "https://www.baidu.com/s?" + urllib.parse.urlencode(query)
    req = urllib.request.Request(url, headers=headers)
    rsp = urllib.request.urlopen(req)
    tree = lxml.etree.HTML(rsp.read().decode())
    titles = tree.xpath('//p[@class="title_3qCGt"]/@title|//p[@class="title_3qCGt"]/text()')
    years = tree.xpath('//div[@class="year-tag_3Iqeg"]/text()')
    years = list(map(lambda x: x.replace('\n', '').replace(' ', ''), years))
    for i in titles:
        if i and '...' not in i:
            td_in_history.append(i)
    td_in_history = [*zip(years, td_in_history)]
    text = f'今天是{time.strftime("%Y.%m.%d", time.localtime(time.time()))}, 历史上的今天:'
    for year, title in td_in_history:
        text += '\n' + year + ' ' + title
    return text


def send_private_msg(user_id, group_id, message, auto_escape=False):
    params = {
        "user_id": user_id,
        "group_id": group_id,
        "message": message,
        "auto_escape": auto_escape,
    }
    rsp = requests.get(urlAt(send_private_msg.__name__), params=params)
    return


def send_group_msg(group_id, message, auto_escape=False):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "message": message,
        "auto_escape": auto_escape,
    }
    rsp = requests.get(urlAt(send_group_msg.__name__), params=params)
    return


def send_group_forward_msg(group_id, messages, ):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "messages": messages,
    }
    rsp = requests.get(urlAt(send_group_forward_msg.__name__), params=params)
    return


def send_msg(message_type, user_id, group_id, message, auto_escape=False):
    if group_id not in authorized_groups:
        return
    params = {
        "message_type": message_type,
        "user_id": user_id,
        "group_id": group_id,
        "message": message,
        "auto_escape": auto_escape,

    }
    rsp = requests.get(urlAt(send_msg.__name__), params=params)
    return


def delete_msg(message_id):
    params = {
        "message_id": message_id,
    }
    rsp = requests.get(urlAt(delete_msg.__name__), params=params)
    return


def get_msg(message_id):
    params = {
        "message_id": message_id,
    }
    rsp = requests.get(urlAt(get_msg.__name__), params=params)
    return


def get_forward_msg(message_id):
    params = {
        "message_id": message_id,
    }
    rsp = requests.get(urlAt(get_forward_msg.__name__), params=params)
    return


def get_image(file):
    params = {
        "file": file,
    }
    rsp = requests.get(urlAt(get_image.__name__), params=params)
    return


def mark_msg_as_read(file):
    params = {
        "file": file,
    }
    rsp = requests.get(urlAt(mark_msg_as_read.__name__), params=params)
    return


def set_group_kick(group_id, user_id, reject_add_request=False):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "user_id": user_id,
        "reject_add_request": reject_add_request,
    }
    rsp = requests.get(urlAt(set_group_kick.__name__), params=params)
    return


def set_group_ban(group_id, user_id, duration):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "user_id": user_id,
        "duration": duration,
    }
    rsp = requests.get(urlAt(set_group_ban.__name__), params=params)
    return


def set_group_anonymous_ban(group_id, anonymous, flag, duration):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "anonymous": anonymous,
        "flag": flag,
        "duration": duration,
    }
    rsp = requests.get(urlAt(set_group_anonymous_ban.__name__), params=params)
    return


def set_group_whole_ban(group_id, enable):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "enable": enable,
    }
    rsp = requests.get(urlAt(set_group_whole_ban.__name__), params=params)
    return


def set_group_admin(group_id, user_id, enable):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "user_id": user_id,
        "enable": enable,
    }
    rsp = requests.get(urlAt(set_group_admin.__name__), params=params)
    return


def set_group_anonymous(group_id, enable):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "enable": enable,
    }
    rsp = requests.get(urlAt(set_group_anonymous.__name__), params=params)
    return


def set_group_card(group_id, enable, card):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "enable": enable,
        "card": card
    }
    rsp = requests.get(urlAt(set_group_card.__name__), params=params)
    return


def set_group_name(group_id, group_name):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "group_name": group_name,
    }
    rsp = requests.get(urlAt(set_group_name.__name__), params=params)
    return


def set_group_leave(group_id, is_dismiss=False):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "is_dismiss": is_dismiss,
    }
    rsp = requests.get(urlAt(set_group_leave.__name__), params=params)
    return


def set_group_special_title(group_id, user_id, special_title, duration=-1):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
        "user_id": user_id,
        "special_title": special_title,
        "duration": duration,
    }
    rsp = requests.get(urlAt(set_group_special_title.__name__), params=params)
    return


def send_group_sign(group_id):
    if group_id not in authorized_groups:
        return
    params = {
        "group_id": group_id,
    }
    rsp = requests.get(urlAt(send_group_sign.__name__), params=params)
    return


def set_friend_add_request(flag, approve, remark):
    params = {
        "flag": flag,
        "approve": approve,
        "remark": remark,
    }
    rsp = requests.get(urlAt(set_friend_add_request.__name__), params=params)
    return


def set_group_add_request(flag, sub_type, approve, reason):
    params = {
        "flag": flag,
        "sub_type": sub_type,
        "approve": approve,
        "reason": reason,
    }
    rsp = requests.get(urlAt(set_group_add_request.__name__), params=params)
    return


def get_login_info(user_id, nickname):
    params = {
        "user_id": user_id,
        "nickname": nickname,
    }
    rsp = requests.get(urlAt(get_login_info.__name__), params=params)
    return


def set_qq_profile(nickname, company, email, college, personal_note):
    params = {
        "nickname": nickname,
        "company": company,
        "email": email,
        "college": college,
        "personal_note": personal_note,
    }
    rsp = requests.get(urlAt(set_qq_profile.__name__), params=params)
    return


def get_stranger_info(user_id, no_cache):
    params = {
        "user_id": user_id,
        "no_cache": no_cache,
    }
    rsp = requests.get(urlAt(get_stranger_info.__name__), params=params)
    return


def get_friend_list():
    params = {

    }
    rsp = requests.get(urlAt(get_friend_list.__name__), params=params)
    return


def get_unidirectional_friend_list():
    params = {
    }
    rsp = requests.get(urlAt(get_unidirectional_friend_list.__name__), params=params)
    return


def delete_friend(friend_id):
    params = {
        "friend_id": friend_id,
    }
    rsp = requests.get(urlAt(delete_friend.__name__), params=params)
    return


def get_group_info(group_id, no_cache):
    params = {
        "group_id": group_id,
        "no_cache": no_cache,
    }
    rsp = requests.get(urlAt(get_group_info.__name__), params=params)
    return


def get_group_list():
    params = {}
    rsp = requests.get(urlAt(get_group_list.__name__), params=params)
    return


def get_group_member_info(group_id, user_id, no_cache):
    params = {
        "group_id": group_id,
        "user_id": user_id,
        "no_cache": no_cache,
    }
    rsp = requests.get(urlAt(get_group_member_info.__name__), params=params)
    return


def get_group_member_list(group_id, no_cache=False):
    params = {
        "group_id": group_id,
        "no_cache": no_cache,
    }
    rsp = requests.get(urlAt(get_group_member_list.__name__), params=params)
    return rsp.json()


def get_group_honor_info(group_id, _type):
    params = {
        "group_id": group_id,
        "type": _type,
    }
    rsp = requests.get(urlAt(get_group_honor_info.__name__), params=params)
    return


def set_essence_msg(message_id):
    params = {
        "message_id": message_id
    }
    rsp = requests.get(urlAt(set_essence_msg.__name__), params=params)
    return


def delete_essence_msg(message_id):
    params = {
        "message_id": message_id
    }
    rsp = requests.get(urlAt(delete_essence_msg.__name__), params=params)
    return


def delete_unidirectional_friend(user_id):
    params = {
        "user_id": user_id
    }
    rsp = requests.get(urlAt(delete_unidirectional_friend.__name__), params=params)
    return


def send_private_forward_msg(user_id, messages):
    params = {
        "user_id": user_id,
        "messages": messages
    }
    rsp = requests.get(urlAt(send_private_forward_msg.__name__), params=params)
    return


if __name__ == '__main__':
    x = whatstoday()
    print(x)
