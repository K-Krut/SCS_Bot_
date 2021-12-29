from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup
import config
import logging
from datetime import datetime, timedelta as tmd
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
import markup

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
