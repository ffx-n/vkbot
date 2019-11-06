import vk_api
import time
import os
import random
import sqlite3
import json
import requests
from keyboards import *
from db import *
from shop import *
headers = {'accept':'*/*',
           'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

token = os.environ.get('token')

vk = vk_api.VkApi(token=token)
vk._auth_token()
ranks = ['Новичок ☕', 'Любитель ①', 'Опытный Кликер ②', 'Профессиональный Кликер③', 'Мастер ⋆', 'Гранд-Мастер ⋆⋆⋆', 'Величайший Кликер ㉨㉨㉨', 'Элита ╰☆╮']
name = ''
eng = ''
interests = ''

def send_message(id,message,keyboard):
    vk.method("messages.send", {"peer_id": id, "keyboard": keyboard, "message": message, "random_id": random.randint(1, 2147483647)})

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

def enter_status(id_f):
    send_message(id_f,'Введи статус, который хочешь установить и отправь его мне!','0')
    while True:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        print(name)
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if id == id_f :
                cursor.execute(f"""UPDATE users
                                    SET status = '{body[0:39]}'
                                    WHERE uid = {id_f}
                                """)
                send_message(id_f, 'Статус установлен', keyboard_game)
                break


def christmas(id_f):
    global eng, interests, name
    vk.method("messages.send",{"peer_id": id_f, "message": "Отправь нам имя того, кого будем поздравлять! \n\nВАЖНО! Поставь перед именем восклицательный знак\n\nНапример: !Артем", "random_id": random.randint(1, 2147483647)})
    while True:
        allow = False
        year = 0
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        print(name)
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == 'в меню':
                vk.method("messages.send", {"peer_id": id_f,"keyboard": keyboard, "message": "Теперь вы в меню!","random_id": random.randint(1, 2147483647)})
                break
            if id == id_f and body[0] == '!':
                name = body[1:len(body)]
                print(name)
                vk.method("messages.send", {"peer_id": id_f,"keyboard" : keyboard_pozdravlenie_part2, "message": "Имя записано. Выбери увлечение ребенка!","random_id": random.randint(1, 2147483647)})
            if id == id_f and body[0] == '@':
                interests = body[1:len(body)]
                print(interests)
                vk.method("messages.send", {"peer_id": id_f, "message": "Записали. Теперь отправь нам возраст ребенка","random_id": random.randint(1, 2147483647)})
            if id == id_f and len(body)<=2:
                year = int(body)
                print(year)
                allow = True
            if id == id_f and allow == True:
                if interests.lower() == 'читать':
                    eng = 'reading'
                elif interests.lower() == 'рисовать':
                    eng = 'painting'
                elif interests.lower() == 'гулять':
                    eng = 'walking'
                elif interests.lower() == 'заниматься спортом':
                    eng = 'sport'
                elif interests.lower() == 'смотреть мультики':
                    eng = 'cartoons'
                elif interests.lower() == 'есть сладости':
                    eng = 'sweets'
                elif interests.lower() == 'петь':
                    eng = 'singing'
                elif interests.lower() == 'заниматься музыкой':
                    eng = 'music'
                elif interests.lower() == 'играть в игры':
                    eng = 'games'
                elif interests.lower() == 'танцевать':
                    eng = 'dancing'
                url = f'https://newyear.mail.ru/?name={name}&hobby={eng}&age={year}'
                print(f'First url = {url}')
                params = {'json':'true',
                          'url':url}
                data = requests.get(f'https://clck.ru/--?', params=params)
                print(data.json())
                short_url = data.json()[0]
                vk.method("messages.send", {"peer_id": id_f, "message": f"Ваше поздравление готово! Откройте и обрадуйте вашего ребенка! \n\n{short_url}","random_id": random.randint(1, 2147483647)})
                vk.method("messages.send", {"peer_id": id_f,"keyboard":keyboard, "message": f"Cпасибо за то, что используете нашу группу! Не забудьте поделиться с друзьями!","random_id": random.randint(1, 2147483647)})
                break



# У кнопок может быть один из 4 цветов:
# 1. primary — синяя кнопка, обозначает основное действие. #5181B8
# 2. default — обычная белая кнопка. #FFFFFF
# 3. negative — опасное действие, или отрицательное действие (отклонить, удалить и тд). #E64646
# 4. positive — согласиться, подтвердить. #4BB34B
message_ded = 'Наша группа сделала новогоднее чудо, доступное каждому.\nНапишите имя ребёнка или близкого человека, которого хотите поздравить, и выберите его увлечение.\nМы передадим это Дедушке Морозу, и через несколько секунд вы получите видеоролик с именным поздравлением.\nДобрый волшебник лично обратится к ребёнку с экрана компьютера и поздравит его с наступающим Новым годом.'
while True:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages ["items"][0]["last_message"]["text"]
            if body.lower() == "возможности":
                send_message(id,'Выбирай',keyboard_vozmojn)
            elif body.lower() == "начать":
                send_message(id,'Вот и они', keyboard)
            elif body.lower() == "новогоднее поздравление":
                send_message(id, message_ded, keyboard_pozdravlenie_part1)
            elif body.lower() == "записать поздравление":
                christmas(id)
            elif body.lower() == "игра":
                send_message(id,'Вы зарегестрированны!', keyboard_game)
                add_new_user(id)
            elif body.lower() == "аккаунт":
                information = get_info_account(id)
                send_message(id, f'{information} ', keyboard_status)
            elif body.lower() == "клик":
                click(id)
                information = get_clicked(id)
                send_message(id, f' Успешно! Ваш баланс: {information} ', '0')
            elif body.lower() == "топ":
                response = top_users()
                print(response)
                send_message(id, response, '0')
            elif body.lower() == "магазин улучшений":
                send_message(id, 'Добро пожаловать!', keyboard_shop)
            elif body.lower() == "золотой клик":
                price = get_price(id)
                send_message(id, price, keyboard_shop_click)
            elif body.lower() == "купить золотой клик":
                a = buy_click(id)
                if a =='success':
                    send_message(id, 'Успешно', keyboard_game)
                else:
                    send_message(id, 'Недостаточно денег', keyboard_game)
            elif body.lower() == "вернуться":
                send_message(id,'Успешно', keyboard_game)
            elif body.lower() == "улучшить ранг":
                price = get_price_rank(id)
                send_message(id,price, keyboard_shop_rank)
            elif body.lower() == "купить ранг":
                a = buy_rank(id)
                if a == 'success':
                    send_message(id, 'Успешно', keyboard_game)
                else:
                    send_message(id, 'Недостаточно денег или у вас максимальный ранг', keyboard_game)
            elif body.lower() == "купить статус":
                send_message(id,'Цена статуса: 500. Маскимальная длина статуса 40 символов', keyboard_status_buy)
            elif body.lower() == "приобрести":
                a = buy_status(id)
                if a =='success':
                    enter_status(id)
        pass
