import sqlite3
import pandas as pd


def init_db():
    # 不存在就创建
    conn = sqlite3.connect("rule.db")
    try:
        sql1 = "create table keywords(" \
               "id integer primary key autoincrement not null," \
               "keyword text unique not null," \
               "class int not null);"
        conn.execute(sql1)
        sql2 = "create table replies(" \
               "id integer primary key autoincrement not null," \
               "class int unique not null," \
               "reply text unique not null);"
        conn.execute(sql2)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


class Database:

    def __init__(self):
        self.conn = None

    def connect(self, db):
        self.conn = sqlite3.connect(db)

    def print_table(self, table_name):
        df = pd.read_sql("select * from %s;" % table_name, con=self.conn, index_col="id")
        print(df)

    def addTo(self, sequence, table_name):
        df = pd.read_sql("select * from %s" % table_name, con=self.conn, index_col="id")
        next_idx = df.index.max() + 1
        df.loc[next_idx] = sequence
        df.to_sql("keywords", self.conn, if_exists="replace")

    def __del__(self):
        if self.conn:
            self.conn.close()


if __name__ == '__main__':
    init_db()
