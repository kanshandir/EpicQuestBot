from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler

from character import create_character, inventory
from critical_variables import BotToken
from handlers import attack, start_quest


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_text(f"Привет, {user.first_name}! Выберите действие:", reply_markup=get_keyboard())


# Function to handle unknown commands or messages
def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Извините, не понимаю ваш запрос. Пожалуйста, используйте кнопки.")


# Function to create and return custom keyboard markup
def get_keyboard():
    keyboard = [
        ["/start", "/create_character"],
        ["/inventory", "/start_quest"]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)


def main() -> None:
    updater = Updater(token=BotToken, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler("create_character", create_character))
    dispatcher.add_handler(CommandHandler("start_quest", start_quest))
    dispatcher.add_handler(CommandHandler("attack", attack))
    dispatcher.add_handler(CommandHandler("inventory", inventory))

    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
