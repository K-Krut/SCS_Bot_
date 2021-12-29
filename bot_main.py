import AirtableParsing
import markup
from imports import bot, types, dp, executor
#     "view": "KKrut In Progress"


@dp.message_handler(commands=['start'])
async def send_welcome_message(message: types.Message):
    await message.delete()
    await bot.send_message(
        message.from_user.id, f"👤*Hi! {message.from_user.first_name if message.from_user.first_name else ''} "
                              f"{message.from_user.last_name if message.from_user.last_name else ''}\n "
                              f"I'm bot Assistant.*", parse_mode="HTML",
        reply_markup=markup.keyboard_
    )


@dp.callback_query_handler(text='TASKS_IN_PROGRESS')
async def tasks_in_progress_handler(call: types.CallbackQuery):
    await call.message.delete()
    try:
        await bot.send_message(
            call.from_user.id,
            '\n\n'.join([i for i in AirtableParsing.getting_processed_data(call.from_user.id)]),
            parse_mode='HTML'
        )
    except Exception as exp:
        return


executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

