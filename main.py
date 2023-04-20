from aiogram.utils import executor
from config import dp, bot, ADMINS
from handlers import fsmAdminMentor
from database.bot_db import sql_create
import logging

async def on_startup(_):
    await bot.send_message(ADMINS[0], 'Я родился')
    sql_create()

fsmAdminMentor.register_handlers_fsm_anketa(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)