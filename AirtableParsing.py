import json
import airtable
from exceptions import SearchUser
from config import BASE_ID, API_KEY
from Constants import TABLE
from Constants import TASKS_IN_PROGRESS_FORMULA, FIELDS


Data_ = airtable.Airtable(BASE_ID, API_KEY)


def get_user_view(user_id):
    data = json.load(open('Creators.json'))
    if not str(user_id) in data:
        raise SearchUser(user_id)
    print(data[str(user_id)]['view'])
    return data[str(user_id)]['view']


def get_view_data(user_id):
    return Data_.iterate(
        table_name=TABLE, view=get_user_view(user_id), fields=FIELDS,
        # filter_by_formula=TASKS_IN_PROGRESS_FORMULA,
    )


def processing(data):
    print(data)
    return f'<b><i>{data["Name"].split(" | ")[0]}</i></b>\n' \
           f'Status: {data["Status"].replace("u200d", "")}\n' \
           f'Brand: {data["Brand"][0]}'


def getting_processed_data(user_id):
    print([processing(i.get('fields')) for i in get_view_data(user_id)])
    return [processing(i.get('fields')) for i in get_view_data(user_id)]

