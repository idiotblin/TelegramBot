# README for Telegram Bot

## Overview

This is a simple Telegram bot built using the `telebot` library that interacts with users by responding to specific commands and echoes back messages received. The bot also has a built-in random joke feature that activates on certain conditions.

## Requirements

To run this bot, you'll need:

- Python 3.6 or higher
- Required Python packages:
  - `pyTelegramBotAPI` (telebot)
  - `SQLAlchemy`
  
You can install the required packages using pip:

```bash
pip install pyTelegramBotAPI sqlalchemy
```

## Database Setup

The bot uses SQLAlchemy to interact with a database where it stores the messages sent by users. Make sure to create the database and configure it according to your needs.

1. Create a database and ensure it's accessible by SQLAlchemy.
2. Set up your models in the `models.py` file as needed for message storage.

## Environment Variables

Before running the bot, make sure to set the `bot_token` environment variable with your Telegram bot token. This token can be obtained from [BotFather](https://t.me/botfather).

Set it in your environment like so:

```bash
export bot_token='YOUR_BOT_TOKEN'
```

## Usage

### Commands

- `/start`: Initializes the welcome message from the bot.
- `/help`: Lists the commands available to the user.
- `/kolvo`: Returns the number of messages sent by the user to the bot.
- `/history [number]`: Returns the text of the user's n-th message (where the number is specified).
  
### Message Handling

- The bot will also echo back any message sent to it unless a joke is triggered.
- Every user's message is stored in the database with a unique number assigned to it.

### Joke Feature

The bot has a joke feature that randomly triggers a joke under certain conditions (17% chance). If triggered, it may send a text joke or an image based on the random number generated.

## Running the Bot

To start the bot, run:

```bash
python your_bot_script.py
```

Replace `your_bot_script.py` with the name of your Python file containing the code.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides an overview, requirements, usage instructions, and guidance for running the Telegram bot. Be sure to adjust the content based on the specifics of your project!
