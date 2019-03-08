# Telegram-бот погоды.
# Дата: 23.02.2017
# -*- coding: utf8 -*-

import telebot
import constants
import random
bot = telebot.TeleBot(constants.TOKEN)

print(bot.get_me())

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)

    user_markup.row('Прайс-лист')
    user_markup.row('Вакансии', 'FAQ')
    user_markup.row('Выход')

    bot.send_chat_action(message.from_user.id, 'upload_photo')
    bot.send_photo(message.from_user.id, constants.LOGO, constants.WELCOME_TEXT)
    bot.send_message(message.from_user.id, constants.DESCRIPTION, reply_markup=user_markup, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    QIWI = '*+7-964-561-36-25*'
    RAND = random.randint(11111, 99999)
    RANDOM = str(RAND)

    if message.text == 'СТАРТ':
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Прайс-лист')
        user_markup.row('Вакансии', 'FAQ')
        user_markup.row('Выход')
        bot.send_photo(message.from_user.id, constants.LOGO, constants.WELCOME_TEXT, reply_markup=user_markup)
    if message.text == 'Прайс-лист':
        user_markup2 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup2.row('Вернуться')
        user_markup2.row('Москва', 'Санкт-Петербург')
        user_markup2.row('Белгород', 'Владивосток')
        user_markup2.row('Воронеж', 'Екатеринбург')
        user_markup2.row('Ижевск', 'Казань')
        user_markup2.row('Самара', 'Воронеж')
        user_markup2.row('Омск', 'Новосибирск')
        user_markup2.row('Рязань')
        user_markup2.row('Вернуться')
        bot.send_message(message.from_user.id, 'Выберите город.', reply_markup=user_markup2)

    if message.text == 'Вeрнуться':
        user_markup2 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup2.row('Вернуться')
        user_markup2.row('Москва', 'Санкт-Петербург')
        user_markup2.row('Белгород', 'Владивосток')
        user_markup2.row('Воронеж', 'Екатеринбург')
        user_markup2.row('Ижевск', 'Казань')
        user_markup2.row('Самара', 'Воронеж')
        user_markup2.row('Омск', 'Новосибирск')
        user_markup2.row('Рязань')
        user_markup2.row('Вернуться')
        bot.send_message(message.from_user.id, 'Выберите город.', reply_markup=user_markup2)
    if message.text == 'Вакансии':
        user_markup3 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup3.row('Вернуться')
        bot.send_message(message.from_user.id, constants.JOB,reply_markup=user_markup3, parse_mode='Markdown')
    if message.text == 'Отмена':
        user_markup4 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup4.row('Прайс-лист')
        user_markup4.row('Вакансии', 'FAQ')
        user_markup4.row('Выход')
        bot.send_message(message.from_user.id, 'Ваше действие?', reply_markup=user_markup4)
    if message.text == 'Выход':
        user_markup5 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup5.row('СТАРТ')
        bot.send_message(message.from_user.id, 'Всего доброго!', reply_markup=user_markup5)
    if message.text == 'FAQ':
        user_markup6 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup6.row('Вернуться')
        bot.send_message(message.from_user.id, constants.FAQ,reply_markup=user_markup6, parse_mode='Markdown')
    if message.text == 'Вернуться':
        user_markup7 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup7.row('Прайс-лист')
        user_markup7.row('Вакансии', 'FAQ')
        user_markup7.row('Выход')
        bot.send_message(message.from_user.id, 'Ваше действие?', reply_markup=user_markup7)


    if message.text == 'Москва':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('01121', '01122', '01123', '01124')
        user_markup8.row('01141', '01142', '01151', '01221')
        user_markup8.row('01222', '01231', '01232', '01241')
        user_markup8.row('01251', '01252')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Москва*\n'
                                               'Выберите товар:\n'

                                               '- *Амфетамин HQ* (1.0 гр.)\n'
                                               '*Район*: ЮАО (Нагорный)\n'
                                               '*Цена*: 1200р. \n'
                                               '*Код*: 01121\n\n' 

											   '- *Амфетамин HQ* (1.0 гр.)\n'
                                               '*Район*: ЮВАО (Марьино)\n'
                                               '*Цена*: 1200р. \n'
                                               '*Код*: 01122\n\n' 

											   '- *Амфетамин HQ* (1.0 гр.)\n'
                                               '*Район*: ЮВАО (Южное Бутово)\n'
                                               '*Цена*: 1200р. \n'
                                               '*Код*: 01123\n\n' 
											   
											   '- *Амфетамин HQ* (1.0 гр.)\n'
                                               '*Район*: СЗАО (Митино)\n'
                                               '*Цена*: 1200р. \n'
                                               '*Код*: 01124\n\n' 
											   
#                                               '- *Амфетамин HQ* (2.0 гр.)\n'
#                                               '*Район*: ЮАО (Нагорный)\n'
#                                               '*Цена*: 2000р. \n'
#                                               '*Код*: 01131\n\n'
											   
#                                               '- *Амфетамин HQ* (2.0 гр.)\n'
#                                               '*Район*: ЦАО (Замоскворечье)\n'
#                                               '*Цена*: 2000р. \n'
#                                               '*Код*: 01132\n\n'

                                               '- *Амфетамин HQ* (3.0 гр.)\n'
                                               '*Район*: ЮВАО (Южное Бутово)\n'
                                               '*Цена*: 2800р. \n'
                                               '*Код*: 01141\n\n'

                                               '- *Амфетамин HQ* (3.0 гр.)\n'
                                               '*Район*: ЮАО (Нагорный)\n'
                                               '*Цена*: 2800р. \n'
                                               '*Код*: 01142\n\n'

                                               '- *Амфетамин HQ* (5.0 гр.)\n'
                                               '*Район*: ЗАО (Филевский парк)\n'
                                               '*Цена*: 3500р. \n'
                                               '*Код*: 01151\n\n'

                                               '- *Гашиш EURO* (1.0 гр.)\n'
                                               '*Район*: ЦАО (Замоскворечье)\n'
                                               '*Цена*: 1000р. \n'
                                               '*КОД*: 01221\n\n'
											   
                                               '- *Гашиш EURO* (1.0 гр.)\n'
                                               '*Район*: ВАО (Измайлово)\n'
                                               '*Цена*: 1000р. \n'
                                               '*КОД*: 01222\n\n'
											   
                                               '- *Гашиш EURO* (2.0 гр.)\n'
                                               '*Район*: ЦАО (Замоскворечье)\n'
                                               '*Цена*: 1500р. \n'
                                               '*КОД*: 01231\n\n'

                                               '- *Гашиш EURO* (2.0 гр.)\n'
                                               '*Район*: ВАО (Измайлово)\n'
                                               '*Цена*: 1500р. \n'
                                               '*КОД*: 01232\n\n'

                                               '- *Гашиш EURO* (3.0 гр.)\n'
                                               '*Район*: ЮАО (Нагорный)\n'
                                               '*Цена*: 2000р. \n'
                                               '*КОД*: 01241\n\n'
                                               
                                               '- *Гашиш EURO* (5.0 гр.)\n'
                                               '*Район*: ВАО (Измайлово)\n'
                                               '*Цена*: 2800р. \n'
                                               '*КОД*: 01251\n\n'
											   
											   '- *Гашиш EURO* (5.0 гр.)\n'
                                               '*Район*: ЗАО (Филевский парк)\n'
                                               '*Цена*: 2800р. \n'
                                               '*КОД*: 01252\n\n', reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '01121':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЮАО (Нагорный).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
		
    if message.text == '01122':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЮВАО (Марьино).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01123':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЮВАО (Южное Бутово).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
		
    if message.text == '01124':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Москва*.\n' \
        '*Район*: СЗАО (Митино).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01131':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (2.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЮАО (Нагорный).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'

    if message.text == '01132':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (2.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЦАО (Замоскворечье).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'

    if message.text == '01141':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (3.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЮВАО (Южное Бутово).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01142':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (3.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЮАО (Нагорный).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01151':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3500'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (5.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЗАО (Филевский парк).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01221':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЦАО (Замоскворечье).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01222':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Москва*.\n' \
        '*Район*: ВАО (Измайлово).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01231':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЦАО (Замоскворечье).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01232':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Москва*.\n' \
        '*Район*: ВАО (Измайлово).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01241':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (3.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЮАО (Нагорный).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01251':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (5.0 гр.), в г. *Москва*.\n' \
        '*Район*: ВАО (Измайлово).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '01252':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (5.0 гр.), в г. *Москва*.\n' \
        '*Район*: ЗАО (Филевский парк).\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == 'Санкт-Петербург':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('0222', '0223', '0224')
        user_markup8.row('0214', '0215', '0247')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Санкт-Петербург*.\n'
                                               'Выберите товар:\n'

                                               '- *Гашиш EURO* (1.0 гр.) -\n'
                                               '*Район*: Кировский\n'
                                               '*Цена*: 800 р. \n'
                                               '*КОД*: 0222\n\n'

                                               '- *Гашиш EURO* (2.0 гр.) -\n'
                                               '*Район*: Фрунзенский\n'
                                               '*Цена*: 1500 р. \n'
                                               '*КОД*: 0223\n\n'

                                               '- *Гашиш EURO* (3.0 гр.) -\n'
                                               '*Район*: Московский\n'
                                               '*Цена*: 2100 р. \n'
                                               '*КОД*: 0224\n\n'

                                               '- *Амфетамин HQ* (3.0 гр.) -\n'
                                               '*Район*: Фрунзенский\n'
                                               '*Цена*: 1800 р. \n'
                                               '*КОД*: 0214\n\n'

                                               '- *Амфетамин HQ* (5.0 гр.) -\n'
                                               '*Район*: Калининский\n'
                                               '*Цена*: 2300 р. \n'
                                               '*КОД*: 0215\n\n'

                                               '- *MDMA Pills 240 мг.* (2 шт.) -\n'
                                               '*Район*: Московский\n'
                                               '*Цена*: 1600 р. \n'
                                               '*КОД*: 0247\n\n',reply_markup=user_markup8, parse_mode='Markdown')
# Hash
    if message.text == '0212':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Санкт-Петербург*.\n' \
        '*Район*: Фрунзенский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0213':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (2.0 гр.), в г. *Санкт-Петербург*.\n\n' \
        '*Район*: Фрунзенский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0214':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (3.0 гр.), в г. *Санкт-Петербург*.\n\n' \
        '*Район*: Фрунзенский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0215':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2300'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (5.0 гр.), в г. *Санкт-Петербург*.\n\n' \
        '*Район*: Калининский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '0222':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Санкт-Петербург*.\n\n' \
        '*Район*: Фрунзенский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0223':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Санкт-Петербург*.\n\n' \
        '*Район*: Фрунзенский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0224':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2100'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (3.0 гр.), в г. *Санкт-Петербург*.\n\n' \
        '*Район*: Московский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0225':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (5.0 гр.), в г. *Санкт-Петербург*.\n\n' \
        '*Район*: Калининский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# MDMA
    if message.text == '0247':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1600'
        PAYMENT = 'Вы выбрали *MDMA Pills* (2 шт.), в г. *Санкт-Петербург*.\n\n' \
        '*Район*: Московский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')


    if message.text == 'Белгород':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('0322', '0323', '0324')
        user_markup8.row('0312', '0313', '0348')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Белгород*.\n'
                                               'Выберите товар:\n'

                                               '- *Гашиш EURO* (1.0 гр.) -\n'
                                               '*Цена*: 1200 р. \n'
                                               '*КОД*: 0322\n\n'

                                               '- *Гашиш EURO* (2.0 гр.) -\n'
                                               '*Цена*: 2200 р. \n'
                                               '*КОД*: 0323\n\n'

                                               '- *Гашиш EURO* (3.0 гр.) -\n'
                                               '*Цена*: 3000 р. \n'
                                               '*КОД*: 0324\n\n'

                                               '- *Амфетамин (Оранжевый)* (1.0 гр.) -\n'
                                               '*Цена*: 1600 р. \n'
                                               '*КОД*: 0312\n\n'

                                               '- *Амфетамин (Оранжевый)* (2.0 гр.) -\n'
                                               '*Цена*: 3000 р. \n'
                                               '*КОД*: 0313\n\n'

                                               '- *Экстази* (2 шт.) -\n'
                                               '*Цена*: 1600 р. \n'
                                               '*КОД*: 0348\n\n', reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '0312':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1600'
        PAYMENT = 'Вы выбрали *Амфетамин  (Оранжевый)* (1.0 гр.), в г. *Белгород*.\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0313':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3000'
        PAYMENT = 'Вы выбрали *Амфетамин  (Оранжевый)* (2.0 гр.), в г. *Белгород*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0314':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '4200'
        PAYMENT = 'Вы выбрали *Амфетамин  (Оранжевый)* (3.0 гр.), в г. *Белгород*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0315':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '5000'
        PAYMENT = 'Вы выбрали *Амфетамин  (Оранжевый)* (5.0 гр.), в г. *Белгород*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# HASH
    if message.text == '0322':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Белгород*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0323':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2200'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Белгород*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0324':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (3.0 гр.), в г. *Белгород*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0325':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '4500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (5.0 гр.), в г. *Белгород*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# Extazy
    if message.text == '0348':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Экстази* (2 шт.), в г. *Белгород*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == 'Владивосток':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('0422', '0423')
        user_markup8.row('0412', '0448')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Владивосток*.\n'
                                               'Выберите товар:\n'

                                               '- *Амфетамин HQ* (1.0 гр.) -\n'
                                               '*Цена*: 1500 р. \n'
                                               '*КОД*: 0412\n\n'

#                                               '- *Амфетамин HQ* (2.0 гр.) -\n'
#                                               '*Цена*: 2800 р. \n'
#                                               '*КОД*: 0413\n\n'

                                               '- *Гашиш EURO* (1.0 гр.) -\n'
                                               '*Цена*: 1500 р. \n'
                                               '*КОД*: 0422\n\n'

                                               '- *Гашиш EURO* (2.0 гр.) -\n'
                                               '*Цена*: 2800 р. \n'
                                               '*КОД*: 0423\n\n'

#                                               '- *Гашиш EURO* (3.0 гр.) -\n'
#                                               '*Цена*: 4200 р. \n'
#                                               '*КОД*: 0424\n\n'

                                               '- *MDMA (Blue Hello Kitty)* (1 шт.) -\n'
                                               '*Цена*: 1500 р. \n'
                                               '*КОД*: 0448\n\n', reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '0412':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Владивосток*.\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0413':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (2.0 гр.), в г. *Владивосток*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0414':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3500'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (3.0 гр.), в г. *Владивосток*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0415':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '4200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (5.0 гр.), в г. *Владивосток*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# HASH
    if message.text == '0422':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Владивосток*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0423':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Владивосток*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0424':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '4200'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (3.0 гр.), в г. *Владивосток*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0425':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '4500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (5.0 гр.), в г. *Владивосток*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# MDMA
    if message.text == '0448':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *MDMA (Blue Hello Kitty)* (1 шт.), в г. *Владивосток*.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')


    if message.text == 'Воронеж':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('0522', '0523', '0524')
        user_markup8.row('0513', '0514', '0548')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Воронеж*.\n'
                                               'Выберите товар:\n'

                                               '- *Экстази (Rolls Royce)* (2 шт.) -\n'
											   '*Район*: Железнодорожный\n'
                                               '*Цена*: 2200 р. \n'
                                               '*КОД*: 0547\n\n'

                                               '- *Гашиш EURO* (1.0 гр.) -\n'
											   '*Район*: Ленинский\n'
                                               '*Цена*: 1000 р. \n'
                                               '*КОД*: 0522\n\n'

                                               '- *Гашиш EURO* (2.0 гр.) -\n'
                                               '*Район*: Коминтерновский\n'
											   '*Цена*: 1500 р. \n'
                                               '*КОД*: 0523\n\n'

                                               '- *Гашиш EURO* (3.0 гр.) -\n'
											   '*Район*: Железнодорожный\n'
                                               '*Цена*: 2000 р. \n'
                                               '*КОД*: 0524\n\n'

                                               '- *Амфетамин HQ* (2.0 гр.) -\n'
                                               '*Цена*: 2000 р. \n'
											   '*Район*: Центральный\n'
                                               '*КОД*: 0513\n\n'

                                               '- *Амфетамин HQ* (3.0 гр.) -\n'
											   '*Район*: Северный\n'
                                               '*Цена*: 2800 р. \n'
                                               '*КОД*: 0514\n\n', reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '0512':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1100'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Центральный\n\n'\
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0513':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (2.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Центральный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0514':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (3.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Северный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0515':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3500'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (5.0 гр.), в г. *Воронеж*.\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        '*Район*: Центральный\n\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# HASH
    if message.text == '0522':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Ленинский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0523':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Коминтерновский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0524':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (3.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Желехнодорожный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0525':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (5.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Ленинский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# Экстази
    if message.text == '0547':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2200'
        PAYMENT = 'Вы выбрали *Экстази (Rolls Royce)* (2 шт.), в г. *Воронеж*.\n' \
        '*Район*: Ленинский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == 'Екатеринбург':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('0622', '0623', '0624')
        user_markup8.row('0612', '0613', '0647')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Екатеринбург*.\n'
                                               'Выберите товар:\n'

                                               '- *Амфетамин (Розовый)* (1.0 гр.) -\n'
                                               '*Цена*: 1750 р. \n'
											   '*Район*: Центральный\n'
                                               '*КОД*: 0612\n\n'

                                               '- *Амфетамин (Розовый)* (2.0 гр.) -\n'
											   '*Район*: Вокзальный\n'
                                               '*Цена*: 2700 р. \n'
                                               '*КОД*: 0613\n\n'

                                               '- *Гашиш Q7* (1.0 гр.) -\n'
											   '*Район*: Парковый\n'
                                               '*Цена*: 1100 р. \n'
                                               '*КОД*: 0622\n\n'

                                               '- *Гашиш Q7* (2.0 гр.) -\n'
                                               '*Район*: Центральный\n'
											   '*Цена*: 2000 р. \n'
                                               '*КОД*: 0623\n\n'

                                               '- *Гашиш Q7* (3.0 гр.) -\n'
											   '*Район*: Вокзальный\n'
                                               '*Цена*: 2800 р. \n'
                                               '*КОД*: 0624\n\n'							  

                                               '- *Экстази (Lego)* (3 шт.) -\n'
											   '*Район*: Центральный\n'
                                               '*Цена*: 2650 р. \n'
                                               '*КОД*: 0647\n\n', reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '0612':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1750'
        PAYMENT = 'Вы выбрали *Амфетамин (Розовый)* (1.0 гр.), в г. *Екатеринбург*.\n' \
        '*Район*: Центральный\n\n'\
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0613':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2700'
        PAYMENT = 'Вы выбрали *Амфетамин (Розовый)* (2.0 гр.), в г. *Екатеринбург*.\n' \
        '*Район*: Вокзальный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0614':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3700'
        PAYMENT = 'Вы выбрали *Амфетамин (Розовый)* (3.0 гр.), в г. *Екатеринбург*.\n' \
        '*Район*: Вокзальный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0615':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '5500'
        PAYMENT = 'Вы выбрали *Амфетамин (Розовый)* (5.0 гр.), в г. *Екатеринбург*.\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        '*Район*: Центральный\n\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# HASH
    if message.text == '0622':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1100'
        PAYMENT = 'Вы выбрали *Гашиш Q7* (1.0 гр.), в г. *Екатеринбург*.\n' \
        '*Район*: Парковый\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0623':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Гашиш Q7* (2.0 гр.), в г. *Екатеринбург*.\n' \
        '*Район*: Центральный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0624':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Гашиш Q7* (3.0 гр.), в г. *Екатеринбург*.\n' \
        '*Район*: Вокзальный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0625':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '4300'
        PAYMENT = 'Вы выбрали *Гашиш Q7* (5.0 гр.), в г. *Екатеринбург*.\n' \
        '*Район*: Парковый\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# Экстази
    if message.text == '0647':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2600'
        PAYMENT = 'Вы выбрали *Экстази (Lego)* (3 шт.), в г. *Екатеринбург*.\n' \
        '*Район*: Парковый\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == 'Ижевск':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('07221', '07222', '0723')
        user_markup8.row('0752', '0753', '0768')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Ижевск*.\n'
                                               'Выберите товар:\n'

                                               '- *Гашиш EURO* (1.0 гр.) -\n'
											   '*Район*: Ипподром\n'
                                               '*Цена*: 1200 р. \n'
                                               '*КОД*: 07221\n\n'
											   
                                               '- *Гашиш А.С.А.В.* (1.0 гр.) -\n'
											   '*Район*: Ипподром\n'
                                               '*Цена*: 1300 р. \n'
                                               '*КОД*: 07222\n\n'

                                               '- *Гашиш EURO* (2.0 гр.) -\n'
                                               '*Район*: Ипподром\n'
											   '*Цена*: 2300 р. \n'
                                               '*КОД*: 0723\n\n'

                                               '- *Мефедрон (Кристализованный)* (1.0 гр.) -\n'
                                               '*Цена*: 1700 р. \n'
											   '*Район*: Ипподром\n'
                                               '*КОД*: 0752\n\n'

                                               '- *Мефедрон (Кристализованный)* (2.0 гр.) -\n'
											   '*Район*: Ипподром\n'
                                               '*Цена*: 2700 р. \n'
                                               '*КОД*: 0753\n\n'
											  

                                               '- *Apple Red Pills* (2 шт.) -\n'
											   '*Район*: Ипподром\n'
                                               '*Цена*: 1200 р. \n'
                                               '*КОД*: 0768\n\n', reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '0752':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1700'
        PAYMENT = 'Вы выбрали *Мефедрон (Кристализованный)* (1.0 гр.), в г. *Ижевск*.\n' \
        '*Район*: Ипподром\n\n'\
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0753':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2700'
        PAYMENT = 'Вы выбрали *Мефедрон (Кристализованный)* (2.0 гр.), в г. *Ижевск*.\n' \
        '*Район*: Ипподром\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# HASH
    if message.text == '07221':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Ижевск*.\n' \
        '*Район*: Ипподром\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '07222':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1300'
        PAYMENT = 'Вы выбрали *Гашиш А.С.А.В.* (1.0 гр.), в г. *Ижевск*.\n' \
        '*Район*: Ипподром\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0723':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2300'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Ижевск*.\n' \
        '*Район*: Ипподром\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

# Экстази
    if message.text == '0768':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Apple Red Pills* (2 шт.), в г. *Ижевск*.\n' \
        '*Район*: Ипподром\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

		
    if message.text == 'Самара':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('09221', '09222', '09231')
        user_markup8.row('09232', '09521', '09522', '09523')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Самара*.\n'
                                               'Выберите товар:\n'

                                               '- *Гашиш EURO* (1.0 гр.) -\n'
											   '*Район*: Центральный\n'
                                               '*Цена*: 1000 р. \n'
                                               '*КОД*: 09221\n\n'
											   
                                               '- *Гашиш EURO* (1.0 гр.) -\n'
											   '*Район*: Западный\n'
                                               '*Цена*: 1000 р. \n'
                                               '*КОД*: 09222\n\n'

                                               '- *Гашиш Q7* (2.0 гр.) -\n'
                                               '*Район*: Юго-Западный\n'
											   '*Цена*: 1800 р. \n'
                                               '*КОД*: 09231\n\n'
											   
                                               '- *Гашиш Q7* (2.0 гр.) -\n'
                                               '*Район*: Западный\n'
											   '*Цена*: 1800 р. \n'
                                               '*КОД*: 09232\n\n'

                                               '- *Амфетамин HQ* (1.0 гр.) -\n'
                                               '*Цена*: 1200 р. \n'
											   '*Район*: Юго-Западный\n'
                                               '*КОД*: 09521\n\n'

                                               '- *Амфетамин HQ* (1.0 гр.) -\n'
                                               '*Цена*: 1200 р. \n'
											   '*Район*: Западный\n'
                                               '*КОД*: 09522\n\n'
											   
                                               '- *Амфетамин HQ* (2.0 гр.) -\n'
                                               '*Цена*: 2000 р. \n'
											   '*Район*: Центральный\n'
                                               '*КОД*: 09523\n\n', reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '09521':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин HQ* (1.0 гр.), в г. *Самара*.\n' \
        '*Район*: Юго-Западный\n\n'\
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
		
    if message.text == '09522':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин HQ* (1.0 гр.), в г. *Самара*.\n' \
        '*Район*: Западный\n\n'\
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
		
    if message.text == '09523':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Амфетамин HQ* (2.0 гр.), в г. *Самара*.\n' \
        '*Район*: Центральный\n\n'\
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
		
# HASH
    if message.text == '09221':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Самара*.\n' \
        '*Район*: Центральный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '09222':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Самара*.\n' \
        '*Район*: Западный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

# HASH
    if message.text == '09231':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1800'
        PAYMENT = 'Вы выбрали *Гашиш Q7* (2.0 гр.), в г. *Самара*.\n' \
        '*Район*: Юго-Западный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '09232':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1800'
        PAYMENT = 'Вы выбрали *Гашиш Q7* (2.0 гр.), в г. *Самара*.\n' \
        '*Район*: Западный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == 'Воронеж':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('1022', '1023', '1024')
        user_markup8.row('1013', '1014', '1048')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Воронеж*.\n'
                                               'Выберите товар:\n'

                                               '- *Экстази (Rolls Royce)* (2 шт.) -\n'
											   '*Район*: Железнодорожный\n'
                                               '*Цена*: 2200 р. \n'
                                               '*КОД*: 1047\n\n'

                                               '- *Гашиш EURO* (1.0 гр.) -\n'
											   '*Район*: Ленинский\n'
                                               '*Цена*: 1000 р. \n'
                                               '*КОД*: 1022\n\n'

                                               '- *Гашиш EURO* (2.0 гр.) -\n'
                                               '*Район*: Коминтерновский\n'
											   '*Цена*: 1500 р. \n'
                                               '*КОД*: 1023\n\n'

                                               '- *Гашиш EURO* (3.0 гр.) -\n'
											   '*Район*: Железнодорожный\n'
                                               '*Цена*: 2000 р. \n'
                                               '*КОД*: 1024\n\n'

                                               '- *Амфетамин HQ* (2.0 гр.) -\n'
                                               '*Цена*: 2000 р. \n'
											   '*Район*: Центральный\n'
                                               '*КОД*: 1013\n\n'

                                               '- *Амфетамин HQ* (3.0 гр.) -\n'
											   '*Район*: Северный\n'
                                               '*Цена*: 2800 р. \n'
                                               '*КОД*: 1014\n\n', reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '1012':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1100'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Центральный\n\n'\
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '1013':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (2.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Центральный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '1014':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (3.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Северный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '1015':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3500'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (5.0 гр.), в г. *Воронеж*.\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        '*Район*: Центральный\n\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# HASH
    if message.text == '1022':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Ленинский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '1023':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Коминтерновский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '1024':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (3.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Желехнодорожный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '1025':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (5.0 гр.), в г. *Воронеж*.\n' \
        '*Район*: Ленинский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# Экстази
    if message.text == '1047':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2200'
        PAYMENT = 'Вы выбрали *Экстази (Rolls Royce)* (2 шт.), в г. *Воронеж*.\n' \
        '*Район*: Ленинский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == 'Омск':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('0422', '0423', '0424')
        user_markup8.row('0414', '0415', '0447')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Омск*.\n'
                                               'Выберите товар:\n'

                                               '- *Гашиш EURO* (1.0 гр.) -\n'
                                               '*Район*: Кировский\n'
                                               '*Цена*: 800 р. \n'
                                               '*КОД*: 0422\n\n'

                                               '- *Гашиш EURO* (2.0 гр.) -\n'
                                               '*Район*: Октябрьский\n'
                                               '*Цена*: 1500 р. \n'
                                               '*КОД*: 0423\n\n'

                                               '- *Гашиш EURO* (3.0 гр.) -\n'
                                               '*Район*: Советский\n'
                                               '*Цена*: 2100 р. \n'
                                               '*КОД*: 0424\n\n'

                                               '- *Амфетамин HQ* (3.0 гр.) -\n'
                                               '*Район*: Октябрьский\n'
                                               '*Цена*: 1800 р. \n'
                                               '*КОД*: 0414\n\n'

                                               '- *Амфетамин HQ* (5.0 гр.) -\n'
                                               '*Район*: Центральный\n'
                                               '*Цена*: 2300 р. \n'
                                               '*КОД*: 0415\n\n'

                                               '- *MDMA Pills 240 мг.* (2 шт.) -\n'
                                               '*Район*: Советский\n'
                                               '*Цена*: 1600 р. \n'
                                               '*КОД*: 0447\n\n',reply_markup=user_markup8, parse_mode='Markdown')
# Hash
    if message.text == '0412':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Омск*.\n' \
        '*Район*: Октябрьский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0413':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (2.0 гр.), в г. *Омск*.\n\n' \
        '*Район*: Октябрьский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0414':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (3.0 гр.), в г. *Омск*.\n\n' \
        '*Район*: Октябрьский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0415':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2300'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (5.0 гр.), в г. *Омск*.\n\n' \
        '*Район*: Центральный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '0422':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Омск*.\n\n' \
        '*Район*: Октябрьский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0423':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Омск*.\n\n' \
        '*Район*: Октябрьский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0424':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2100'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (3.0 гр.), в г. *Омск*.\n\n' \
        '*Район*: Советский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '0425':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (5.0 гр.), в г. *Омск*.\n\n' \
        '*Район*: Центральный.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
# MDMA
    if message.text == '0447':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1600'
        PAYMENT = 'Вы выбрали *MDMA Pills* (2 шт.), в г. *Омск*.\n\n' \
        '*Район*: Советский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

		
    if message.text == 'Новосибирск':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('10121', '10122')
        user_markup8.row('10141', '10142', '10151', '10221')
        user_markup8.row('10222', '10231', '10232', '10241')
        user_markup8.row('10251')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Новосибирск*\n'
                                               'Выберите товар:\n'

                                               '- *Амфетамин HQ* (1.0 гр.)\n'
                                               '*Район*: Дзержинский\n'
                                               '*Цена*: 1200р. \n'
                                               '*Код*: 10121\n\n' 

											   '- *Амфетамин HQ* (1.0 гр.)\n'
                                               '*Район*: Железнодорожный\n'
                                               '*Цена*: 1200р. \n'
                                               '*Код*: 10122\n\n' 

                                               '- *Амфетамин HQ* (3.0 гр.)\n'
                                               '*Район*: Калининский\n'
                                               '*Цена*: 2800р. \n'
                                               '*Код*: 10141\n\n'

                                               '- *Амфетамин HQ* (3.0 гр.)\n'
                                               '*Район*: Дзержинский\n'
                                               '*Цена*: 2800р. \n'
                                               '*Код*: 10142\n\n'

                                               '- *Амфетамин HQ* (5.0 гр.)\n'
                                               '*Район*: Ленинский\n'
                                               '*Цена*: 3500р. \n'
                                               '*Код*: 10151\n\n'

                                               '- *Гашиш EURO* (1.0 гр.)\n'
                                               '*Район*: Октябрьский\n'
                                               '*Цена*: 1000р. \n'
                                               '*КОД*: 10221\n\n'
											   
                                               '- *Гашиш EURO* (1.0 гр.)\n'
                                               '*Район*: Центральный\n'
                                               '*Цена*: 1000р. \n'
                                               '*КОД*: 10222\n\n'
											   
                                               '- *Гашиш EURO* (2.0 гр.)\n'
                                               '*Район*: Октябрьский\n'
                                               '*Цена*: 1500р. \n'
                                               '*КОД*: 10231\n\n'

                                               '- *Гашиш EURO* (2.0 гр.)\n'
                                               '*Район*: Центральный\n'
                                               '*Цена*: 1500р. \n'
                                               '*КОД*: 10232\n\n'

                                               '- *Гашиш EURO* (3.0 гр.)\n'
                                               '*Район*: Дзержинский\n'
                                               '*Цена*: 2000р. \n'
                                               '*КОД*: 10241\n\n'
                                               
                                               '- *Гашиш EURO* (5.0 гр.)\n'
                                               '*Район*: Центральный\n'
                                               '*Цена*: 2800р. \n'
                                               '*КОД*: 10251\n\n', reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '10121':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Дзержинский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
		
    if message.text == '10122':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Железнодорожный.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '10123':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Калининский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
		
    if message.text == '10124':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (1.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Кировский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '10131':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (2.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Дзержинский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'

    if message.text == '10132':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (2.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Октябрьский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'

    if message.text == '10141':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (3.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Калининский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '10142':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (3.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Дзержинский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '10151':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '3500'
        PAYMENT = 'Вы выбрали *Амфетамин  HQ* (5.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Ленинский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '10221':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Октябрьский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '10222':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Центральный.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '10231':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Октябрьский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '10232':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1500'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (2.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Центральный.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '10241':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (3.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Дзержинский.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == '10251':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2800'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (5.0 гр.), в г. *Новосибирск*.\n' \
        '*Район*: Центральный.\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

    if message.text == 'Рязань':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('11221', '11222', '11231')
        user_markup8.row('11232', '11521', '11522', '11523')
        user_markup8.row('Вeрнуться')
        bot.send_message(message.from_user.id, 'Вы выбрали г. *Рязань*.\n'
                                               'Выберите товар:\n'

                                               '- *Гашиш EURO* (1.0 гр.) -\n'
											   '*Район*: Железнодорожный\n'
                                               '*Цена*: 1000 р. \n'
                                               '*КОД*: 11221\n\n'
											   
                                               '- *Гашиш EURO* (1.0 гр.) -\n'
											   '*Район*: Московский\n'
                                               '*Цена*: 1000 р. \n'
                                               '*КОД*: 11222\n\n'

                                               '- *Гашиш Q7* (2.0 гр.) -\n'
                                               '*Район*: Октябрьский\n'
											   '*Цена*: 1800 р. \n'
                                               '*КОД*: 11231\n\n'
											   
                                               '- *Гашиш Q7* (2.0 гр.) -\n'
                                               '*Район*: Московский\n'
											   '*Цена*: 1800 р. \n'
                                               '*КОД*: 11232\n\n'

                                               '- *Амфетамин HQ* (1.0 гр.) -\n'
                                               '*Цена*: 1200 р. \n'
											   '*Район*: Октябрьский\n'
                                               '*КОД*: 11521\n\n'

                                               '- *Амфетамин HQ* (1.0 гр.) -\n'
                                               '*Цена*: 1200 р. \n'
											   '*Район*: Московский\n'
                                               '*КОД*: 11522\n\n'
											   
                                               '- *Амфетамин HQ* (2.0 гр.) -\n'
                                               '*Цена*: 2000 р. \n'
											   '*Район*: Железнодорожный\n'
                                               '*КОД*: 11523\n\n', reply_markup=user_markup8, parse_mode='Markdown')
# Amph
    if message.text == '11521':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин HQ* (1.0 гр.), в г. *Рязань*.\n' \
        '*Район*: Октябрьский\n\n'\
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
		
    if message.text == '11522':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1200'
        PAYMENT = 'Вы выбрали *Амфетамин HQ* (1.0 гр.), в г. *Рязань*.\n' \
        '*Район*: Московский\n\n'\
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
		
    if message.text == '11523':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '2000'
        PAYMENT = 'Вы выбрали *Амфетамин HQ* (2.0 гр.), в г. *Рязань*.\n' \
        '*Район*: Железнодорожный\n\n'\
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
		
# HASH
    if message.text == '11221':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Рязань*.\n' \
        '*Район*: Железнодорожный\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '11222':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1000'
        PAYMENT = 'Вы выбрали *Гашиш EURO* (1.0 гр.), в г. *Рязань*.\n' \
        '*Район*: Московский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')

# HASH
    if message.text == '11231':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1800'
        PAYMENT = 'Вы выбрали *Гашиш Q7* (2.0 гр.), в г. *Рязань*.\n' \
        '*Район*: Октябрьский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    if message.text == '11232':
        user_markup8 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup8.row('Отмена')
        SUMM = '1800'
        PAYMENT = 'Вы выбрали *Гашиш Q7* (2.0 гр.), в г. *Рязань*.\n' \
        '*Район*: Московский\n\n' \
        'Выполните перевод на QIWI-кошелек.\n' \
        'Номер: ' + QIWI + '.\n' \
        'Сумма перевода: *' + SUMM + '* р. \n\n' \
        'Без комментария бот не отследит Ваш перевод и не выдаст адрес.\n' \
        '*Обязательно* укажите комментарий к платежу: *' + RANDOM + '*.'
        bot.send_message(message.from_user.id, PAYMENT, reply_markup=user_markup8, parse_mode='Markdown')
    

if __name__ == '__main__':
     bot.polling(none_stop=True)