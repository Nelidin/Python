#  Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него 
#                     и отправлять ответ обратно пользователю.

import telebot

bot = telebot.TeleBot("TOKEN") 

question = '1481736055 : Чем занимаешься?'.split(':')
answer = 'Отвечаю на вопросы.'
bot.send_message(question[0], f'Ваш вопрос: {question[1]}')
bot.send_message(question[0], f'Ответ: {answer}')