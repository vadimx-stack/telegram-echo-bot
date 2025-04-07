from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot.handlers.command_handlers import start_command, help_command
from bot.handlers.message_handlers import echo_message
from bot.utils.config import load_config
from bot.utils.logger import setup_logger


class TelegramBot:
    def __init__(self):
        self.logger = setup_logger()
        self.token = load_config()
        self.application = Application.builder().token(self.token).build()
        
        self.register_handlers()
        
    def register_handlers(self) -> None:
        self.application.add_handler(CommandHandler("start", start_command))
        self.application.add_handler(CommandHandler("help", help_command))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))
        
        self.logger.info("Обработчики команд и сообщений зарегистрированы")
        
    async def start(self) -> None:
        self.logger.info("Запуск бота...")
        await self.application.initialize()
        await self.application.start()
        await self.application.updater.start_polling()
        self.logger.info("Бот запущен")
        
    async def stop(self) -> None:
        self.logger.info("Остановка бота...")
        await self.application.updater.stop()
        await self.application.stop()
        await self.application.shutdown()
        self.logger.info("Бот остановлен") 