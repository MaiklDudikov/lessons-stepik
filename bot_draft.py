import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
import openai

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего Telegram бота
telegram_bot_token = "your_token_telegram"


# Замените 'YOUR_OPENAI_API_KEY' на ваш ключ API от OpenAI
openai_api_key = "your_api_key_openai"

# Инициализация Telegram бота
bot = telegram.Bot(token=telegram_bot_token)


# Функция для отправки сообщения ChatGPT и получения ответа
def ask_gpt3(text):
    openai.api_key = openai_api_key
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=50  # Максимальная длина ответа от ChatGPT
    )
    return response.choices[0].text.strip()


# Обработчик команды /start
def start(update, context):
    update.message.reply_text("Привет! Я готов отвечать на ваши вопросы. Просто напишите мне что-нибудь.")


# Обработчик входящих текстовых сообщений
def text_message(update, context):
    user_input = update.message.text
    response = ask_gpt3(user_input)  # Получение ответа от ChatGPT
    update.message.reply_text(response)


def main():
    # Инициализация Updater и диспетчера
    updater = Updater(token=telegram_bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Обработчики команд и сообщений
    start_handler = CommandHandler('start', start)
    text_message_handler = MessageHandler(Filters.text & ~Filters.command, text_message)

    # Регистрация обработчиков
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(text_message_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
