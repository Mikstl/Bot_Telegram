import requests
import json
import string
import datetime

def get_all():

	url= 'https://yobit.net/api/2/eth_btc/ticker'
	url_btc = 'https://yobit.net/api/2/btc_usd/ticker'
	url_eth = 'https://yobit.net/api/2/eth_usd/ticker'

	response = requests.get(url).json()
	response_btc = requests.get(url_btc).json()
	response_eth = requests.get(url_eth).json()

	last_price = response['ticker']['last']
	high_price = response['ticker']['high']
	low_price = response['ticker']['low']
	buy_price = response['ticker']['buy']
	sell_price = response['ticker']['sell']

	last_price_btc = response_btc['ticker']['last']
	high_price_btc = response_btc['ticker']['high']
	low_price_btc = response_btc['ticker']['low']

	last_price_eth = response_eth['ticker']['last']
	high_price_eth = response_eth['ticker']['high']
	low_price_eth = response_eth['ticker']['low']

	vivod = [
	('ETH/BTC:'),
	('| Последний курс:',str("%.8f" %last_price)),
	('| Макc. курc:',str("%.8f" %high_price)),
	('| Мин. курс:',str("%.8f" %low_price)),
	('| Покупка:',str("%.8f" %buy_price)),
	('| Продажа:',str("%.8f" %sell_price)),
	('-------'),
	('BTC/USD:'),
	('| Последний курс: ',str("%.2f" %last_price_btc),"$"),
	('| Макc. курc: ',str("%.2f" %high_price_btc),"$"),
	('| Мин. курс: ',str("%.2f" %low_price_btc),"$"),
	('-------'),
	('ETH/USD:'),
	('| Последний курс: ',str("%.2f" %last_price_eth),"$"),
	('| Макc. курc: ',str("%.2f" %high_price_eth),"$"),
	('| Мин. курс: ',str("%.2f" %low_price_eth),"$"),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------ETH/BTC---------------------------
def get_eth_btc():
	url= 'https://yobit.net/api/2/eth_btc/ticker'
	response = requests.get(url).json()
	last_price = response['ticker']['last']
	high_price = response['ticker']['high']
	low_price = response['ticker']['low']
	buy_price = response['ticker']['buy']
	sell_price = response['ticker']['sell']
	vivod = [
	('ETH/BTC:'),
	('| Последний курс:',str("%.8f" %last_price)),
	('| Макc. курc:',str("%.8f" %high_price)),
	('| Мин. курс:',str("%.8f" %low_price)),
	('| Покупка:',str("%.8f" %buy_price)),
	('| Продажа:',str("%.8f" %sell_price)),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------YO/BTC---------------------------
def get_yo_btc():
	url= 'https://yobit.net/api/2/yo_btc/ticker'
	response = requests.get(url).json()
	last_price = response['ticker']['last']
	high_price = response['ticker']['high']
	low_price = response['ticker']['low']
	buy_price = response['ticker']['buy']
	sell_price = response['ticker']['sell']
	vivod = [
	('YO/BTC:'),
	('| Последний курс:',str("%.8f" %last_price)),
	('| Макc. курc:',str("%.8f" %high_price)),
	('| Мин. курс:',str("%.8f" %low_price)),
	('| Покупка:',str("%.8f" %buy_price)),
	('| Продажа:',str("%.8f" %sell_price)),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------YOVI/BTC---------------------------
def get_yovi_btc():
	url= 'https://yobit.net/api/2/yovi_btc/ticker'
	response = requests.get(url).json()
	last_price = response['ticker']['last']
	high_price = response['ticker']['high']
	low_price = response['ticker']['low']
	buy_price = response['ticker']['buy']
	sell_price = response['ticker']['sell']
	vivod = [
	('YOVI/BTC:'),
	('| Последний курс:',str("%.8f" %last_price)),
	('| Макc. курc:',str("%.8f" %high_price)),
	('| Мин. курс:',str("%.8f" %low_price)),
	('| Покупка:',str("%.8f" %buy_price)),
	('| Продажа:',str("%.8f" %sell_price)),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------ZEC/BTC---------------------------
def get_zec_btc():
	url= 'https://yobit.net/api/2/zec_btc/ticker'
	response = requests.get(url).json()
	last_price = response['ticker']['last']
	high_price = response['ticker']['high']
	low_price = response['ticker']['low']
	buy_price = response['ticker']['buy']
	sell_price = response['ticker']['sell']
	vivod = [
	('ZEC/BTC:'),
	('| Последний курс:',str("%.8f" %last_price)),
	('| Макc. курc:',str("%.8f" %high_price)),
	('| Мин. курс:',str("%.8f" %low_price)),
	('| Покупка:',str("%.8f" %buy_price)),
	('| Продажа:',str("%.8f" %sell_price)),
	('-------')]
	return "\n".join(map("\t".join,vivod))		
#  ------------------------DASH/BTC---------------------------
def get_dash_btc():
	url = 'https://yobit.net/api/2/dash_btc/ticker'
	response = requests.get(url).json()
	last_price = response['ticker']['last']
	high_price = response['ticker']['high']
	low_price = response['ticker']['low']
	buy_price = response['ticker']['buy']
	sell_price = response['ticker']['sell']
	vivod = [
	('DASH/BTC:'),
	('| Последний курс:',str("%.8f" %last_price)),
	('| Макc. курc:',str("%.8f" %high_price)),
	('| Мин. курс:',str("%.8f" %low_price)),
	('| Покупка:',str("%.8f" %buy_price)),
	('| Продажа:',str("%.8f" %sell_price)),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------LSK/BTC---------------------------
def get_lsk_btc():
	url = 'https://yobit.net/api/2/lsk_btc/ticker'
	response = requests.get(url).json()
	last_price = response['ticker']['last']
	high_price = response['ticker']['high']
	low_price = response['ticker']['low']
	buy_price = response['ticker']['buy']
	sell_price = response['ticker']['sell']
	vivod = [
	('LSK/BTC:'),
	('| Последний курс:',str("%.8f" %last_price)),
	('| Макc. курc:',str("%.8f" %high_price)),
	('| Мин. курс:',str("%.8f" %low_price)),
	('| Покупка:',str("%.8f" %buy_price)),
	('| Продажа:',str("%.8f" %sell_price)),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------LTC/BTC---------------------------
def get_ltc_btc():
	url = 'https://yobit.net/api/2/ltc_btc/ticker'
	response = requests.get(url).json()
	last_price = response['ticker']['last']
	high_price = response['ticker']['high']
	low_price = response['ticker']['low']
	buy_price = response['ticker']['buy']
	sell_price = response['ticker']['sell']
	vivod = [
	('LTC/BTC:'),
	('| Последний курс:',str("%.8f" %last_price)),
	('| Макc. курc:',str("%.8f" %high_price)),
	('| Мин. курс:',str("%.8f" %low_price)),
	('| Покупка:',str("%.8f" %buy_price)),
	('| Продажа:',str("%.8f" %sell_price)),
	('-------')]
	return "\n".join(map("\t".join,vivod))

#  ------------------------BTC/USD---------------------------
def get_btc_usd():
	url_usd = 'https://yobit.net/api/2/btc_usd/ticker'
	response_usd = requests.get(url_usd).json()
	last_price_usd = response_usd['ticker']['last']
	high_price_usd = response_usd['ticker']['high']
	low_price_usd = response_usd['ticker']['low']
	vivod=[
	('BTC/USD:'),
	('| Последний курс: ',str("%.2f" %last_price_usd),"$"),
	('| Макc. курc: ',str("%.2f" %high_price_usd),"$"),
	('| Мин. курс: ',str("%.2f" %low_price_usd),"$"),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------ETH/USD---------------------------
def get_eth_usd():
	url_usd = 'https://yobit.net/api/2/eth_usd/ticker'
	response_usd = requests.get(url_usd).json()
	last_price_usd = response_usd['ticker']['last']
	high_price_usd = response_usd['ticker']['high']
	low_price_usd = response_usd['ticker']['low']
	vivod=[
	('ETH/USD:'),
	('| Последний курс: ',str("%.2f" %last_price_usd),"$"),
	('| Макc. курc: ',str("%.2f" %high_price_usd),"$"),
	('| Мин. курс: ',str("%.2f" %low_price_usd),"$"),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------YO/USD---------------------------
def get_yo_usd():
	url_usd = 'https://yobit.net/api/2/yo_usd/ticker'
	response_usd = requests.get(url_usd).json()
	last_price_usd = response_usd['ticker']['last']
	high_price_usd = response_usd['ticker']['high']
	low_price_usd = response_usd['ticker']['low']
	vivod=[
	('YO/USD:'),
	('| Последний курс: ',str("%.2f" %last_price_usd),"$"),
	('| Макc. курc: ',str("%.2f" %high_price_usd),"$"),
	('| Мин. курс: ',str("%.2f" %low_price_usd),"$"),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------LTC/USD---------------------------
def get_ltc_usd():
	url_usd = 'https://yobit.net/api/2/ltc_usd/ticker'
	response_usd = requests.get(url_usd).json()
	last_price_usd = response_usd['ticker']['last']
	high_price_usd = response_usd['ticker']['high']
	low_price_usd = response_usd['ticker']['low']
	vivod=[
	('LTC/USD:'),
	('| Последний курс: ',str("%.2f" %last_price_usd),"$"),
	('| Макc. курc: ',str("%.2f" %high_price_usd),"$"),
	('| Мин. курс: ',str("%.2f" %low_price_usd),"$"),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------DASH/USD---------------------------
def get_dash_usd():
	url_usd = 'https://yobit.net/api/2/dash_usd/ticker'
	response_usd = requests.get(url_usd).json()
	last_price_usd = response_usd['ticker']['last']
	high_price_usd = response_usd['ticker']['high']
	low_price_usd = response_usd['ticker']['low']
	vivod=[
	('DASH/USD:'),
	('| Последний курс: ',str("%.2f" %last_price_usd),"$"),
	('| Макc. курc: ',str("%.2f" %high_price_usd),"$"),
	('| Мин. курс: ',str("%.2f" %low_price_usd),"$"),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------ZEC/USD---------------------------
def get_zec_usd():
	url_usd = 'https://yobit.net/api/2/zec_usd/ticker'
	response_usd = requests.get(url_usd).json()
	last_price_usd = response_usd['ticker']['last']
	high_price_usd = response_usd['ticker']['high']
	low_price_usd = response_usd['ticker']['low']
	vivod=[
	('ZEC/USD:'),
	('| Последний курс: ',str("%.2f" %last_price_usd),"$"),
	('| Макc. курc: ',str("%.2f" %high_price_usd),"$"),
	('| Мин. курс: ',str("%.2f" %low_price_usd),"$"),
	('-------')]
	return "\n".join(map("\t".join,vivod))
#  ------------------------BCHABC/USD---------------------------
def get_bchabc_usd():
	url_usd = 'https://yobit.net/api/2/bchabc_usd/ticker'
	response_usd = requests.get(url_usd).json()
	last_price_usd = response_usd['ticker']['last']
	high_price_usd = response_usd['ticker']['high']
	low_price_usd = response_usd['ticker']['low']
	vivod=[
	('BCHABC/USD:'),
	('| Последний курс: ',str("%.2f" %last_price_usd),"$"),
	('| Макc. курc: ',str("%.2f" %high_price_usd),"$"),
	('| Мин. курс: ',str("%.2f" %low_price_usd),"$"),
	('-------')]
	return "\n".join(map("\t".join,vivod))