import sqlite3

#подключение к бд
def bd_start():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    return cursor, conn
    
def bd_close(conn):
    conn.close()

#функция добавления пользователя
def add_user(tg_id, elo):
    cursor, conn = bd_start()
    cursor.execute('INSERT INTO users (tg_id, elo) VALUES (?,?)', (tg_id, elo))
    conn.commit()
    bd_close(conn)
#TODO проверка на наличие пользователя в базе

#функция удаления пользователя
def del_user(tg_id):
    cursor, conn = bd_start()
    cursor.execute('DELETE FROM users WHERE tg_id = ?',(tg_id,) )
    conn.commit()
    bd_close(conn)

#функция изменения elo
def elo_change(tg_id,elo):
    cursor, conn = bd_start()
    cursor.execute('UPDATE users SET elo = ? WHERE tg_id = ?',(elo, tg_id) )
    conn.commit()
    bd_close(conn)

#функция вызова рейтинга
def leaderbords():
    cursor, conn = bd_start()
    leaders = cursor.execute('SELECT * from users ORDER BY elo DESC')
    for item in leaders.fetchall():
        print (f'{item[1]} {item[2]}')
    bd_close(conn)

try:
    #conn = sqlite3.connect("bd.db")
    #cursor = conn.cursor()
    #  подключение к БД
    #conn = sqlite3.connect("bd.db")
    # объект курсора для взаимодействия с бд
    #cursor = conn.cursor()

  
    #блок вызова функций удаления/добавления пользователя
    #TODO получать данные из вне
    #add_user('romka', 200)
    #del_user('tg_id')
    #elo_change('noi4eg7', 20)
    leaderbords()

    # запрос SELECT 
    # users = cursor.execute("SELECT * FROM 'users'")
    # метод fetchall() вовзаращет совпадания из SELECT 
    #print(users.fetchall())
    #bd_close()
except sqlite3.Error as error:
    print("Error", error)

#finally:
#    if(conn):
#        # отключиться от БД
#        conn.close()
