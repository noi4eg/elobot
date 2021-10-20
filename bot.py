import logging

from aiogram.types.reply_keyboard import KeyboardButton, ReplyKeyboardMarkup
import crud
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# TODO спрятать токен в гитигнор
TOKEN = "2028789368:AAFATx6X4WgQpUP5n6d3MjoDao1h87eyLNE"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# mainmenu
btnReg = KeyboardButton('Регистрация участника')
btnLeaders = KeyboardButton('Доска участников')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnReg, btnLeaders)


@dp.message_handler(commands=['start'])
async def send_start(msg: types.Message):
    await msg.reply(text=(f'Я бот. Ты, {msg.from_user.full_name}'), reply_markup=mainMenu)


@dp.message_handler(commands=['help'])
async def send_help(msg: types.Message):
    await msg.reply(text=('ответ(реплай) на /help без цитирования'), reply=False)


@dp.message_handler(commands=['reg'])
async def registration(msg: types.Message):
    # ответ в личку
    # await bot.send_message(msg.from_user.id, text="Welcome to the club, buddy")

    # ответ реплаем
    await msg.reply(text=('Welcome to the club, buddy.\nТвой ник {0}, твой ID {1}').format(msg.from_user.full_name,
                                                                                          msg.from_user.id),
                    reply=False)


@dp.message_handler(commands=['elo'])
async def send_elo(msg: types.Message):
    await msg.reply(text=crud.leaderbords(), reply=False)


@dp.message_handler(content_types=['text'])
async def send_messages(msg: types.Message):
    if msg.text.lower() == 'регистрация участника':
        if crud.add_user(str(msg.from_user.id), msg.from_user.full_name) == True:
            await msg.reply(text="Вы зарегестированы")
        elif crud.add_user(str(msg.from_user.id), msg.from_user.full_name) == False:
            await msg.reply(text="Пользователь уже зарегистрирован")
    elif msg.text.lower() == 'доска участников':
        await msg.reply(text=crud.leaderbords(), reply=False)



def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
