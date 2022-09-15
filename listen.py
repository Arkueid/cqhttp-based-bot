from flask import Flask, request
from utils import parsePost
from core import Core


app = Flask("Aki-listen")
core = Core("data/config.json")


@app.route('/', methods=['post'])
def listen():
    post = request.get_json()
    result = parsePost(post, core)
    print(result.__class__)
    if result == "PrivateMessage" or result == "GroupMessage":
        result.reply()
    elif result == "GroupDecreaseNotice" or result == "GroupIncreaseNotice":
        result.react()
    elif result == "FriendPokeNotice" or result == "GroupPokeNotice":
        result.react()
    return ''


if __name__ == '__main__':
    app.run('127.0.0.1', 5701, debug=True)
