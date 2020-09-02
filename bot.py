#Библиотеки
import os
import requests
import telebot
import time
import schedule
from telebot.types import Message
from telebot import types
# ОРДЕРЫ
import urllib, http.client
import hmac, hashlib
#ФУНКЦИИ
from moi_kel import get_all, get_eth_btc,get_yo_btc,get_yovi_btc,get_zec_btc,get_dash_btc,get_lsk_btc,get_ltc_btc,get_eth_btc,get_btc_usd,get_btc_usd,get_eth_usd,get_yo_usd,get_ltc_usd,get_dash_usd,get_zec_usd,get_bchabc_usd
from func_bd_bot import kurs_pos_tav,kurs_human,kurs_izm,kurs_pos_obnov,kurs_pos_tav_val,val_pos_obnov

#Глобальные токены - СЕКРЕТНО
TOKEN = "703727616:AAELMD88UTNSo1gP7iyRyBaPCyn0DGgsbEg"
API_KEY = 'B6002E73EF499669742C65CA6AC1B6FD' 
API_SECRET = 'db23f9f4f961d5801cdade3543d5d08e'

bot = telebot.TeleBot(TOKEN)

# #Клавиатура пользователя - к сообщению
# keyboard = types.InlineKeyboardMarkup(row_width=1)
# all_button = types.InlineKeyboardButton(text="Полная информация",callback_data="all")
# kurs_button = types.InlineKeyboardButton(text="Курс ETH/BTC",callback_data="kurs")
# izm_button = types.InlineKeyboardButton(text="Изменение курса",callback_data="post_kurs")
# post_kurs_button = types.InlineKeyboardButton(text="Обновить личный курс",callback_data="obnov_kurs")
# keyboard.add(all_button,kurs_button,izm_button,post_kurs_button)

#Клавиатура пользователя - внизу экрана
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
izm_button = types.InlineKeyboardButton(text="Пользовательский вывод")
post_kurs_button = types.InlineKeyboardButton(text="Обновить пару")
post_val_button = types.InlineKeyboardButton(text="Обновить курс")
podsk_button = types.InlineKeyboardButton(text="Подсказка")
keyboard.add(izm_button,post_kurs_button,post_val_button,podsk_button)

#Ответчик на команды
@bot.message_handler(commands=['start','help'])
def send_welcome(message):
	vivod = [
		('Привет! Я бот который передает курс необходимой валюты с биржи YObit. Мои команды представлены ниже!',''),
		('| ————————————'),
		('| Курс к BTC: ',''),
		('| ————————————'),
		('| ETH / BTC:',' /ETH_BTC'),
		('| YO / BTC:',' /YO_BTC'),
		('| YOVI / BTC:',' /YOVI_BTC'),
		('| ZEC / BTC:',' /ZEC_BTC'),
		('| DASH / BTC:',' /DASH_BTC'),
		('| LSK / BTC:',' /LSK_BTC'),
		('| LTC / BTC:',' /LTC_BTC'),
		('| ————————————'),
		('| Курс к USD: ',''),
		('| ————————————'),
		('| BTC / USD:',' /BTC_USD'),
		('| ETH / USD:',' /ETH_USD'),
		('| YO / USD:',' /YO_USD'),
		('| ZEC / USD:',' /ZEC_USD'),
		('| DASH / USD:',' /DASH_USD'),
		('| BCHABC / USD:',' /BCHABC_USD'),
		('| LTC / USD:',' /LTC_USD'),
		('Здесь предложены все пары которые может вывести бот. Чтобы бот выводил необходимую вам пару, выберите номер пары: ',''),
		('| ————————————'),
		('| ETH / BTC:',' 1️⃣ '),
		('| ————————————'),
		('| YO / BTC:',' 2️⃣ '),
		('| ————————————'),
		('| YOVI / BTC:',' 3️⃣ '),
		('| ————————————'),
		('| ZEC / BTC:',' 4️⃣ '),
		('| ————————————'),
		('| DASH / BTC:',' 5️⃣ '),
		('| ————————————'),
		('| LSK / BTC:',' 6️⃣ '),
		('| ————————————'),
		('| LTC / BTC:',' 7️⃣ '),
		('| ————————————')]
	bot.reply_to(message,"\n".join(map("\t".join,vivod)),reply_markup=keyboard,parse_mode="Markdown")

		

