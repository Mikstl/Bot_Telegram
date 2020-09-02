import requests
import misc
import json
from moi_kel import get_btc
from time import sleep 

token = misc.token

URL = 'https://api.telegram.org/bot' + token + '/'

global last_update_id
last_update_id = 0


def get_updates():
	url = URL + 'getUpdates'
	r = requests.get(url)
	return r.json()

def get_message():
	# Отвечать только на новые сообщения.
	data = get_updates()

	last_object = data['result'][-1]
	current_update_id = last_object['update_id']

	global last_update_id
	if last_update_id != current_update_id:
			last_update_id = current_update_id

			chat_id = last_object['message']['chat']['id']
			message_text = last_object['message']['text']

			message = {'chat_id':chat_id,
					   'text':message_text}
			return message
	return None

def send_message(chat_id, text="Подождите немного пожалуйста....",parse_mode= 'Markdown'):
	url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id,text)
	requests.get(url)

def main():

	while True:
		answer= get_message()
		url= 'https://yobit.net/api/2/eth_btc/ticker'
		response = requests.get(url).json()
		price = response['ticker']['last']
		new_high_price = response['ticker']['high']

		if answer != None:
			 chat_id = answer['chat_id']
			 text = answer['text']
			 if text == '/btc':
			 	send_message(chat_id,
			 	get_btc())
			 	
		if price >= new_high_price:
			tekst = "Курс поднялся. /n"+get_btc()
			send_message('531253663',tekst)
			sleep(10)

		else:
			continue

		

if __name__ == '__main__':
	main()