from datetime import datetime
import schedule as schedule
import time
import AirtableParsing
import config
import telegram
import markup
bot = telegram.Bot(token=config.TOKEN)


def handler():
    try:
        records = AirtableParsing.getting_result_records()
        if records:
            for i in records:
                bot.send_message(chat_id=i[0], text=i[1], parse_mode="HTML")
    except Exception as exp:
        print("Failed at", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def main():
    schedule.every(2).to(3).minutes.do(handler)
    print("Running...")

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    main()


