import os, sys, json, redis, random

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

app = Flask(__name__)

db=redis.from_url(os.environ['REDIS_URL'])
bot_id = os.getenv('BOT_ID')
test_bot_id = os.getenv('TEST_BOT_ID')

@app.route('/', methods=['POST'])
def webhook():

	message = request.get_json()
	if message['group_id'] == '51705871':
		message_id = test_bot_id
	else:
		message_id = bot_id
	log('Recieved: {}'.format(message))
	log('group_id: {}'.format(message['group_id']))
	log('message_id: {}'.format(message_id))

	return "ok", 200

###########################################################

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def reply(text_of_message, id):
	allowedLength = 1000
	for message in chunkstring(text_of_message, allowedLength):
		send_string_message(message, id)

def send_string_message(text_of_message, id):
	url  = 'https://api.groupme.com/v3/bots/post'
	data = {
		'bot_id' : id,
		'text'   : str(text_of_message),
		}
	request = Request(url, urlencode(data).encode())
	json = urlopen(request).read().decode()

# Checks whether the message sender is a bot
def sender_is_bot(message):
	return message['sender_type'] == "bot"

def log(msg):
	print(str(msg))
	sys.stdout.flush()