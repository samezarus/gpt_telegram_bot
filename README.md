# gpt_telegram_bot

Hello everyone, this project is for quickly getting started with GPT-chat (openai.com).

ENV-params:
    
    BOT_TOKEN - telegram bot token (create with "https://t.me/BotFather")
    OAI_TOKEN - token from openai.com (create in profile)

Access list:
    
    Add to file user-id's for access to bot (each id from a new line)

    User-id can be found in "https://t.me/getmyid_bot"

Launch options:
    
    DEV:
        install: requirements.txt
        run: in project folder "python main.py"

    PROD:
        install: docker and docker-compose
        install: make
        run: in project folder "make up"