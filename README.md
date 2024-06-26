# Description
This project is about using Google AI in Telegram bot.\
The bot takes question from a user and redirects it to neural network.\
After that the bot takes the answer from the network and issues it to the user.

# Main components
| Module        | Description            |
|---------------|------------------------|
| Python 3.10   | - the base programming language |
| Poetry 1.6.1  | - virtual environment handling |
|Google-generativeai 0.3.2| - neural network engine|
|Telebot 0.0.5| - Telegram bot module  |

# Files and folders
| File (folder)  | Description                              |
|----------------|------------------------------------------|
| poetry         | - poetry files for virtual environment   |
| poetry.lock    | - all the installed packages description |
| pyproject.toml | - all the project poetry data            |
| geminitrial    | - project logic files                    |
| bot.py         | - Telegram bot logic                     |
| models.py      | - The AI model's settings                |
| views.py       | - the project logic                      |
