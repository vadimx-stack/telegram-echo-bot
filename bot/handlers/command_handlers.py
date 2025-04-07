from telegram import Update
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я телеграм бот, созданный для демонстрации профессиональной разработки. "
        "Используйте /help для получения справки."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "Доступные команды:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Показать это сообщение\n\n"
        "Вы также можете отправить мне любое сообщение, и я его повторю."
    )
    await update.message.reply_text(help_text) 