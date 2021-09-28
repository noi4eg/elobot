import sqlite3
from sqlite3.dbapi2 import Cursor


try:
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (tg_id, elo) VALUES (?,?)", ('noi4eg',200))

    users = cursor.execute("SELECT * FROM 'users'")
    print(users.fetchall())

    conn.commit()

except sqlite3.Error as error:
    print("Error", error)

finally:
    if(conn):
        conn.close()
