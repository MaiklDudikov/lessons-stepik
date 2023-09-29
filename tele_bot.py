import telebot
import openai
import time

telegram_token = 'your_token_telegram'
openai.api_key = 'your_api_key_openai'
admin_id = 111111111
users = [111111111, 22222222]

bot = telebot.TeleBot(telegram_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот на основе искуственного интелекта chatGPT, "
                                      "готовый помочь Вам. Просто напишите мне что-нибудь!")


@bot.message_handler(commands=['send'])
def send(message):
    if message.chat.id == admin_id:
        bot.send_message(message.chat.id, "Рассылка началась!")
        for i in users:
            bot.send_message(i, message.text[message.text.find(' '):])
        bot.send_message(message.chat.id, "Закончилась!")
    else:
        bot.send_message(message.chat.id, "Ошибка!")


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    user_input = message.text
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    print(user_name, user_id, user_input)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=1000  # Максимальная длина ответа от ChatGPT
    )

    bot.send_message(message.chat.id, response.choices[0].text)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Error: {str(e)}")
            time.sleep(10)
