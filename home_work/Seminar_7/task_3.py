# Добавьте в telegram-бота игру «Угадай числа». Бот загадывает число от 1 до 1000. 
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot, random
from telebot import types


bot = telebot.TeleBot("TOKEN")

markup = types.ReplyKeyboardMarkup(row_width=2)
btn_start = types.KeyboardButton('/start')
btn_help = types.KeyboardButton('/help')
btn_games = types.KeyboardButton('/new_game')

markup.add(btn_start, btn_help, btn_games)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.from_user.id, 'Привет! Я бот "Угадай число.".\n' + 
                    'Давай поиграем?!', reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.send_message(message.from_user.id, 'Я бот "Угадай число". Я загадываю число от 1 до 1000, а тебе нужно его угадать.')


@bot.message_handler(commands=['new_game'])
def newgame(message):    
    global HiddenNumber
    global UserNumber
    HiddenNumber = random.randint(1, 1000)
    print(message.text)
    print(HiddenNumber)    
    message = bot.send_message(message.chat.id, 'Введи число от 1 до 1000:')
    bot.register_next_step_handler(message, GuessNumber)

def GuessNumber(message):
    text = message.text
    # count = 1
    if text != HiddenNumber:           
        print(message.text)             
        user_num = int(message.text)
        # count +=1   
        if user_num < HiddenNumber:                   
            message = bot.send_message(message.chat.id, 'Число должно быть больше!')
            bot.register_next_step_handler(message, GuessNumber)               
        elif user_num > HiddenNumber:               
            message = bot.send_message(message.chat.id, 'Число должно быть меньше!')
            bot.register_next_step_handler(message, GuessNumber)           
        else:            
            bot.send_message(message.chat.id, 'Ты угадал, это число: ' + str(HiddenNumber))
            # bot.send_message(message.chat.id, f'Количество твоих попыток: {count}\nСпасибо за игру!')
            bot.send_message(message.chat.id, 'Начать новую игру: /new_game' )    
    # count +=1   

@bot.message_handler(content_types=['text'])
def greetings(message):
	text = message.text
	if 'привет' in text:
		bot.reply_to(message, f'Привет, {message.from_user.first_name}', reply_markup=markup)

bot.polling()