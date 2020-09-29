import telebot
from telebot import types
import threading
from time import sleep

from tokenfile import TOKEN
from settings import FDATETIME, FTIME, FDATE, current_datetime, this_date, this_time, good_morning, check_when_user_reg
import db


bot = telebot.TeleBot(TOKEN)

#клавиатура для опроса 27.09
btn_yes_27 = types.InlineKeyboardButton('Конечно!\nЯ готов!', callback_data='yes_27')
btn_no_27 = types.InlineKeyboardButton('Чёт не', callback_data='no_27')
markup_27 = types.InlineKeyboardMarkup().add(btn_yes_27, btn_no_27)

def information():
	#все пользователи бота из бд
    users = db.query_all_user()

    if users:
        while True:

            # всем доброе утро в 10:00 каждый день
            if current_datetime(format=FTIME) == this_time(10, 00):
                name_file_image = good_morning()
                try:
                    image = open(name_file_image, 'rb')
                    for user in users:
                        try:
                            bot.send_photo(user[0], image)
                        except Exception as e:
                            print('ошибка "доброе утро" картинка')
                            print(e)
                    image.close()
                except:
                    for user in users:
                        try:
                            bot.send_message(user[0], 'Доброе утро! Хорошего настроения и улыбок на весь день! ☺️')
                        except Exception as e:
                            print('ошибка "доброе утро" текст')
                            print(e)
            
            #26.09 Общий текст о квесте. Мем
            if current_datetime(format=FDATETIME) == this_date(2020, 9, 26, 20, 0):
                for user in users:
                    try:
                        bot.send_message(user[0], f'Привет, {user[2]}! \n'
                                                  f'Мы рады приветствовать в игре «Хроники родного края». \n'
                                                  f'Переходи по ссылке: ... и жди новостей!💥')
                        bot.send_photo(user[0], 'https://301-1.ru/uploads/image/mem-so-shrekom-v-bolote-zaebumba_Iw87RIFG7o.jpeg')
                    except Exception as e:
                        print('ошибка "26.09"')
                        print(e)

            #27.09 Опрос ты готов?
            if current_datetime(format=FDATETIME) == this_date(2020, 9, 27, 20, 00):
                for user in users:
                    try:
                        bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "27.09"')
                        print(e)

            #28.09 Видео о городе
            if current_datetime(format=FDATETIME) == this_date(2020, 9, 28, 20, 00):
                for user in users:
                    try:
                        bot.send_message(user[0], f'Привет, {user[2]}!\nЛови видео о городе!')
                        #bot.send_video(user[0], 45612378)
                    except Exception as e:
                        print('ошибка "28.09"')
                        print(e)

            # 29.09
            if current_datetime(format=FDATETIME) == this_date(2020, 9, 29, 20, 00):
                for user in users:
                    try:
                        pass
                        #bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "29.09"')
                        print(e)

            # 30.09 факт
            if current_datetime(format=FDATETIME) == this_date(2020, 9, 30, 20, 00):
                for user in users:
                    try:
                        pass
                        #bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "30.09"')
                        print(e)

            # 1.10 было стало
            if current_datetime(format=FDATETIME) == this_date(2020, 10, 1, 20, 00):
                for user in users:
                    try:
                        pass
                        #bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "1.10"')
                        print(e)

            # 2.10 видео тренды
            if current_datetime(format=FDATETIME) == this_date(2020, 10, 2, 20, 00):
                for user in users:
                    try:
                        pass
                        #bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "2.10"')
                        print(e)


            # 3.10 финал шурале
            if current_datetime(format=FDATETIME) == this_date(2020, 10, 3, 20, 00):
                for user in users:
                    try:
                        pass
                        #bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "3.10"')
                        print(e)

            # 4.10 тик ток от оргов
            if current_datetime(format=FDATETIME) == this_date(2020, 10, 4, 20, 00):
                for user in users:
                    try:
                        pass
                        #bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "4.10"')
                        print(e)

            # 5.10 твбросы шурале
            if current_datetime(format=FDATETIME) == this_date(2020, 10, 5, 20, 00):
                for user in users:
                    try:
                        pass
                        #bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "5.10"')
                        print(e)

            # 6.10 инфа о квесте
            if current_datetime(format=FDATETIME) == this_date(2020, 10, 6, 20, 00):
                for user in users:
                    try:
                        pass
                        #bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "6.10"')
                        print(e)

            # 7.10 шурале о участниках
            if current_datetime(format=FDATETIME) == this_date(2020, 10, 7, 13, 00):
                for user in users:
                    try:
                        pass
                        #bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "7.10"')
                        print(e)

            # 7.10 опрос о квесте
            if current_datetime(format=FDATETIME) == this_date(2020, 10, 7, 21, 00):
                for user in users:
                    try:
                        pass
                        #bot.send_message(user[0], f'Привет, {user[2]}!\nТы готов к игре?', reply_markup=markup_27)
                    except Exception as e:
                        print('ошибка "7.10" опрос')
                        print(e)

            sleep(60)
            
    else:
        print('Нет юзеров в бд')
        return



'''
Обработчик команды /start
Добавляем в бд нового пользователя
'''
@bot.message_handler(commands=['start'])
def send_welcome(message):
    sent = bot.send_message(message.from_user.id, f'Добро пожаловать в игру! Назови своё имя 😊')
    bot.register_next_step_handler(sent, hello)


def hello(message):
    name = message.text
    db.register_user(message.from_user.id, message.from_user.username, name)
    bot.send_message(message.from_user.id,
                     f'Отлично, {name}! Я твой квест-бот! ' 
                     f'Именно благодаря мне ты будешь узнавать самую актуальную и интересную информацию об игре! ⚡️\n'
                     f'Включай уведомления и хорошее настроение, ведь совсем скоро ты получишь новое послание. 😏 \n'
                     f'Все вопросы ты можешь задать по номеру: 899999999999999999')
    #bot.send_photo(message.from_user.id, )

    if check_when_user_reg():
        pass



'''
Опрос 27.09
'''
@bot.callback_query_handler(func=lambda call: call.data == 'yes_27' or call.data == 'no_27')
def answer_27(call):
    if call.data == 'yes_27':
        bot.send_photo(call.from_user.id,
                       'https://301-1.ru/uploads/image/mem-so-shrekom-v-bolote-zaebumba_Iw87RIFG7o.jpeg')
        bot.send_message(call.from_user.id, f'Квест «Хроники родного края» посвящен истории Республики Башкортостан. '
                                            f'А знаешь ли ты историю нашей страны? 🧐 \n ' \
                                            f'Если да, то ты наверняка слышал о нашем партнере,  ' \
                                            f'интерактивном историческом парке «Россия - моя история»! '
                                            f'Если нет, то скорее заглядывай туда: ...')
    if call.data == 'no_27':
        bot.send_photo(call.from_user.id,
                       'https://borodatiyvopros.com/wp-content/uploads/2020/05/SOtLsavrJ00_146987_8.jpg')
        bot.send_message(call.from_user.id, f'Океей...\nТы можешь меня отключить и я тебя больше не побеспокою. '
                                            f'Уходи.\n'
                                            f'Или подумай еще раз.')
        bot.send_message(call.from_user.id, f'Ты готов к квесту?', reply_markup=markup_27)


#todo: танцы, задания

if __name__=='__main__':
	db.create_tables()

	t1 = threading.Thread(target=information, daemon=True)
	t1.start()

	bot.polling()
