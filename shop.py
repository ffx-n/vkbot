import sqlite3

from db import *
ranks = ['Новичок ☕', 'Любитель ①', 'Опытный Кликер ②', 'Профессиональный Кликер③', 'Мастер ⋆', 'Гранд-Мастер ⋆⋆⋆', 'Величайший Кликер ㉨㉨㉨', 'Элита ╰☆╮']

def get_price(id):
    sql = f"SELECT * FROM users WHERE uid={id}"
    cursor.execute(sql)
    info = cursor.fetchone()
    price = int(info[4])
    price_text = f'Цена улучшения: {price}'
    return price_text

def buy_click(id):
    sql = f"SELECT * FROM users WHERE uid={id}"
    cursor.execute(sql)
    info = cursor.fetchone()
    print(info)
    if int(info[1])>int(info[4]):
        cursor.execute(f"""
        UPDATE users 
        SET money = money - {info[4]},
            click_price = click_price*2,
            per_click = per_click + 1
        WHERE uid={id}
                """)
        return 'success'
    else:
        return 'none'

def get_price_rank(id):
    sql = f"SELECT * FROM users WHERE uid={id}"
    cursor.execute(sql)
    info = cursor.fetchone()
    rank = int(info[3])
    price = rank * 300 * 2
    if rank == 0:
        price = 250
    price_text = f'Цена улучшения: {price}'
    return price_text

def buy_rank(id):
    sql = f"SELECT * FROM users WHERE uid={id}"
    cursor.execute(sql)
    info = cursor.fetchone()
    print(len(ranks)-1)
    rank = int(info[3])
    print(rank)
    rank_price = rank*300*2
    if rank == 0:
        rank_price = 250
    if int(info[1])>rank_price and rank < len(ranks)-1:
        cursor.execute(f"""
        UPDATE users 
        SET money = money - {rank_price},
            rank = rank +1,
            per_click = per_click +4
        WHERE uid={id}
                """)

        return 'success'
    else:
        return 'none'


def buy_status(id):
    sql = f"SELECT * FROM users WHERE uid={id}"
    cursor.execute(sql)
    info = cursor.fetchone()
    print(info)
    if int(info[1]) > 500:
        cursor.execute(f"""
            UPDATE users 
            SET money = money - 500  
            WHERE uid={id}
                    """)
        return 'success'
    else:
        return 'none'
#get_price('142901911')