from telegram.ext import Updater, CommandHandler

from character import create_character, inventory
from critical_variables import BotToken
from handlers import attack, start_quest


def main() -> None:
    updater = Updater(token=BotToken, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("create_character", create_character))
    dispatcher.add_handler(CommandHandler("start_quest", start_quest))
    dispatcher.add_handler(CommandHandler("attack", attack))
    dispatcher.add_handler(CommandHandler("inventory", inventory))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
