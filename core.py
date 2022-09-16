import json
import sqlite3


class Core:

    def __init__(self, config):
        config = json.loads(open(config, 'r', encoding="utf-8-sig").read())
        self.use_db: bool = config["use-db"]
        if self.use_db is False:
            json_paths = config["json-path"].split("|")
            self.keywords: dict = json.loads(open(json_paths[0], 'r', encoding="utf-8-sig").read())
            self.replies: dict = json.loads(open(json_paths[1], 'r', encoding="utf-8-sig").read())
        else:
            self.db: str = config["db-path"]
        self.self_id: int = config["self_id"]
        self.self_nickname: str = config["self_nickname"]
        self.admins: list = config["admins"]

    def match_keyword(self, raw_message):
        match_word = None
        if self.use_db:
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()
            cursor.execute("select keyword from keywords;")
            r = cursor.fetchall()
            for i in r:
                if i in raw_message:
                    match_word = i
                    break
            cursor.execute('select class from keywords where keyword="%s"' % match_word)
            r = cursor.fetchall()
            if "&" in r:
                return r
            cursor.execute('select reply from replies where class=%s' % r)
            r = cursor.fetchall()
            return r
        else:
            for i in self.keywords:
                if i in raw_message:
                    match_word = i
                    break
            if not match_word:
                if raw_message == "?" or raw_message == "？":
                    return self.replies['4']
                else:
                    return None
            r = self.keywords[match_word]
            if "&" in r:
                return r
            r = self.replies[r]
            return r
