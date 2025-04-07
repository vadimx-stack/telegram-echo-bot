from telegram import Update
from telegram.ext import ContextTypes


async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text) 