#Функции работы с BD бота
import requests
import json
import string
import datetime
import sqlite3

last_update_id = 0.1
last_update_time = datetime.datetime(2017, 3, 5)
kurs_postav_perem = 0.020


# ПРОВЕРКА В БАЗЕ ДАННЫХ ЗАПРОСА ----------------- 1 --------------------
def kurs_human(id_human):
	conn = sqlite3.connect("mydatabase.db")
	cursor = conn.cursor()
	#Проверка на наличие в базе курса
	sql = "SELECT * FROM albums WHERE id_human=?"
	cursor.execute(sql, [(id_human)])
	perem = cursor.fetchall()
	#Если нету тогда создаем.
	if perem ==[]:
		vivod = "От вас не было раньше запросов на курс, пожалуйста введите данные."
	else:
		vivod = kurs_izm(id_human)
	return vivod


# ВСТАВКА КУРСА ----------------- 2 --------------------
def kurs_pos_tav(kurs_postav,id_human): 
	kurs_postav_perem=kurs_postav
	id_human_perem=id_human
	vivod = kurs_postav_perem
	test_nol_now = 10
	try:
		kurs_postav_perem = float(kurs_postav_perem)
		test_nol_now = test_nol_now/kurs_postav_perem
	except:
		kurs_postav_perem=0.020
		vivod = "Фатальная ошибка при инициализации, выставлено 0.020 по умолчанию"

	if vivod != "Фатальная ошибка при инициализации, выставлено 0.020 по умолчанию":
		conn = sqlite3.connect("mydatabase.db")
		cursor = conn.cursor()
		valut_id = 1
		cursor.execute("INSERT INTO albums (id_human,kurs,valut_id) VALUES ('%s','%s','%s')"%(id_human_perem,kurs_postav_perem,valut_id))
		conn.commit()
	return "Вы поставили курс: "+vivod

# ВСТАВКА ВАЛЮТЫ ----------------- 2.1 --------------------
def kurs_pos_tav_val(val_postav,id_human): 
	val_postav_perem=val_postav
	id_human_perem=id_human
	vivod = val_postav_perem
	test_nol_now = 10
	try:
		val_postav_perem = float(val_postav_perem)
		test_nol_now = test_nol_now/kurs_postav_perem
	except:
		val_postav_perem=1
		vivod = "Фатальная ошибка при инициализации, выставлено ETH/BTC по умолчанию"
		
	# if val_postav_perem !=1 or  val_postav_perem !=2 or val_postav_perem !=3 or val_postav_perem !=4 or val_postav_perem !=5 or val_postav_perem !=6 or val_postav_perem !=7:
	# 	vivod = "Фатальная ошибка при инициализации, выставлено ETH/BTC по умолчанию"

	test = [(val_postav_perem,id_human_perem)]
	if vivod != "Фатальная ошибка при инициализации, выставлено ETH/BTC по умолчанию":
		conn = sqlite3.connect("mydatabase.db")
		cursor = conn.cursor()
		cursor.executemany(" UPDATE albums SET valut_id=? WHERE id_human=?",(test))
		conn.commit()
	return "Вы поставили валюту: "+vivod

# Поле в функцию (ПОДФУНКЦИЯ КУРС) ----------------- 3 --------------------
def dlya_func(id_human):
	conn = sqlite3.connect("mydatabase.db")
	cursor = conn.cursor()
	sql = "SELECT * FROM albums WHERE id_human=?"
	cursor.execute(sql, [(id_human)])
	perem = cursor.fetchall()
	perem = perem[-1]
	vivod = perem[2]
	return vivod


# Поле в функцию (ПОДФУНКЦИЯ ВАЛЮТЫ) ----------------- 3.1 --------------------
def dlya_func_val(id_human):
	conn = sqlite3.connect("mydatabase.db")
	cursor = conn.cursor()
	sql = "SELECT * FROM albums WHERE id_human=?"
	cursor.execute(sql, [(id_human)])
	perem = cursor.fetchall()
	perem = perem[-1]
	vivod = perem[3]
	return vivod

