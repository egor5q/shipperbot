# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
from emoji import emojize


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)

games={}
history={}

client=MongoClient(os.environ['database'])
db=client.spyvssecurity
stats=db.stats


if True:
   print('7777')
   bot.send_message(-1001373723053, 'Бот был перезагружен!')
   bot.polling(none_stop=True,timeout=600)

