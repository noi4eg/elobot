from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# TODO спрятать токен в гитигнор
TOKEN = "2028789368:AAGJaecJtmyQNu8wpd-zJyxnzpSz-SbPKh4"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_start(msg: types.Message):
    await msg.reply(text = (f'Я бот. Ты, {msg.from_user.full_name}'))

@dp.message_handler(commands=['help'])
async def send_help(msg: types.Message):
    await msg.reply(text=('ответ на /help без цитирования'), reply=False)

@dp.message_handler(content_types=['text'])
async def send_messages(msg: types.Message):
    if msg.text.lower() == 'привет':
        await msg.answer('Привет')
    else:
        await msg.answer('Напиши "Привет"')

if __name__ == '__main__':
    executor.start_polling(dp)