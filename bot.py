import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# TODO спрятать токен в гитигнор
TOKEN = "2028789368:AAGJaecJtmyQNu8wpd-zJyxnzpSz-SbPKh4"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_start(msg: types.Message):
    await msg.reply(text = (f'Я бот. Ты, {msg.from_user.full_name}'))

@dp.message_handler(commands=['help'])
async def send_help(msg: types.Message):
    await msg.reply(text=('ответ(реплай) на /help без цитирования'), reply=False)

@dp.message_handler(commands=['reg'])
async def registration(msg: types.Message):
    # ответ в личку
    # await bot.send_message(msg.from_user.id, text="Welcome to the club, buddy")
    
    # ответ реплаем
    await msg.reply(text=('Welcome to the club, buddy. Твой ник {0}, твой ID {1}').format(msg.from_user.full_name, msg.from_user.id), reply=False)


# @dp.message_handler(content_types=['text'])
# async def send_messages(msg: types.Message):
#     if msg.text.lower() == 'привет':
#         await msg.answer('Привет')
#     else:
#         await msg.answer('Напиши "Привет"')


def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()