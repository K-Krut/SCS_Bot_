import json
from datetime import datetime
from functools import reduce
from operator import or_
from urllib.parse import urlparse

import airtable
import re
from exceptions import SearchUser
from config import BASE_ID, API_KEY
from Constants import *

Data_ = airtable.Airtable(BASE_ID, API_KEY)


def _get_now_date():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_user_view(user_id):
    data = json.load(open('Creators.json'))
    if not str(user_id) in data:
        raise SearchUser(user_id)
    return data[str(user_id)]['view']


def get_view_data(user_id, table=TABLE_EDITING, formula=TASKS_IN_PROGRESS_FORMULA, fields_=EDITING_FIELDS):
    return Data_.iterate(
        table_name=table, view=get_user_view(user_id), fields=fields_,
        filter_by_formula=formula, max_records=15
    )


def process_links(data, name=None):
    urls = [x[0] for x in re.findall(URL_REGULAR, data)]

    return [data.replace('<', '').replace('>', '').replace(i, f"<a href='{i}'>{urlparse(i).netloc}</a>" if not name
    else f"<a href='{i}'>{name}</a>") for i in urls][-1] if urls else data


def processing_editing_tasks(data):
    return f'<b><i>{data["Name"].split(" | ")[0]}</i></b>\n' \
           f'Status: {data["Status"].replace("u200d", "")}\n' \
           f'Brand: {data["Brand"][0]}'


def fields_processing(field):
    return field[0] if field and isinstance(field, list) else field if field else ''


def process_status(record, filed):
    print(record)
    result = record.get(filed)
    return result[0] if result and isinstance(result, list) else ''


def processing_technical_support_tasks(data):
    return f'<b><i>⁉️ Technical Support</i></b>\n\n' \
           f'{data["Created By (Text)"]} submitted new support ticket\n\n' \
           f'Details: {process_links(data["Details"])}\n' \
           f'{process_links(data["Airtbale Record URL"], "Airtable URL")}\n\n' \
           f'{process_status(data, "🚦 Actual Status Text")} <b>⇒</b> ' \
           f'{process_status(data, "🚦 Next Status")}\n\n' \
           f'{process_status(data, "Name (from 💻 Editing)")}'


def getting_processed_data(user_id):
    return [processing_editing_tasks(i.get('fields')) for i in get_view_data(user_id)]


def _get_view_records(view_, formula_, fields_, table=TABLE_EDITING):
    return Data_.iterate(
        table_name=table, view=view_, fields=fields_,
        filter_by_formula=formula_
    )


def get_views():  # print([i for i in kek if bot.approve_chat_join_request(user_id=float(i))])
    return [i['view'] for i in json.load(open('Creators.json')).values()]


def get_views_records():
    print(' get_views_records()')
    arr, data = [], json.load(open('updates.json'))
    for j in get_views():
        for i in _get_view_records(j, ASSIGNED_FORMULA, 'record_id'):
            arr.append(i.get('id'))

    for j in _get_view_records(view_=TECHNICAL_SUPPORT_VIEW, formula_=None, fields_=TECHNICAL_SUPPORT_FIENDS,
                               table=TABLE_REVISIONS):
        arr.append(j.get('id'))
    data[_get_now_date()] = arr
    json.dump(data, open('updates.json', 'w'), indent=4)


def unpack_dict(dict_):
    return reduce(or_, dict_.values())


def list_difference(li1, li2):
    return list(set(li1) - set(li2))


def get_record_photo(record):
    print('get_record_photo(record)')
    photo = record.get('fields').get('Attachments')
    return photo[0].get('url') if photo else None


# def get_record_editing(record):
#     editing = record.get('fields').get('Name (from 💻 Editing)')
#     return editing[0].get() if editing else None


def delete_records_json():
    saved_records = list(json.load(open('updates.json', 'r')).items())[-1]
    modified_dict = {
        saved_records[0]: saved_records[1]
    }
    json.dump(modified_dict, open('updates.json', 'w'), indent=4)


def check_updates():
    print('check updates')
    get_views_records()
    data = json.load(open('updates.json'))
    records = list(data.values())

    if records[-1] == records[-2]:
        return

    result = list_difference(records[1], records[0])
    # delete_records_json()
    return result


def getting_result_records():
    print('getting_result_records()')
    result = []
    new_records = check_updates()  # KEK
    creators_ = json.load(open('Creators.json'))

    if not new_records:
        delete_records_json()
        return

    for i in creators_.items():
        for j in _get_view_records(i[1]['view'], ASSIGNED_FORMULA, ['Name', 'Status', 'Brand']):
            if any(j.get('id') == x for x in new_records):
                result.append((i[0], processing_editing_tasks(j.get('fields'))))

    for j in _get_view_records(view_=TECHNICAL_SUPPORT_VIEW, formula_=None, fields_=TECHNICAL_SUPPORT_FIENDS,
                               table=TABLE_REVISIONS):
        if any(j.get('id') == x for x in new_records):
            result.append(
                (TECHNICAL_SUPPORT_CHANNEL, processing_technical_support_tasks(j.get('fields')), get_record_photo(j)))

    print(result)
    return result