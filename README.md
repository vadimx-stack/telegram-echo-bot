# 🤖 Professional Telegram Bot

[![English](https://img.shields.io/badge/Language-English-blue)](README.md)
[![Russian](https://img.shields.io/badge/Language-Russian-green)](README.ru.md)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-v20%2B-green)

A professional, scalable, and clean Telegram bot project using a modern asynchronous approach in Python. This project demonstrates best practices for Telegram bot development and can serve as a foundation for creating more complex bots.

## ✨ Features

- ⚡ Asynchronous architecture using `python-telegram-bot` v20+
- 🧩 Modular project structure, ready for extension
- 🔐 Environment variable support via `.env` for bot token storage
- 📝 Full typing with Python type annotations
- 🛡️ Built-in logging system with file and console output
- 🔄 Proper termination signal handling

## 📋 Bot Commands

- `/start` - Initial greeting and bot information
- `/help` - List of available commands and instructions
- Echo responses to all text messages

## 🚀 Installation and Launch

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Project Setup

1. Clone the repository:
```bash
git clone https://github.com/username/telegram-bot-framework.git
cd telegram-bot-framework
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

5. Edit the `.env` file and add your bot token:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### Running the Bot

```bash
python main.py
```

## 🏗️ Project Structure

```
telegram-bot-framework/
├── bot/
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── command_handlers.py    # Command handlers (/start, /help)
│   │   └── message_handlers.py    # Message handlers (echo)
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py              # Loading configuration from .env
│   │   └── logger.py              # Logging setup
│   ├── __init__.py
│   └── bot.py                     # Main bot class
├── logs/                          # Log directory (created automatically)
├── .env                           # Environment variables file (not included in repo)
├── .env.example                   # Example environment variables file
├── .gitignore                     # Files and directories excluded from the repo
├── main.py                        # Application entry point
├── README.md                      # Project documentation (English)
├── README.ru.md                   # Project documentation (Russian)
└── requirements.txt               # Project dependencies
```

## 🛠️ Extending Functionality

The project has a modular structure that simplifies extending its functionality:

1. Add new command handlers in `bot/handlers/command_handlers.py`
2. Add handlers for new message types in `bot/handlers/message_handlers.py`
3. Register new handlers in the `register_handlers()` method of the `TelegramBot` class

## 📄 License

This project is distributed under the MIT license. See the LICENSE file for details.

## 📬 Contact

If you have any questions or suggestions, feel free to create an issue or pull request.

---

⭐ **Don't forget to star the project if you liked it!** ⭐ 