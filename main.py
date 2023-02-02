import telebot
import openai
from dotenv import load_dotenv
import os
from datetime import datetime


load_dotenv()


wl_path = './witelist.txt'

lf_path = './log.txt'


wite_list = []

bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
openai.api_key = os.environ['OAI_TOKEN']


def to_log(level: str, message: str):
    log_file = open(lf_path, 'a')
    log_file.write(f'[{datetime.now()}]  [{level}]  [{message}] \n')
    log_file.close()


def to_log_info(message: str):
    to_log('INFO', message)


def to_log_war(message: str):
    to_log('WARNING', message)


def to_log_err(message: str):
    to_log('ERROR', message)


def load_wite_list(wlf: str):
    f = open(wlf, 'r')
    for line in f:
        wite_list.append(line.replace('\n', ''))
    f.close()


def chek_user_id(user_id):
    if str(user_id) in wite_list:
        return True
    else:
        return False


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi, Im "GPT Chat", lets get started')


@bot.message_handler(content_types=['text'])
def send_text(message):
    uerr_id = message.from_user.id

    answer = "Sorry, you are denied access"

    if chek_user_id(uerr_id):
        to_log_info('question')
        to_log_info(message.text)

        response = openai.Completion.create(
            model='text-davinci-003',
            prompt=message.text,
            temperature=0,
            max_tokens=3048,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None
            # stop=["\n"]
        )

        answer = response.choices[0].text
        to_log_info('answer')
        to_log_info(answer)
    else:
        to_log_war(f'{uerr_id}: is not in access list')

    bot.send_message(message.chat.id, f'{answer}')


if __name__ == '__main__':
    load_wite_list(wl_path)
    bot.polling()