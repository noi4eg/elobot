import sqlite3
#что-нибудь
try:
    #  подключение к БД
    conn = sqlite3.connect("bd.db")
    # объект курсора для взаимодействия с бд
    cursor = conn.cursor()

    #  выполнение запроса INSERT
    #  TODO закомментить инсерт
    #  cursor.execute("INSERT OR IGNORE INTO users (tg_id, elo) VALUES (?,?)", ('noi4eg7',200))
    
    # запрос SELECT 
    users = cursor.execute("SELECT * FROM 'users'")
    # метод fetchall() вовзаращет совпадания из SELECT 
    print(users.fetchall())

    # Сохранить изменения, в этом случае INSERT
    conn.commit()

except sqlite3.Error as error:
    print("Error", error)

finally:
    if(conn):
        # отключиться от БД
        conn.close()
