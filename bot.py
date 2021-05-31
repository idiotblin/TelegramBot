import os
import telebot
import models
import random

from sqlalchemy.orm import scoped_session
from database import SessionLocal, engine
from models import Message

models.Base.metadata.create_all(bind=engine)

session = scoped_session(SessionLocal)
bot = telebot.TeleBot(os.environ['bot_token'])


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Darova chel. Prishly text ya tebe tozhe samoe otpravly. "
                                           "No est' 17% shans chto ti ya prishly tebe joke.")


@bot.message_handler(commands=['help'])
def help_user(message):
    bot.send_message(message.from_user.id, "Commands:\n"
                                           "/kolvo - kolichestovo soobsheniy kotorie ti prislal\n"
                                           "/history - pishesh etu komandu and chislo, chtobi poluchit' svoye n-noe soobshenie")


@bot.message_handler(commands=['kolvo'])
def kol(message):
    name = message.from_user.username
    ans = len(session.query(Message).filter_by(name=name).all())
    bot.reply_to(message, f"Ti prislal {ans} messages")


@bot.message_handler(commands=['history'])
def history(message):
    text = message.text.split(' ')
    if len(text) == 1:
        bot.send_message(message.from_user.id, 'Chislo ne napisal')
        return
    num = int(text[1])
    name = message.from_user.username
    res = session.query(Message).filter_by(name=name, num=num).first().text
    bot.send_message(message.from_user.id, f'Tvoyo {num} soobshenie:\n' + res)


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    name = message.from_user.username
    n = len(session.query(Message).filter_by(name=name).all())
    session.add(Message(name=name, num=n + 1, text=message.text))
    session.commit()
    rnd = random.randint(1, 100)
    if rnd < 18:
        bot.send_message(message.from_user.id, "Krasava, tebe povezlo, v podarok ti poluchaesh:")
        bol = False
        if rnd < 11:
            bol = True
            bot.send_message(message.from_user.id, "Anekdot!!11!1!!")
            joke = open(f'Anekdots/{str(rnd)}.txt', 'r', encoding='utf-8').read()
        elif rnd == 11:
            bot.send_message(message.from_user.id, "Anice or Nafice?")
            joke = open(f'Anekdots/aniceORnafice.jpg', 'rb').read()
        elif rnd == 12:
            bot.send_message(message.from_user.id, "Derzhim arsk")
            joke = open(f'Anekdots/arsk.jpg', 'rb').read()
        elif rnd == 13:
            bot.send_message(message.from_user.id, "Ti ne ti kogda goloden")
            joke = open(f'Anekdots/Karim.jpg', 'rb').read()
        elif rnd == 14:
            bot.send_message(message.from_user.id, "Kogda poshel obedat', a Ram za tebya otmetilsya")
            joke = open(f'Anekdots/arthur.jpg', 'rb').read()
        elif rnd == 15:
            bot.send_message(message.from_user.id, "Delu vremya - no kak nibud' potom")
            joke = open(f'Anekdots/haba.jpg', 'rb').read()
        elif rnd == 16:
            bot.send_message(message.from_user.id, "Lomau akk tvoey materi")
            joke = open(f'Anekdots/ram.jpg', 'rb').read()
        else:
            bot.send_message(message.from_user.id, "XGOD")
            joke = open(f'Anekdots/cam.jpg', 'rb').read()
        if not bol:
            bot.send_photo(message.from_user.id, joke)
        else:
            bot.send_message(message.from_user.id, joke)
    else:
        bot.reply_to(message, message.text)


bot.polling()
