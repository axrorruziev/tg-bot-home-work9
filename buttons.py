from telebot import types


def buttons_boss():
    buttons = types.ReplyKeyboardMarkup(row_width=2)

    btn1 = types.KeyboardButton('КОДЫ НА ПИТОНЕ(Т-Г БОТЫ)')
    btn2 = types.KeyboardButton('КОДЫ НА FRONTEND(HTML)')
    buttons.add(btn1, btn2)
    return buttons


def main_buttons():
    buttons = types.ReplyKeyboardMarkup(row_width=2)

    btn1 = types.KeyboardButton('КОД НА ПИТОНЕ(БОТ КОНВЕРТОР ВАЛЮТ)')
    btn2 = types.KeyboardButton('КОД НА ПИТОНЕ(БОТ ВИКИПЕДИЯ)')
    buttons.add(btn1, btn2)
    return buttons


def main_buttons1():
    buttons = types.ReplyKeyboardMarkup(row_width=2)

    btn1 = types.KeyboardButton('Код на html похвастаться')
    btn2 = types.KeyboardButton('Код на html для магазина')
    buttons.add(btn1, btn2)
    return buttons
