from flask import Flask, request
from utils import parsePost
from core import Core
from api import authorized_groups


app = Flask("Aki-listen")
core = Core("data/config.json")

authorized_groups.extend(core.config['authorized-groups'])


@app.route('/', methods=['post'])
def listen():
    post = request.get_json()
    result = parsePost(post, core)
    print(result.__class__)
    if result == "PrivateMessage" or result == "GroupMessage":
        result.reply()
    elif result == "GroupDecreaseNotice" or result == "GroupIncreaseNotice":
        result.react()
    elif result == "FriendPokeNotice" \
            or result == "GroupRecallNotice" \
            or result == "GroupPokeNotice":
        print(post)
        result.react()
    return ''


if __name__ == '__main__':
    app.run('127.0.0.1', 5701, debug=True)
