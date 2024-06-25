from telegram import Update
from telegram.ext import CallbackContext
import random


def start_quest(update: Update, context: CallbackContext) -> None:
    character = context.user_data.get('character')
    if not character:
        update.message.reply_text("Сначала создайте персонажа с помощью /create_character")
        return

    quest = "Спасти деревню от бандитов"
    character['quests'].append(quest)
    update.message.reply_text(f"Квест начат: {quest}")

def attack(update: Update, context: CallbackContext) -> None:
    character = context.user_data.get('character')
    if not character:
        update.message.reply_text("Сначала создайте персонажа с помощью /create_character")
        return

    monster_hp = random.randint(50, 150)
    damage = random.randint(10, 50)
    character['hp'] -= damage
    if character['hp'] <= 0:
        update.message.reply_text("Вы погибли в бою с монстром!")
        character['hp'] = 100  # Восстанавливаем HP для простоты
    else:
        update.message.reply_text(f"Вы атаковали монстра и нанесли {damage} урона! У вас осталось {character['hp']} HP")
