import telebot
import config
from telebot import types
import sqlite3 as sql
from app.models import db, Feedback
from application import app
import time

bot = telebot.TeleBot(token='6646805556:AAF4nxZjSV6yMrg8zrUNliX_XgxSPTcJoHI')


def get_markup(UID):
    mk = types.InlineKeyboardMarkup(row_width=3)
    mk.add(
        types.InlineKeyboardButton('✔️', callback_data=f'accept_{UID}'),
        types.InlineKeyboardButton('❌', callback_data=f'decline_{UID}'),
    )
    return mk


def send_feedback(UID, user_name, photo, feedback):
    photo_path = photo.split('\\')[-1]
    bot.send_photo(chat_id=str(config.ADMIN_ID),
                   photo=open(f'static/uploads/{photo_path}', 'rb'), # TODO REMOVE UPLOADS
                   caption=f'Новый отзыв!\n'
                           f'<u>Имя:</u> {user_name}\n'
                           f'<u>Отзыв:</u> {feedback}\n',
                   reply_markup=get_markup(UID))


def get_feedback(UID):
    time.sleep(0.5)
    with sql.connect(config.SITE_PATH, uri=True) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, feedback, photo FROM feedback WHERE id = ?", (UID,))
        row = cursor.fetchone()
        if row:
            name, feedback, photo = row
            return name, feedback, photo
        else:
            return None, None, None


def parse_updates():
    @bot.callback_query_handler(func=lambda call: 'accept' in call.data or 'decline' in call.data)
    def callback(call):

        if not int(call.message.chat.id) == int(config.ADMIN_ID):
            return

        UID = call.data.split('_')[1]
        if 'accept' in call.data:
            name, feedback, photo_url = get_feedback(UID)
            try:
                conn = sql.connect(config.APPROVED_PATH)
                cursor = conn.cursor()
                cursor.execute("INSERT INTO approved_feedbacks (name, feedback, photo_url) VALUES (?, ?, ?)",
                               (name, feedback, photo_url))
                conn.commit()
                conn.close()
                bot.send_message(chat_id=call.message.chat.id,
                                 text='Отзыв успешно добавлен в базу!')
            except Exception as e:
                bot.send_message(chat_id=call.message.chat.id,
                                 text=f'Связь с базой "Подтвержденные" не установлена. \n'
                                      f'Свяжитесь с @algo1328 для устранения проблемы. \n'
                                      f'Ошибка: {str(e)}')
        else:
            bot.send_message(chat_id=call.message.chat.id,
                             text='Отзыв отклонен!')

    bot.infinity_polling()


if __name__ == "__main__":
    parse_updates()
