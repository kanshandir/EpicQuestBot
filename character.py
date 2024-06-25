from telegram import Update
from telegram.ext import CallbackContext


def create_character(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    character = {
        'name': user.first_name,
        'level': 1,
        'hp': 100,
        'inventory': [],
        'quests': []
    }
    context.user_data['character'] = character
    update.message.reply_text(f"Персонаж {user.first_name} создан!")


def inventory(update: Update, context: CallbackContext) -> None:
    character = context.user_data.get('character')
    if not character:
        update.message.reply_text("Сначала создайте персонажа с помощью /create_character")
        return

    inventory_list = "\n".join(character['inventory']) if character['inventory'] else "Ваш инвентарь пуст."
    update.message.reply_text(f"Ваш инвентарь:\n{inventory_list}")

