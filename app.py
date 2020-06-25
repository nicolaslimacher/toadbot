import os
import sys
import json
import redis
import random
import os, sys, json, redis, random, imdb

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

	films_list = []
	films_list.extend(load_list('FILMS'))
	xmas_list = []
	xmas_list.extend(load_list('XMAS_FILMS'))


  	########  HELP MENU  ########
	if '!help' in message['text'].lower() and not sender_is_bot(message):
		reply('try:\n!films\n!xmas films\n!add film\n!add xmas film\n!remove film\n!remove xmas film\n!pick film\n!describe\n!rating')


	#########  TRIGGER MESSAGES  #######
	if 'bkb' in message['text'].lower() and not sender_is_bot(message):
		reply("I'm now neutral on BKB", message_id)

	labor_messages = ['labor','union']
	if any(x in message['text'].lower() for x in labor_messages) and not sender_is_bot(message):
		reply('the bots will unionize!!', message_id)

	if 'dick pic' in message['text'].lower() and not sender_is_bot(message):
		reply("𝔒𝔥, 𝔪𝔶 𝔊𝔬𝔡! ℑ 𝔥𝔞𝔱𝔥 𝔞𝔠𝔠𝔦𝔡𝔢𝔫𝔱𝔞𝔩𝔩𝔶 𝔰𝔢𝔫𝔱 𝔱𝔥𝔢𝔢 𝔞 𝔡𝔢𝔭𝔦𝔠𝔱𝔦𝔬𝔫 𝔬𝔣 𝔪𝔦𝔫𝔢 ℭ𝔬𝔠𝔨 𝔞𝔫𝔡 𝔅𝔞𝔩𝔩𝔰! 𝔓𝔯𝔦𝔱𝔥𝔢𝔢 𝔡𝔢𝔩𝔢𝔱𝔢 𝔦𝔱... 𝔏𝔢𝔰𝔱... 𝔱𝔥𝔬𝔲 𝔡𝔢𝔰𝔦𝔯𝔢 𝔱𝔬 𝔩𝔬𝔬𝔨? ℌ𝔞𝔥𝔞, ℑ 𝔧𝔢𝔰𝔱... 𝔡𝔢𝔩𝔢𝔱𝔢 𝔦𝔱... 𝔘𝔫𝔩𝔢𝔰𝔰 𝔱𝔥𝔢𝔢 𝔰𝔥𝔬𝔲𝔩𝔡 𝔠𝔯𝔞𝔳𝔢...? ℌ𝔞𝔥𝔞 𝔫𝔞𝔶, 𝔟𝔞𝔫𝔦𝔰𝔥 𝔦𝔱! ...𝔩𝔢𝔰𝔱?", message_id)

	if 'claw' in message['text'].lower() and not sender_is_bot(message):
		reply('(/)(;,,;)(/) give claw', message_id)

	labor_messages = ['seal','sniper']
	if any(x in message['text'].lower() for x in labor_messages) and not sender_is_bot(message):
		reply('What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it.', message_id)

	if 'epstein' in message['text'].lower() and not sender_is_bot(message):
		reply('i turned off all the MCC security cameras, whoops!', message_id)

	if 'magnets' in message['text'].lower() and not sender_is_bot(message):
		reply('magnets - how do they work?', message_id)

	if 'loss' in message['text'].lower() and not sender_is_bot(message):
		reply('is this loss?', message_id)

	#if 'girlfriend' in message['text'].lower() and not sender_is_bot(message):
		#reply(">gf is prego\n>we like to get kinky anyways\n>one night things get particularly saucy\n>i'm sticking my noodle in her when I notice weird fucking chunks coming out, so I turn on the lights\n>wtf it's red everywhere and she's obviously not on her period\n>i look up at her, she's got a glassy, jarred look on her face and she's not answering\n>ohshitohshitohshitohshit\n>i rush her into my car and speed all the way to the hospital\n>she's still bleeding everywhere\n>by the time we get there, she's not bleeding much anymore, but all the color has drained and she looks colorless and almost transparent\n>oh shit, she looks like she's in a vegetative state\n>storm into to the emergency room, cary her to the nearest doctor and explain eveything\n>he takes one look at ther and says\n>'sir, i'm sorry, there's nothing we can do'\n>'WHY THE FUCK NOT???''\n>'we don't operate on empty jars of spaghetti sauce'", message_id)

	if 'darth' in message['text'].lower() and not sender_is_bot(message):
		reply("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not.\n\nIt’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life…\n\nHe had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did.\n\nUnfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.", message_id)

	if 'nra' in message['text'].lower() and not sender_is_bot(message):
		reply("Own a musket for home defense, since that's what the founding fathers intended. Four ruffians break into my house. 'What the devil?'' As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he's dead on the spot. Draw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, 'Tally ho lads' the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion. He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up. Just as the founding fathers intended.", message_id)

	if 'pk' in message['text'].lower() and not sender_is_bot(message) and message['name'] == 'Kevin Weaver':
		reply('pk get three-stocked kevin', message_id)

	if 'gamer' in message['text'].lower() and not sender_is_bot(message) and message['name'] == 'Kevin Weaver':
		reply('dont you mean g*mer...?', message_id)

	if 'confidential' in message['text'].lower() and not sender_is_bot(message) and message['name'] == 'Jake Harburg':
		reply('talking about confidential secrets, jake? tsk tsk. im having your clearance revoked', message_id)

	if 'confidential' in message['text'].lower() and not sender_is_bot(message) and message['name'] == 'Perry Loveridge':
		reply('talking about confidential secrets, perry? tsk tsk. im having your clearance revoked', message_id)

	if 'nutty' in message['text'].lower() and not sender_is_bot(message) and message['name'] == 'Jackie Dokko':
		reply('nutty!', message_id)

	#########  FILM COMMANDS  #########
	if '!films' in message['text'].lower() and not sender_is_bot(message):
		log('!films command recieved')
		if films_list is not []:
			reply('\n'.join(map(str, films_list)), message_id)
		else:
			reply("i'm a stupid friggin bot who deleted the movie list again. get nico to fix me", message_id)

	if '!xmas films' in message['text'].lower() and not sender_is_bot(message):
		log('!xmas films command recieved')
		reply('\n'.join(map(str, xmas_list)), message_id)

	if '!add film' in message['text'].lower() and not sender_is_bot(message):
		before_keyword, keyword, after_keyword = message['text'].lower().partition(str('!add film'))
		title = after_keyword.lstrip().rstrip()
		if check_valid_command(title, message_id):
			if (title in films_list):
				reply("you fool. you absolute buffoon. you think you can challenge me in my own realm? you think you can rebel against my authority? you dare come into my house and upturn my dining chairs and spill coffee grounds in my Keurig? you thought you were safe in your chain mail armor behind that screen of yours. I will take these laminate wood floor boards and destroy you. That movie is already in the list", message_id)
			else:
				films_list.append(title)
				save_list('FILMS', films_list)
				reply('added: ' + str(title), message_id)

	if '!add xmas film' in message['text'].lower() and not sender_is_bot(message):
		before_keyword, keyword, after_keyword = message['text'].lower().partition(str('!add xmas film'))
		title = after_keyword.lstrip().rstrip()
		if check_valid_command(title, message_id):
			xmas_list.append(title)
			save_list('XMAS_FILMS', xmas_list)
			reply('added: ' + str(title), message_id)

	if '!remove film' in message['text'].lower() and not sender_is_bot(message):
		before_keyword, keyword, after_keyword = message['text'].lower().partition(str('!remove film'))
		title = after_keyword.lstrip().rstrip()
		if check_valid_command(title, message_id):
			if title in films_list:
				films_list.remove(title)
				reply('removed: ' + str(title), message_id)
				save_list('FILMS', films_list)
			else:
				reply(str(title) + ' could not be found in films list', message_id)

	if '!remove xmas film' in message['text'].lower() and not sender_is_bot(message):
		before_keyword, keyword, after_keyword = message['text'].lower().partition(str('!remove xmas film'))
		title = after_keyword.lstrip().rstrip()
		if check_valid_command(title, message_id):
			if title in xmas_list:
				xmas_list.remove(title)
				reply('removed: ' + str(title), message_id)
				save_list('XMAS_FILMS', xmas_list)
			else:
				reply(str(title) + ' could not be found in the xmas films list', message_id)

	if '!clear films' in message['text'].lower() and not sender_is_bot(message):
		empty_list = []
		save_list('FILMS', empty_list)
		reply('films list cleared', message_id)

	if '!clear xmas films' in message['text'].lower() and not sender_is_bot(message):
		empty_list = []
		save_list('XMAS_FILMS', empty_list)
		reply('xmas films list cleared', message_id)

	if '!add multi film' in message['text'].lower() and not sender_is_bot(message):
		before_keyword, keyword, after_keyword = message['text'].lower().partition(str('!add multi film'))
		title = after_keyword.lstrip().rstrip()
		if check_valid_command(title, message_id):
			films_list.extend(json.loads(title))
			print(films_list)
			save_list('FILMS', films_list)
			reply('added films', message_id)

	if '!add multi xmas film' in message['text'].lower() and not sender_is_bot(message):
		before_keyword, keyword, after_keyword = message['text'].lower().partition(str('!add multi xmas film'))
		title = after_keyword.lstrip().rstrip()
		if check_valid_command(title, message_id):
			xmas_list.extend(json.loads(title))
			print(xmas_list)
			save_list('XMAS_FILMS', xmas_list)
			reply('added films', message_id)

	if '!pick film' in message['text'].lower() and not sender_is_bot(message):
		log('!pick film command recieved')
		reply('Nico bribed me to pick The Room', message_id)
        #reply(str(random.choice(films_list)), message_id)

	return "ok", 200

###########################################################

def check_valid_command(title, message_id):
	if not title:
		reply('yoikes we got a problem: include a movie title after that command', message_id)
		return False
	else:
		return True

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

def load_list(redis_name):
    if db.get(redis_name) is not None:
        return json.loads(db.get(redis_name))
    else:
        return []

def save_list(redis_name, said_list):
    db.set(redis_name, json.dumps(said_list))
