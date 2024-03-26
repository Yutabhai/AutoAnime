import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get(23902408)) #API ID
API_HASH = environ.get('API_HASH', '6a36a4ef2f07d63aeba7b53b99c64d73') #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', '7190718780:AAEoMKzvj9Mb16iipToTw8uuwCrhkth0yYY') #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', 'mongodb+srv://pietar19sc:A0jqNJO96p3MQfOg@cluster0.467yujo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0') #MONGO DB
OWNER_ID = int(environ.get(7179837246)) #OWNER ID
MAIN_CHANNEL = int(environ.get(-1001951273334))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get(-1001692585152))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get(-1002059315034)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
