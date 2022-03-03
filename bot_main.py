from datetime import datetime
import schedule as schedule
import time
import AirtableParsing
import telegram
from config import TOKEN

bot = telegram.Bot(token=TOKEN)


def handler():
    try:
        records = AirtableParsing.getting_result_records()
        if records:
            for i in records:
                bot.send_message(chat_id=i[0], text=i[1], parse_mode="HTML")
    except Exception as exp:
        print("Failed at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '\n', exp)


def main():
    schedule.every(2).to(3).minutes.do(handler)
    print("Running...")

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()

#
# @dp.message_handler(commands=['start'])
# async def send_welcome_message(message: types.Message):
#     await message.delete()
#     await bot.send_message(
#         message.from_user.id, f"👤*Hi! {message.from_user.first_name if message.from_user.first_name else ''} "
#                               f"{message.from_user.last_name if message.from_user.last_name else ''}\n "
#                               f"I'm bot Assistant.*", parse_mode="HTML",
#         reply_markup=markup.keyboard_
#     )
#
#
# @dp.callback_query_handler(text='TASKS_IN_PROGRESS')
# async def tasks_in_progress_handler(call: types.CallbackQuery):
#     await call.message.delete()
#     try:
#         await bot.send_message(
#             call.from_user.id,
#             '\n\n'.join([i for i in AirtableParsing.getting_processed_data(call.from_user.id)]),
#             parse_mode='HTML'
#         )
#     except Exception as exp:
#         return
