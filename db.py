import sqlite3
ranks = ['Новичок ☕', 'Любитель ①', 'Опытный Кликер ②', 'Профессиональный Кликер③', 'Мастер ⋆', 'Гранд-Мастер ⋆⋆⋆', 'Величайший Кликер ㉨㉨㉨', 'Элита ╰☆╮']

conn = sqlite3.connect("bot_db.db")
cursor = conn.cursor()
n=1 #Для вывода топ игроков
#колонны - per_click, click_price, rank, status
# Создание таблицы
'''
cursor.execute("""CREATE TABLE users
                  (uid text, money integer)
                """)
cursor.execute("""ALTER TABLE users ADD COLUMN per_click integer 
                """) # добавил новый table к users
'''
def update(id):
    sql = f"""
        UPDATE users
        SET money = 153
        WHERE uid = 555555
        """
    cursor.execute(sql)
    conn.commit()

def sort_col(i): # для вывода топ игроков
    return i[n]

def top_users():
    numbers = []
    sql = f"SELECT * FROM users "
    cursor.execute(sql)
    info = cursor.fetchall()
    for i in range(0,len(info)):
        numbers.append(info[i][0:6])
    numbers.sort(key=sort_col, reverse=True)
    print(numbers)
    top10 = ''
    for i in range(0, len(numbers)):
        status = numbers[i][5]
        rank_index = int(numbers[i][3])
        top10+=f'{i+1}. @id{numbers[i][0]}, Баланс: {numbers[i][1]} | Ранг: {ranks[rank_index]} | Личный статус: {status}\n'
    return top10


def add_new_user(uid):
    sql = f"SELECT * FROM users WHERE uid={uid}"
    cursor.execute(sql)
    count = cursor.fetchall()
    if len(count) == 0:
        users = [(uid, 5, 1, '0', 150)]
        cursor.executemany("INSERT INTO users VALUES ( ?,?,?,?,? )", users)
        conn.commit()

def get_clicked(id):
    sql = f"SELECT * FROM users WHERE uid={id}"
    cursor.execute(sql)
    info = cursor.fetchone()
    print(info)
    balance = info[1]
    return balance

def get_info_account(id):
    sql = f"SELECT * FROM users WHERE uid={id}"
    cursor.execute(sql)
    info = cursor.fetchone()
    print(info)
    status = info[5]
    per_click = info[2]
    balance = info[1]
    rank = int(info[3])
    information = f'Ваш баланс:{balance} | Очки за клик:{per_click} | Ранг: {ranks[rank]}\n\n Личный статус: {status}'
    return information

def click(id):
    sql = f"""
    UPDATE users 
    SET money = money + per_click
    WHERE uid={id}
    """
    cursor.execute(sql)
    conn.commit()
sql = "SELECT * FROM users"
cursor.execute(sql)
print(cursor.fetchall())
#print(get_info_account('142901911'))