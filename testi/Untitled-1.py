from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я Пайпер-помощница! Чем могу помочь?")

def test(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать, сэр! Чем я могу помочь сегодня?")

def handle_message(update, context):
    text = update.message.text

    # Словарь с вопросами и ответами
    qa_dict = {
        'привет': 'Привет! Как дела?',
        'как дела?': 'У меня всё хорошо, спасибо! А у вас?',
        'тестик': 'Тест прошел успешно',
        'кто ты?': 'Я бот-помощница Пайпер! Помогу вам с чем угодно и когда угодно!',
        'что ты умеешь?': 'Я могу отвечать на ваши вопросы и выполнять различные команды.',
        "кто ты": "Я бот-помощница Пайпер! Помогу вам с чем угодно и когда угодно!",
        "что ты умеешь?": "В разработке...",
        "владелец": "Телеграмы владельца - @Drrixs/@Professional_In_Kotlin"
        # Добавьте другие вопросы и ответы здесь
    }

    # Проверяем, есть ли вопрос в словаре
    if text.lower() in qa_dict:
        answer = qa_dict[text.lower()]
    else:
        answer = 'Извините, я не понимаю ваш вопрос.'

    # Отправляем ответ пользователю
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer)


    


def main():
    updater = Updater(token='6199605276:AAG2qs7yWfZelU6yyYIxyPTk-Qd4qMjduKg', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    test_handler = CommandHandler('test', test)
    message_handler = MessageHandler(Filters.text, handle_message)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(test_handler)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
