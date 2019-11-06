import json

def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }

keyboard = {
    "one_time": False,
    "buttons": [
        [get_button(label="Возможности", color="primary"), get_button(label="Ваши предложения", color="positive")]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))
#=====================================================#

keyboard_vozmojn = {
    "one_time": False,
    "buttons": [
        [get_button(label="Новогоднее поздравление", color="primary"), get_button(label="Ваши предложения", color="positive")],
        [get_button(label="Игра", color="primary")]
    ]
}

keyboard_vozmojn = json.dumps(keyboard_vozmojn, ensure_ascii=False).encode('utf-8')
keyboard_vozmojn = str(keyboard_vozmojn.decode('utf-8'))
#=====================================================#

keyboard_pozdravlenie_part1 = {
    "one_time": False,
    "buttons": [
        [get_button(label="Записать поздравление", color="primary")]
    ]
}

keyboard_pozdravlenie_part1 = json.dumps(keyboard_pozdravlenie_part1, ensure_ascii=False).encode('utf-8')
keyboard_pozdravlenie_part1 = str(keyboard_pozdravlenie_part1.decode('utf-8'))
#=====================================================#

keyboard_pozdravlenie_part2 = {
    "one_time": False,
    "buttons": [
        [get_button(label="@Читать", color="primary"),get_button(label="@Рисовать", color="primary")],
        [get_button(label="@Гулять", color="primary"),get_button(label="@Смотреть мультики", color="primary")],
        [get_button(label="@Заниматься спортом", color="primary"),get_button(label="@Есть сладости", color="primary")],
        [get_button(label="@Петь", color="primary"),get_button(label="@Заниматься музыкой", color="primary")],
        [get_button(label="@Играть\n в игры", color="primary"),get_button(label="@Танцевать", color="primary")],
        [get_button(label="В меню", color="positive")]

    ]
}

keyboard_pozdravlenie_part2 = json.dumps(keyboard_pozdravlenie_part2, ensure_ascii=False).encode('utf-8')
keyboard_pozdravlenie_part2 = str(keyboard_pozdravlenie_part2.decode('utf-8'))
#=====================================================#

keyboard_game = {
    "one_time": False,
    "buttons": [
        [get_button(label="Клик", color="positive"), get_button(label="Магазин улучшений", color="primary")],
        [get_button(label="Топ", color="negative"), get_button(label="Аккаунт", color="primary")]
    ]
}

keyboard_game = json.dumps(keyboard_game, ensure_ascii=False).encode('utf-8')
keyboard_game = str(keyboard_game.decode('utf-8'))

#=====================================================#

keyboard_shop = {
    "one_time": False,
    "buttons": [
        [get_button(label="Золотой клик", color="positive"), get_button(label="Вернуться", color="negative")],
        [get_button(label="Улучшить ранг", color="positive")]
    ]
}

keyboard_shop = json.dumps(keyboard_shop, ensure_ascii=False).encode('utf-8')
keyboard_shop = str(keyboard_shop.decode('utf-8'))

#=====================================================#

keyboard_shop_click = {
    "one_time": False,
    "buttons": [
        [get_button(label="Купить золотой клик", color="positive"), get_button(label="Вернуться", color="negative")]
    ]
}

keyboard_shop_click = json.dumps(keyboard_shop_click, ensure_ascii=False).encode('utf-8')
keyboard_shop_click = str(keyboard_shop_click.decode('utf-8'))

#=====================================================#

keyboard_shop_rank = {
    "one_time": False,
    "buttons": [
        [get_button(label="Купить ранг", color="positive"), get_button(label="Вернуться", color="negative")]
    ]
}

keyboard_shop_rank = json.dumps(keyboard_shop_rank, ensure_ascii=False).encode('utf-8')
keyboard_shop_rank = str(keyboard_shop_rank.decode('utf-8'))

#=====================================================#

keyboard_status = {
    "one_time": False,
    "buttons": [
        [get_button(label="Купить статус", color="positive"), get_button(label="Вернуться", color="negative")]
    ]
}

keyboard_status = json.dumps(keyboard_status, ensure_ascii=False).encode('utf-8')
keyboard_status = str(keyboard_status.decode('utf-8'))

#=====================================================#

keyboard_status_buy = {
    "one_time": False,
    "buttons": [
        [get_button(label="Приобрести", color="positive"), get_button(label="Вернуться", color="negative")]
    ]
}

keyboard_status_buy = json.dumps(keyboard_status_buy, ensure_ascii=False).encode('utf-8')
keyboard_status_buy = str(keyboard_status_buy.decode('utf-8'))