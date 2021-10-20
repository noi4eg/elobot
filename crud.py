import sqlite3


# подключение к бд
def bd_start():
    conn = sqlite3.connect("bd.db")
    cursor = conn.cursor()
    return cursor, conn


def bd_close(conn):
    conn.close()


# функция добавления пользователя
def add_user(tg_id, tg_full_name):
    cursor, conn = bd_start()
    check_user = cursor.execute('SELECT * FROM users WHERE tg_id = ?',(tg_id,))
    check_user = check_user.fetchall()
    elo = 200 #стартовый elo
    if check_user == []:
        cursor.execute('INSERT INTO users (tg_id, tg_name, elo) VALUES (?,?,?)', (tg_id, tg_full_name, elo))
        conn.commit()
        bd_close(conn)
        return True
    else:
        return False
    
    


# TODO проверка на наличие пользователя в базе

# функция удаления пользователя
def del_user(tg_id):
    cursor, conn = bd_start()
    cursor.execute('DELETE FROM users WHERE tg_id = ?', (tg_id,))
    conn.commit()
    bd_close(conn)


# функция изменения elo
def elo_change(tg_id, elo):
    cursor, conn = bd_start()
    cursor.execute('UPDATE users SET elo = ? WHERE tg_id = ?', (elo, tg_id))
    conn.commit()
    bd_close(conn)


# функция вызова рейтинга
def leaderbords():
    cursor, conn = bd_start()
    leaders = cursor.execute('SELECT * from users ORDER BY elo DESC')
    end_str = "{:<3} {:<20} {:<15}".format('№','Name','Value') +'\n'
    
    place = 1
    #print(leaders.fetchall())
    for item in leaders.fetchall():
        end_str += "{:<3} {:<20} {:<15}".format(str(place), item[3], str(item[2])) + '\n'
        place += 1

    #print (end_str)
    bd_close(conn)
    return end_str

def my_elo(tg_id):
    cursor, conn = bd_start()
    my_elo_end = cursor.execute('SELECT * FROM users WHERE tg_id = ?',(tg_id,))
    my_elo_end = my_elo_end.fetchall()
    bd_close(conn)
    return f'Хей, {my_elo_end[0][1]}, твой рейтинг = {my_elo_end[0][2]}'
try:
    # conn = sqlite3.connect("bd.db")
    # cursor = conn.cursor()
    #  подключение к БД
    # conn = sqlite3.connect("bd.db")
    # объект курсора для взаимодействия с бд
    # cursor = conn.cursor()

    # блок вызова функций удаления/добавления пользователя
    # TODO получать данные из вне
    #add_user('123123123','romka', 200)
    #del_user('320362842')
    # elo_change('noi4eg7', 20)
    #leaderbords()
    #my_elo('noi4eg7')
    pass
    # запрос SELECT 
    #users = cursor.execute("SELECT * FROM 'users'")
    # метод fetchall() вовзаращет совпадания из SELECT 
    #print(users.fetchall())
    # bd_close()
except sqlite3.Error as error:
    print("Error", error)

# finally:
#    if(conn):
#        # отключиться от БД
#        conn.close()
