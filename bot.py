import telebot
import config
from telebot import types
import sqlite3 as sql
from app.models import db, Feedback
from application import app


bot = telebot.TeleBot(token='6646805556:AAFx2bCt9cXPx_TTWEoPTqotyxsO4Dakgh0')


def get_markup(UID):
    mk = types.InlineKeyboardMarkup(row_width=3)
    mk.add(
        types.InlineKeyboardButton('✔️', callback_data=f'accept_{UID}'),
        types.InlineKeyboardButton('❌', callback_data=f'decline_{UID}'),
    )
    return mk


def send_feedback(UID, user_name, photo, feedback):  # TODO
    photo_path = photo.split('\\')[-1]
    bot.send_photo(chat_id=str(config.ADMIN_ID),
                   photo=open(f'uploads/{photo_path}', 'rb'))
    bot.send_message(chat_id=str(config.ADMIN_ID),
                     text=f'Новый отзыв!\n'
                          f'<u>Имя:</u> {user_name}\n'
                          f'<u>Отзыв:</u> {feedback}\n',
                     parse_mode='HTML',
                     reply_markup=get_markup(UID))


def parse_updates():
    print('bot started')
    @bot.callback_query_handler(func=lambda call: 'accept' in call.data or 'decline' in call.data)
    def callback(call):
        print('callback found')
        if not int(call.message.chat.id) == int(config.ADMIN_ID):
            return
        UID = call.data.split('_')[1]
        if 'accept' in call.data:
            with app.app_context():
                with db.session.begin():
                    feedback_obj = db.session.get(Feedback, UID)
                    if feedback_obj:
                        name = feedback_obj.name
                        feedback = feedback_obj.feedback
                        try:
                            conn = sql.connect('instance/approved.db')
                            cursor = conn.cursor()
                            cursor.execute("INSERT INTO approved_feedbacks (name, feedback) VALUES (?, ?)", (name, feedback))
                            conn.commit()
                            conn.close()

                            db.session.delete(feedback_obj)
                        except:
                            print('connection to approved failed')
                    else:
                        print('feedback object have not found')


    bot.infinity_polling()
