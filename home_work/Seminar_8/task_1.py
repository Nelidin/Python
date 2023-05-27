# Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot
from telebot import types


bot = telebot.TeleBot("TOKEN") 

markup = types.ReplyKeyboardMarkup(row_width=2)
btn_start = types.KeyboardButton('/start')
btn_help = types.KeyboardButton('/help')
markup.add(btn_start, btn_help)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Привет! Я бот техподдержки.', reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, 'Задавайте свой вопрос.', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text_message(message):
    data = open('question.txt', mode='a', encoding='utf-8')
    text = f'{message.from_user.id} : {message.text}\n'
    data.write(text)
    data.close()

bot.polling()