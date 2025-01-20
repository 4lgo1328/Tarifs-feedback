import telebot
import config
from telebot import types

bot = telebot.TeleBot(token=config.TOKEN)


def get_markup(UID):
    mk = types.InlineKeyboardMarkup(
        types.InlineKeyboardButton(text='✔️', callback_data=f'accept_{UID}'),
        types.InlineKeyboardButton(text='❌', callback_data=f'decline_{UID}')
    )
    return mk


def send_feedback(UID, user_name, photo, feedback): # TODO
    bot.send_message(config.ADMIN_ID,
                     text=f'Новый отзыв!\n'
                          f'<u>Имя:</u> {user_name}\n'
                          f'<u>Отзыв:</u> {feedback}'
                          f'<u>Скриншот покупки</u> {photo}',
                     parse_mode='HTML',
                     reply_markup=get_markup(UID))


def parse_updates():
    @bot.callback_query_handler()

    bot.infinity_polling()