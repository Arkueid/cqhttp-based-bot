import sqlite3

conn = sqlite3.connect('friendliness.db')
cursor = conn.cursor()
# conn.execute('insert into user_friendliness values(-1, 3327265384, 100);')
# conn.execute('update user_friendliness set friendliness=0 where user_id=3327565304;')
# conn.commit()
cursor.execute('select user_id from user_friendliness')
print(tuple(map(lambda x: x[0], cursor.fetchall())))
