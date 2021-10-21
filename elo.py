import crud
#расчет elo после матчей
#входные данные - игрок_1(tg_id), игрок_2(tg_id)  (в телеге должны быть реализация, 1. матч -> 2. я игрок_1 выиграл 3. кого выиграли)

#
#получить текущий ELO из BD
# 
def elo_change (winner, loser):
    #открываем базу
    cursor, conn = crud.bd_start()
    
    #блок расчета elo 
    elo_winner = cursor.execute('SELECT elo FROM users WHERE tg_id = ?',(winner,))
    elo_winner = elo_winner.fetchall()  
    Rw = elo_winner[0][0]

    elo_loser = cursor.execute('SELECT elo FROM users WHERE tg_id = ?',(loser,))
    elo_loser = elo_loser.fetchall()  
    Rl = elo_loser[0][0]
    
    Ew = 1/(1 + 10**((Rl-Rw)/400))
    El = 1/(1 + 10**((Rw-Rl)/400))

    Elo_change_winner = Rw + 16*(1-Ew)
    Elo_change_loser = Rl + 16*(0-El)
    
    #меняем elo в базе
    crud.elo_change(winner, int(Elo_change_winner))
    crud.elo_change(loser, int(Elo_change_loser))

    #закрываем базу
    crud.bd_close(conn)

#тестовый набор
#elo_change (262335305 ,  320362842)
pass  