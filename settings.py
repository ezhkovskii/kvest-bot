from datetime import datetime, time
import pytz
import os.path
from random import randint


#константы
TZ_UFA = pytz.timezone('Asia/Yekaterinburg')
FDATETIME = "%d-%m-%Y %H:%M"
FDATE = "%d-%m-%Y"
FTIME = "%H:%M"
PATH = './goodmorning' #папка с картинками из ватсапа



#**********************Работа с датами и временем*************************

#возравщает текущую дату и время или дату
def current_datetime(format=FDATETIME):
    return datetime.now(TZ_UFA).strftime(format)

#возращает заданную дату в определенном формате
def this_date(year, month, day, hour=None, minute=None):
    if hour == None and minute == None:
        return datetime(year, month, day).strftime(FDATE)
    else:
        return datetime(year, month, day, hour, minute).strftime(FDATETIME)

#возвращает заданное время
def this_time(hour, minute):
    return time(hour, minute).strftime(FTIME)

#**********************Работа с картинками*************************

def good_morning():
	num_files = sum(os.path.isfile(os.path.join(PATH, f)) for f in os.listdir(PATH)) #количество файлов в папке из PATH
	num_image = randint(1, num_files)
	name_file_image = './goodmorning/' + str(num_image) + '.jpg'
	return name_file_image
	
#**********************Проверка регистрации юзера после старта*************************
def check_when_user_reg():
    pass