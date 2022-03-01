import json
from datetime import datetime
from functools import reduce
from operator import or_
import airtable
from exceptions import SearchUser
from config import BASE_ID, API_KEY
from Constants import TABLE, ASSIGNED_FORMULA, TASKS_IN_PROGRESS_FORMULA, FIELDS


Data_ = airtable.Airtable(BASE_ID, API_KEY)


def _get_now_date():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_user_view(user_id):
    data = json.load(open('Creators.json'))
    if not str(user_id) in data:
        raise SearchUser(user_id)
    return data[str(user_id)]['view']


def get_view_data(user_id):
    return Data_.iterate(
        table_name=TABLE, view=get_user_view(user_id), fields=FIELDS,
        filter_by_formula=TASKS_IN_PROGRESS_FORMULA, max_records=15
    )


def processing(data):
    return f'<b><i>{data["Name"].split(" | ")[0]}</i></b>\n' \
           f'Status: {data["Status"].replace("u200d", "")}\n' \
           f'Brand: {data["Brand"][0]}'


def getting_processed_data(user_id):
    return [processing(i.get('fields')) for i in get_view_data(user_id)]


def _get_view_records(view_, formula_, fields_):
    return Data_.iterate(
        table_name=TABLE, view=view_, fields=fields_,
        filter_by_formula=formula_
    )


def get_views():
    # print([i for i in kek if bot.approve_chat_join_request(user_id=float(i))])
    return [i['view'] for i in json.load(open('Creators.json')).values()]


def get_views_records():
    arr, data = [], json.load(open('updates.json'))
    for j in get_views():
        for i in _get_view_records(j, ASSIGNED_FORMULA, 'record_id'):
            arr.append(i.get('id'))
    data[_get_now_date()] = arr
    json.dump(data, open('updates.json', 'w'), indent=4)


def unpack_dict(dict_):
    return reduce(or_, dict_.values())


def list_difference(li1, li2):
    return list(set(li1) - set(li2))


def delete_records_json():
    kek = list(json.load(open('updates.json', 'r')).items())[-1]
    modified_dict = {
        kek[0]: kek[1]
    }
    json.dump(modified_dict, open('updates.json', 'w'), indent=4)


def check_updates():
    get_views_records()
    data = json.load(open('updates.json'))
    records = list(data.values())

    if records[-1] == records[-2]:
        return

    result = list_difference(records[1], records[0])
    delete_records_json()
    return result


def getting_result_records():
    result = []
    new_records = check_updates()
    creators_ = json.load(open('Creators.json'))

    if not new_records:
        delete_records_json()
        return

    for i in creators_.items():
        for j in _get_view_records(i[1]['view'], ASSIGNED_FORMULA, ['Name', 'Status', 'Brand']):
            if any(j.get('id') == x for x in new_records):
                result.append((i[0], processing(j.get('fields'))))
    return result
