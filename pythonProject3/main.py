import telebot
from config import keys, TOKEN
from extensions import CryptoConverter, ConvertionExeption
import traceback
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(messege: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \n Увидеть список всех доступных валют: /values'
    bot.reply_to(messege, text)

@bot.message_handler(commands=['values'])
def values(messege: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(messege, text)


@bot.message_handler(content_types=['text'])
def get_prise(messege: telebot.types.Message):
    try:


        values = messege.text.split(' ')


        if len(values) != 3:
            raise ConvertionExeption('Слишком много параметров')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)


    except ConvertionExeption as e:
        bot.reply_to(messege, f'Ошибка пользоателя\n{e}')

    except Exception as e:
        bot.reply_to(messege, f'Не удалось обработать команду\n{e}')

    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(messege, f"Неизвестная ошибка:\n{e}")

    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'

        bot.send_message(messege.chat.id, text)

bot.polling()