import sqlite3

with sqlite3.connect('new.db') as db:
    cursor = db.cursor()
    if db:
        print('База данных подключена нормально !')
    query1 = """ INSERT INTO guys (id , name) VALUES(1, 'Миша') """
    query2 = """ INSERT INTO guys (id , name) VALUES(2, 'Андрей') """
    query3 = """ INSERT INTO guys (id , name) VALUES(3, 'Иван') """
    query4 = """ INSERT INTO guys (id , name) VALUES(4, 'Илья') """
    query5 = """ INSERT INTO guys (id , name) VALUES(5, 'Максим') """
    query6 = """ INSERT INTO guys (id , name) VALUES(6, 'Дмитрий') """
    query7 = """ INSERT INTO guys (id , name) VALUES(7, 'Евгений') """
    query8 = """ INSERT INTO guys (id , name) VALUES(8, 'Олег') """
    # cursor.execute(query1)
    # cursor.execute(query2)
    # cursor.execute(query3)
    # cursor.execute(query4)
    # cursor.execute(query5)
    # cursor.execute(query6)
    # cursor.execute(query7)
    # cursor.execute(query8)
    db.commit()

with sqlite3.connect('new.db') as db:
    cursor = db.cursor()
    query = """ SELECT cash, name FROM moneys JOIN guys 
                ON guys.id = moneys.link_id WHERE link_id = 1 """
    cursor.execute(query)
    sum = 0
    for result in cursor:
        sum += result[0]
        print(result[0], result[1])
    print('Всего :', sum)
