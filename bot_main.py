from datetime import datetime
import schedule
import time
import telegram
from aiogram.types import ParseMode
import AirtableParsing
from config import TOKEN


bot = telegram.Bot(token=TOKEN)


def handler():

    try:
        print('handler')
        records = AirtableParsing.getting_result_records()
        if records:
            for i in records:
                if i[2]:
                    bot.send_photo(
                        chat_id=i[0], photo=i[2], caption=i[1], parse_mode=ParseMode.HTML, disable_notification=True
                    )
                else:
                    bot.send_message(chat_id=i[0], text=i[1], parse_mode=ParseMode.HTML, disable_notification=True)

    except Exception as exp:
        print("Failed at ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '\n', exp)


def main():
    schedule.every(0).to(1).minutes.do(handler)
    print("Running...")

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()


