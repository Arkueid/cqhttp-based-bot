import sqlite3
import pandas as pd


def create_user_assets_table():
    conn = sqlite3.connect('data.db')
    try:
        conn.execute('create table user_assets('
                     'id integer primary key autoincrement,'
                     'user_id int unique not null,'
                     'friendliness int not null default 50,'
                     'money decimal not null default 0,'
                     'last_sign datetime default "2022-03-07 00:00:00",'
                     'jrrp int default 100,'
                     'last_jrrp date default "2022-03-07 00:00:00");')
    except sqlite3.OperationalError:
        pass
    print(pd.read_sql('select * from user_assets', conn))
    conn.close()


def create_keywords_table():
    conn = sqlite3.connect('data.db')
    try:
        conn.execute('create table keywords('
                     'id integer primary key autoincrement not null,'
                     'keyword text unique not null,'
                     'reply_id int not null);')
    except sqlite3.OperationalError as e:
        pass
    print(pd.read_sql('select keyword from keywords;', conn))
    conn.close()


def create_replies_table():
    conn = sqlite3.connect('data.db')
    try:
        conn.execute('create table replies('
                     'id integer primary key autoincrement not null,'
                     'reply text unique not null);')
    except sqlite3.OperationalError as e:
        pass
    print(pd.read_sql('select * from replies;', conn, index_col='id'))
    conn.close()


def init():
    create_user_assets_table()
    create_keywords_table()
    create_replies_table()


def db_to_excel():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('select name from sqlite_master where type="table"')
    ew = pd.ExcelWriter('data.xlsx')
    for i in cursor.fetchall():
        if i != "sqlite_sequence":
            pd.read_sql('select * from %s' % i[0], conn).to_excel(ew, sheet_name=i[0], index=False)
    ew.save()


def excel_to_db():
    conn = sqlite3.connect('data.db')
    df = pd.read_excel('data.xlsx', sheet_name=None)
    for i in df.keys():
        curr = df[i]
        for j in curr.to_numpy():
            s = map(lambda x: f'"{x}"' if type(x) == pd._libs.tslibs.timestamps.Timestamp or type(x) == str else str(x), j)
            conn.execute(f'insert into {i} values({",".join(s)})')
    conn.commit()


init()
# db_to_excel()
excel_to_db()