# ВЫВОД КУРСА  ----------------- 4 --------------------	
def kurs_izm(id_human):
	global last_update_id
	global last_update_time

	star = last_update_id
	star_time = last_update_time

	val_postav_perem = dlya_func_val(id_human)
	val_postav_perem = float(val_postav_perem)
	if val_postav_perem ==1:
		url= 'https://yobit.net/api/2/eth_btc/ticker'
		name = "ETH/BTC:"
	elif val_postav_perem ==2:
		url= 'https://yobit.net/api/2/yo_btc/ticker'
		name = "YO/BTC:"
	elif val_postav_perem ==3:
		url= 'https://yobit.net/api/2/yovi_btc/ticker'
		name = "YOVI/BTC:"
	elif val_postav_perem ==4:
		url= 'https://yobit.net/api/2/zec_btc/ticker'
		name = "ZEC/BTC:"
	elif val_postav_perem ==5:
		url= 'https://yobit.net/api/2/dash_btc/ticker'
		name = "DASH/BTC:"
	elif val_postav_perem ==6:
		url= 'https://yobit.net/api/2/lsk_btc/ticker'
		name = "LSK/BTC:"
	elif val_postav_perem ==7:
		url= 'https://yobit.net/api/2/ltc_btc/ticker'
		name = "LTC/BTC:"
	else:
		url= 'https://yobit.net/api/2/eth_btc/ticker'
		name = "Вы ввели неправильную цифру, обновите ПАРУ.Сейчас стоит ETH/BTC"

	response = requests.get(url).json()

	last_price = response['ticker']['last']
	last_time = datetime.datetime.now()

	kurs_postav_perem = dlya_func(id_human)
	kurs_postav_perem = float(kurs_postav_perem)

	razn_kurs_postav = ((last_price-kurs_postav_perem)/kurs_postav_perem)*100
	razn = ((last_price-last_update_id)/last_update_id)*100
	razn_date = last_time-star_time
	if razn >0:
			vivod = [
			(name),
			('| Курс с последнего запроса:',str(star)),
			('| Время прошлого запроса:',star_time.strftime("%Y-%m-%d | %H:%M:%S")),
			('------------'),
			('| Текущая цена:',str(last_price)),
			('| Текущее время запроса:',last_time.strftime("%Y-%m-%d | %H:%M:%S")),
			('------------'),
			('| Разница времени 🕓:',str(razn_date)),
			('| Разница с последнего запроса: ✅',str("%.4f" %razn),"%"),
			('------------'),
			('| Курс поставленный пользователем:',str(kurs_postav_perem)),
			('| Разница c поставленным пользователем курсом:',str("%.4f" %razn_kurs_postav),"%")]
	elif razn == 0:
			vivod = [
			(name),
			('| Курс с последнего запроса:',str(star)),
			('| Время прошлого запроса:',star_time.strftime("%Y-%m-%d | %H:%M:%S")),
			('------------'),
			('| Текущая цена:',str(last_price)),
			('| Текущее время запроса:',last_time.strftime("%Y-%m-%d | %H:%M:%S")),
			('------------'),
			('| Разница времени 🕓:',str(razn_date)),
			('| Разница с последнего запроса:',"0️⃣"),
			('------------'),
			('| Курс поставленный пользователем:',str(kurs_postav_perem)),
			('| Разница c поставленным пользователем курсом:',str("%.4f" %razn_kurs_postav),"%")]
	else:
			vivod = [
			(name),
			('| Курс с последнего запроса:',str(star)),
			('| Время прошлого запроса:',star_time.strftime("%Y-%m-%d | %H:%M:%S")),
			('------------'),
			('| Текущая цена:',str(last_price)),
			('| Текущее время запроса:',last_time.strftime("%Y-%m-%d | %H:%M:%S")),
			('------------'),
			('| Разница времени 🕓:',str(razn_date)),
			('| Разница с последнего запроса: ⛔️',str("%.4f" %razn),"%"),
			('------------'),
			('| Курс поставленный пользователем:',str(kurs_postav_perem)),
			('| Разница c поставленным пользователем курсом:',str("%.4f" %razn_kurs_postav),"%")]

	last_update_time = last_time
	last_update_id = last_price
	return "\n".join(map("\t".join,vivod))

# ОБНОВЛЕНИЕ КУРСА КАЖДОГО ПОЛЬЗОВАТЕЛЯ ----------------- 5 --------------------
def kurs_pos_obnov(kurs_postav,id_human): 
	kurs_postav_perem=kurs_postav
	id_human_perem=id_human
	vivod = kurs_postav_perem
	test_nol_now = 10
	try:
		kurs_postav_perem = float(kurs_postav_perem)
		test_nol_now = test_nol_now/kurs_postav_perem
	except:
		kurs_postav_perem=0.020
		vivod = "Фатальная ошибка при инициализации"

	if vivod != "Фатальная ошибка при инициализации":
		conn = sqlite3.connect("mydatabase.db")
		cursor = conn.cursor()
		test = [(kurs_postav_perem,id_human_perem)]
		cursor.executemany(" UPDATE albums SET kurs=? WHERE id_human=?",(test))
		conn.commit()
	return "Вы обновили курс до: "+vivod

# ОБНОВЛЕНИЕ ПАРЫ КАЖДОГО ПОЛЬЗОВАТЕЛЯ ----------------- 5.1 --------------------
def val_pos_obnov(val_postav,id_human): 
	val_postav_perem=val_postav
	id_human_perem=id_human
	vivod = val_postav_perem
	test_nol_now = 10
	try:
		val_postav_perem = float(val_postav_perem)
		test_nol_now = test_nol_now/val_postav_perem
	except:
		val_postav_perem=1
		vivod = "Фатальная ошибка при инициализации"

	if vivod != "Фатальная ошибка при инициализации":
		conn = sqlite3.connect("mydatabase.db")
		cursor = conn.cursor()
		test = [(val_postav_perem,id_human_perem)]
		cursor.executemany(" UPDATE albums SET valut_id=? WHERE id_human=?",(test))
		conn.commit()
	return "Вы обновили пару до: "+vivod