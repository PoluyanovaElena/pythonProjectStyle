from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = "7833663712:AAFr6YylIeIL8j5yh44CRcnnrA7rXjkW8HU"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


InlineKeyboardMarkup = InlineKeyboardMarkup()
InlineKeyboardButton1 = KeyboardButton('Рассчитать норму калорий', callback_data='calories')
InlineKeyboardButton2 = KeyboardButton('Формулы расчёта', callback_data='formulas')
InlineKeyboardMarkup.add(InlineKeyboardButton1, InlineKeyboardButton2)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=InlineKeyboardMarkup)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(f"для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;"
                              f"для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.")
    await call.answer


kb = ReplyKeyboardMarkup(resize_keyboard=True)
KeyboardButton1 = KeyboardButton(text="Рассчитать")
KeyboardButton2 = KeyboardButton(text="Информация")
kb.row(KeyboardButton1, KeyboardButton2)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет", reply_markup = kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(first=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(second=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(third=message.text)
    data = await state.get_data()
    await message.answer(f"Ваша норма калорий: "
                         f"{10 * int(data['third']) + 6.25 * int(data['second'])- 5 * int(data['first']) + 5}")
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)