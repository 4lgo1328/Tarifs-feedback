import telebot
import config
from telebot import types
import sqlite3 as sql

bot = telebot.TeleBot(token=config.TOKEN)


def get_markup(UID, name):
    mk = types.InlineKeyboardMarkup(
        types.InlineKeyboardButton(text='✔️', callback_data=f'accept_{UID}_{name}'),
        types.InlineKeyboardButton(text='❌', callback_data=f'decline_{UID}_{name}')
    )
    return mk


def send_feedback(UID, user_name, photo, feedback):  # TODO
    print(photo)
    bot.send_photo(config.ADMIN_ID,
                    photo=open(f'uploads/{photo}'),
                    caption=f'Новый отзыв!\n'
                          f'<u>Имя:</u> {user_name}\n'
                          f'<u>Отзыв:</u> {feedback}'
                          f'<u>Скриншот покупки</u> {photo}',
                    parse_mode='HTML',
                    reply_markup=get_markup(UID))

def parse_updates():
    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if not int(call.message.chat.id) == int(config.ADMIN_ID):
            return
        UID = call.data.split('_')[1]
        if 'accept' in call.data:
            conn = sql.connect('instance/site.db')
            cursor = conn.cursor()
            cursor.execute('SELECT (name, feedback) FROM feedback WHERE id = ?', UID)
            found = cursor.fetchone()
            name, feedback = found[0], found[1]
            conn.close()

            conn = sql.connect('instance/approved.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO approved_feedbacks (name, feedback) VALUES (?, ?)", (name, feedback))
            conn.commit()
            conn.close()
        conn = sql.connect('instance/site.db')
        query = "DELETE FROM feedback WHERE id = ?"
        conn.execute(query, UID)
        conn.close()

    bot.infinity_polling()