@bot.message_handler(commands=['all'])
def send_all(message):
	bot.reply_to(message,get_all(),reply_markup=keyboard)

@bot.message_handler(commands=['izm'])
def izm_kurs(message):
	id_human_send = message.chat.id
	bot.reply_to(message, kurs_izm(id_human_send))
#========================BTC=========================================
@bot.message_handler(commands=['ETH_BTC'])
def send_kurs_eth_btc(message):
	bot.reply_to(message,get_eth_btc(),reply_markup=keyboard)

@bot.message_handler(commands=['YO_BTC'])
def send_kurs_yo_btc(message):
	bot.reply_to(message, get_yo_btc(),reply_markup=keyboard)

@bot.message_handler(commands=['YOVI_BTC'])
def send_kurs_yovi_btc(message):
	bot.reply_to(message, get_yovi_btc(),reply_markup=keyboard)

@bot.message_handler(commands=['ZEC_BTC'])
def send_kurs_zec_btc(message):
	bot.reply_to(message, get_zec_btc(),reply_markup=keyboard)

@bot.message_handler(commands=['DASH_BTC'])
def send_kurs_dash_btc(message):
	bot.reply_to(message, get_dash_btc(),reply_markup=keyboard)

@bot.message_handler(commands=['LSK_BTC'])
def send_kurs_lsk_btc(message):
	bot.reply_to(message, get_lsk_btc(),reply_markup=keyboard)

@bot.message_handler(commands=['LTC_BTC'])
def send_kurs_ltc_btc(message):
	bot.reply_to(message, get_ltc_btc(),reply_markup=keyboard)
#========================USD=========================================
@bot.message_handler(commands=['BTC_USD'])
def send_kurs_btc_usd(message):
	bot.reply_to(message,get_btc_usd(),reply_markup=keyboard)

@bot.message_handler(commands=['ETH_USD'])
def send_kurs_eth_usd(message):
	bot.reply_to(message,get_eth_usd(),reply_markup=keyboard)

@bot.message_handler(commands=['DASH_USD'])
def send_kurs_dash_usd(message):
	bot.reply_to(message,get_dash_usd(),reply_markup=keyboard)

@bot.message_handler(commands=['BCHABC_USD'])
def send_kurs_bchabc_usd(message):
	bot.reply_to(message,get_bchabc_usd(),reply_markup=keyboard)

@bot.message_handler(commands=['ZEC_USD'])
def send_kurs_zec_usd(message):
	bot.reply_to(message,get_zec_usd(),reply_markup=keyboard)

@bot.message_handler(commands=['LTC_USD'])
def send_kurs_ltc_usd(message):
	bot.reply_to(message,get_ltc_usd(),reply_markup=keyboard)

@bot.message_handler(commands=['YO_USD'])
def send_kurs_yo_usd(message):
	bot.reply_to(message,get_yo_usd(),reply_markup=keyboard)


