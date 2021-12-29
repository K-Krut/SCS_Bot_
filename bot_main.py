import AirtableParsing
import markup
from imports import bot, types, dp, executor


@dp.message_handler(commands=['start'])
async def send_welcome_message(message: types.Message):
    await message.delete()
    print(message.from_user.id)
    await bot.send_message(
        message.from_user.id, f"👤*Hi! {message.from_user.first_name if message.from_user.first_name else ''} "
                              f"{message.from_user.last_name if message.from_user.last_name else ''}\n "
                              f"I'm bot Assistant.*", parse_mode="HTML",
        reply_markup=markup.keyboard_
    )


@dp.callback_query_handler(text='TASKS_IN_PROGRESS')
async def this_month_statistic_handler(call: types.CallbackQuery):
    await call.message.delete()
    print('@dp.callback_query_handler(text=TASKS_IN_PROGRESS')
    try:
        await bot.send_message(
            call.from_user.id,
            '\n\n'.join([i for i in AirtableParsing.getting_data()]),
            parse_mode='HTML'
        )
    except Exception:
        return


executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

