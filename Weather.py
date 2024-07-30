# подключаем модуль для Телеграмма
import telebot
# подключаем библиотеку для работы с запросами
import requests
# для обработки json-объектов
import json

bot = telebot.TeleBot("12345678:ПАОПАЫПОлавлмсчидмсДМВЫДЛсалвмлЛЛаывпд")
API = '684569шЛПдлВлпЛОП9435ь'

# приветственный текст
start_txt = ('Привет! Это бот прогноза погоды. '
             '\n\nОтправьте боту название города и он скажет, '
             'какая там температура.')

# обрабатываем старт бота
@bot.message_handler(commands=['start'])
def start(message):
    # выводим приветственное сообщение
    bot.send_message(message.chat.id, start_txt)

# обрабатываем любой текстовый запрос
@bot.message_handler(content_types=['text'])
def weather(message):
    # получаем город из сообщения пользователя
    city = message.text.strip().lower()
    # формируем запрос
    # отправляем запрос на сервер и сразу получаем результат
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={API}')
    # проверяем корректность запроса
    if res.status_code == 200:
        data = json.loads(res.text)
        # получаем данные о температуре
        temp = data["main"]["temp"]
        # формируем ответы и отправляем значения пользователю
        bot.reply_to(message, f'Сейчас в городе {city}: {temp}')
    else:
        bot.reply_to(message, 'Город указан неверно, попробуйте еще раз')

# опрашиваем бота — есть ли новые сообщения
bot.polling(none_stop=True)
