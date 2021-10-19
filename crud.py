import sqlite3

#функция добавления пользователя
def add_user(tg_id, elo):
    cursor.execute('INSERT INTO users (tg_id, elo) VALUES (?,?)', (tg_id, elo))
    conn.commit()
#TODO проверка на наличие пользователя в базе

#функция удаления пользователя
def del_user(tg_id):
    cursor.execute('DELETE FROM users WHERE tg_id = ?',(tg_id,) )
    conn.commit()

#функция изменения elo
def elo_change(tg_id,elo):
    cursor.execute('UPDATE users SET elo = ? WHERE tg_id = ?',(elo, tg_id) )
    conn.commit()

#функция вызова рейтинга
def leaderbords():
    leaders = cursor.execute('SELECT * from users ORDER BY elo DESC')
    for item in leaders.fetchall():
        print (f'{item[1]} {item[2]}')

try:
    #  подключение к БД
    conn = sqlite3.connect("bd.db")
    # объект курсора для взаимодействия с бд
    cursor = conn.cursor()

  
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


  

except sqlite3.Error as error:
    print("Error", error)

finally:
    if(conn):
        # отключиться от БД
        conn.close()
