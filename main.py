import telebot
import sqlite3
import buttons

bot = telebot.TeleBot('6693828674:AAF7mUV_xqnROXlFvP95-tRSMidAKkpD4nk')
name = None


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    conn = sqlite3.connect('telegram-bot.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, pass INTEGER);')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(user_id, 'Привет пройдите регистрацию что-бы пользоватся ботом.ВВЕДИТЕ СВОЕ ИМЯ')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    user_id = message.from_user.id
    name = message.text.strip()
    bot.send_message(user_id, 'Придумайте пароль(только цыфры)')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    user_id = message.from_user.id
    password = message.text.strip()
    conn = sqlite3.connect('telegram-bot.sql')
    cur = conn.cursor()
    cur.execute('INSERT INTO users(name,pass) VALUES ("%s","%s")' % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(user_id, 'Пользователь зарегестрирован!\nВведите коды для получения кодов')
    bot.register_next_step_handler(message, main)

def main(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Виберите пункт", reply_markup=buttons.buttons_boss())
    bot.register_next_step_handler(message, if_buttons1)


def if_buttons1(message):
    user_id = message.from_user.id
    text = message.text.strip()
    if text == 'КОДЫ НА ПИТОНЕ(Т-Г БОТЫ)':
        bot.send_message(user_id, 'ВОТ ВАМ КОДЫ НА ПИТОНЕ', reply_markup=buttons.main_buttons())
        bot.register_next_step_handler(message, if_buttons2)
    elif text == 'КОДЫ НА FRONTEND(HTML)':
        bot.send_message(user_id, 'ВОТ ВАМ КОДЫ FRONTEND(HTML)', reply_markup=buttons.main_buttons1())
        bot.register_next_step_handler(message, if_buttons3)


def if_buttons2(message):
    user_id = message.from_user.id
    text = message.text.strip()
    if text == 'КОД НА ПИТОНЕ(БОТ КОНВЕРТОР ВАЛЮТ)':
        bot.send_message(user_id, 'GITHUB:-:')
    elif text == 'КОД НА ПИТОНЕ(БОТ ВИКИПЕДИЯ)':
        bot.send_message(user_id, 'GITHUB:-:')


def if_buttons3(message):
    user_id = message.from_user.id
    text = message.text.strip()
    if text == 'Код на html похвастаться':
        bot.send_message(user_id, 'GITHUB:-:')
    elif text == 'Код на html для магазина':
        bot.send_message(user_id, 'GITHUB:-:')


bot.polling(none_stop=True)
