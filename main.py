import asyncio
import signal
import sys
from typing import Dict, Any, Callable

from bot.bot import TelegramBot


def handle_exit_signals(bot: TelegramBot) -> None:
    loop = asyncio.get_running_loop()
    
    def signal_handler() -> None:
        loop.create_task(bot.stop())
    
    for sig_name in ('SIGINT', 'SIGTERM'):
        loop.add_signal_handler(
            getattr(signal, sig_name),
            signal_handler
        )


async def main() -> None:
    bot = TelegramBot()
    
    try:
        handle_exit_signals(bot)
        await bot.start()
        
        while True:
            await asyncio.sleep(3600)
            
    except Exception as e:
        print(f"Ошибка: {e}")
        await bot.stop()
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен вручную") 