@bot.message_handler(func=lambda message:True)
def echo_all(message):

	if message.text == "Подсказка":
		vivod = [
		('| Здесь предложены все курсы которые может вывести бот: ',''),
		('| ————————————'),
		('| Курс к BTC: ',''),
		('| ————————————'),
		('| ETH / BTC:',' /ETH_BTC'),
		('| YO / BTC:',' /YO_BTC'),
		('| YOVI / BTC:',' /YOVI_BTC'),
		('| ZEC / BTC:',' /ZEC_BTC'),
		('| DASH / BTC:',' /DASH_BTC'),
		('| LSK / BTC:',' /LSK_BTC'),
		('| LTC / BTC:',' /LTC_BTC'),
		('| ————————————'),
		('| Курс к USD: ',''),
		('| ————————————'),
		('| BTC / USD:',' /BTC_USD'),
		('| ETH / USD:',' /ETH_USD'),
		('| YO / USD:',' /YO_USD'),
		('| ZEC / USD:',' /ZEC_USD'),
		('| DASH / USD:',' /DASH_USD'),
		('| BCHABC / USD:',' /BCHABC_USD'),
		('| LTC / USD:',' /LTC_USD'),
		('Здесь предложены все пары которые может вывести бот. Чтобы бот выводил необходимую вам пару, выберите номер пары: ',''),
		('| ————————————'),
		('| ETH / BTC:',' 1️⃣ '),
		('| ————————————'),
		('| YO / BTC:',' 2️⃣ '),
		('| ————————————'),
		('| YOVI / BTC:',' 3️⃣ '),
		('| ————————————'),
		('| ZEC / BTC:',' 4️⃣ '),
		('| ————————————'),
		('| DASH / BTC:',' 5️⃣ '),
		('| ————————————'),
		('| LSK / BTC:',' 6️⃣ '),
		('| ————————————'),
		('| LTC / BTC:',' 7️⃣ '),
		('| ————————————')]
		bot.reply_to(message,"\n".join(map("\t".join,vivod)))

	if message.text == "Пользовательский вывод":
		prov_bd = message.chat.id
		cid = message.chat.id
		bot.send_message(cid, kurs_human(prov_bd))
		if kurs_human(prov_bd) == "От вас не было раньше запросов на курс, пожалуйста введите данные.":		
			msgPrice = bot.send_message(cid, 'Какой курс вы хотите поставить?:')
			bot.register_next_step_handler(msgPrice , step_Set_Price)
			
	
	if message.text == "Обновить курс":
		prov_bd = message.chat.id
		cid = message.chat.id
		msgPrice = bot.send_message(cid, 'На какой курс вы хотите обновить бота:')
		bot.register_next_step_handler(msgPrice , step_Set_Obnov)

	if message.text == "Обновить пару":
		prov_bd = message.chat.id
		cid = message.chat.id
		vivod_val_number = [
		('Здесь предложены все пары которые может вывести бот. Чтобы бот выводил необходимую вам пару, выберите номер пары: ',''),
		('————————————'),
		('ETH / BTC:',' 1️⃣ '),
		('————'),
		('YO / BTC:',' 2️⃣ '),
		('————'),
		('YOVI / BTC:',' 3️⃣ '),
		('————'),
		('ZEC / BTC:',' 4️⃣ '),
		('————'),
		('DASH / BTC:',' 5️⃣ '),
		('————'),
		('LSK / BTC:',' 6️⃣ '),
		('————'),
		('LTC / BTC:',' 7️⃣ '),
		('————————————')]
		bot.send_message(cid,"\n".join(map("\t".join,vivod_val_number)))
		msgPrice = bot.send_message(cid, 'На какую пару вы хотите обновить бота:')
		bot.register_next_step_handler(msgPrice , step_Set_Par)

#Работа с переменной в функцию проверки поля		
def step_Set_Price(message):
	vivod_val_number = [
		('Здесь предложены все пары которые может вывести бот. Чтобы бот выводил необходимую вам пару, выберите номер пары: ',''),
		('————————————'),
		('ETH / BTC:',' 1️⃣ '),
		('————'),
		('YO / BTC:',' 2️⃣ '),
		('————'),
		('YOVI / BTC:',' 3️⃣ '),
		('————'),
		('ZEC / BTC:',' 4️⃣ '),
		('————'),
		('DASH / BTC:',' 5️⃣ '),
		('————'),
		('LSK / BTC:',' 6️⃣ '),
		('————'),
		('LTC / BTC:',' 7️⃣ '),
		('————————————')]
	id_human = message.chat.id
	kurs_postav= message.text
	bot.send_message(id_human,kurs_pos_tav(kurs_postav,id_human),reply_markup=keyboard)
	bot.send_message(id_human,"\n".join(map("\t".join,vivod_val_number)))
	msgVal = bot.send_message(id_human, 'Введите валюту:')
	bot.register_next_step_handler(msgVal , step_Set_Val)

#Работа с переменной в функцию проверки поля		
def step_Set_Val(message):
	id_human = message.chat.id
	val_postav= message.text
	bot.send_message(id_human,kurs_pos_tav_val(val_postav,id_human),reply_markup=keyboard)	

#Работа с обновлением курса пользователя	
def step_Set_Obnov(message):
	id_human = message.chat.id
	kurs_postav= message.text
	bot.send_message(id_human,kurs_pos_obnov(kurs_postav,id_human),reply_markup=keyboard)	

#Работа с обновлением пары пользователя	
def step_Set_Par(message):
	id_human = message.chat.id
	val_postav= message.text
	bot.send_message(id_human,val_pos_obnov(val_postav,id_human),reply_markup=keyboard)	

# ВЫВОД ВАЛЮТ КУРСА - ВЛАД 

if __name__ == "__main__":
	bot.polling(none_stop=True)