import os
import telebot
import models

from sqlalchemy.orm import scoped_session
from database import SessionLocal, engine
from models import Message

models.Base.metadata.create_all(bind=engine)

session = scoped_session(SessionLocal)
bot = telebot.TeleBot(os.environ['bot_token'])


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Darova chel. Prishly text ya tebe tozhe samoe otpravly")


@bot.message_handler(commands=['kolvo'])
def kol(message):
    name = message.from_user.username
    ans = len(session.query(Message).filter_by(name=name).all())
    bot.reply_to(message, f"Ti prislal {ans} messages")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    name = message.from_user.username
    session.add(Message(name=name, text=message.text))
    session.commit()
    bot.reply_to(message, message.text)


bot.polling()
