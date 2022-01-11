import json
from datetime import datetime
from functools import reduce
from operator import or_

import airtable
import dictdiffer as dictdiffer
import numpy

from exceptions import SearchUser
from config import BASE_ID, API_KEY
from Constants import TABLE, EDITOR_ASSIGNED_FORMULA, EDITOR_REVISION_FORMULA, \
    ASSIGNED_FORMULA, TASKS_IN_PROGRESS_FORMULA, FIELDS


Data_ = airtable.Airtable(BASE_ID, API_KEY)


def _get_now_date():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_user_view(user_id):
    data = json.load(open('Creators.json'))
    if not str(user_id) in data:
        raise SearchUser(user_id)
    print(data[str(user_id)]['view'])
    return data[str(user_id)]['view']


def get_view_data(user_id):
    return Data_.iterate(
        table_name=TABLE, view=get_user_view(user_id), fields=FIELDS,
        filter_by_formula=TASKS_IN_PROGRESS_FORMULA, max_records=5
    )


def processing(data):
    print(data)
    return f'<b><i>{data["Name"].split(" | ")[0]}</i></b>\n' \
           f'Status: {data["Status"].replace("u200d", "")}\n' \
           f'Brand: {data["Brand"][0]}'


def getting_processed_data(user_id):
    print([processing(i.get('fields')) for i in get_view_data(user_id)])
    return [processing(i.get('fields')) for i in get_view_data(user_id)]


def _get_view_records(view_, formula_):
    return Data_.iterate(
        table_name=TABLE, view=view_, fields='record_id',
        filter_by_formula=formula_
    )


def get_views():
    return [i['view'] for i in json.load(open('Creators.json')).values()]


def get_views_records():
    arr, data = {}, json.load(open('updates.json'))
    for j in get_views():
        assigned_arr, revisions_arr = [], []
        for i in _get_view_records(j, ASSIGNED_FORMULA):
            if i.get('fields')['Status'] == '👨🏻‍💻 Editor Assigned':
                assigned_arr.append(i.get('id'))
            else:
                revisions_arr.append(i.get('id'))
            arr[j] = {
                "assigned": assigned_arr,
                "revisions": revisions_arr
            }
            print(arr)
        data[_get_now_date()] = arr
    json.dump(data, open('updates.json', 'w'), indent=4)


def unpack_dict(dict_):
    # print(reduce(or_, dict_.values()), dict_)
    return reduce(or_, dict_.values())


def check_updates():
    data = json.load(open('updates.json'))
    # print(data)
    # print(type(data.values()), data.values())
    records = list(data.values())
    if not records[0] == records[1]:
        for k in unpack_dict(data):
            print(unpack_dict(k))
        # for i in data.values():
        #     # print(i)
        #     unpack_dict(i)
        #     for j in i:
        #         print()
        #         # print(j)
        # # print(set.difference(records[1].items()))


"""value = { k : second_dict[k] for k in set(second_dict) - set(first_dict) }"""
check_updates()




"""(
    'add', '',
    [
        (
            'Mikola Matskevich',
            {
                'assigned': ['rec68mFqf6P4VGvZo'],
                'revisions': []
            }
        )
    ]
)
"""
"""[
    {
        'Serge Creator - Creator':
            {
                'assigned': [], 
                'revisions': [
                    'recufsQKq8TyiQOI9', 'receAX1QZmsUlXQAP'
                ]
            }
    }, 
    {
        'Serge Creator - Creator': 
            {
                'assigned': [
                    
                ], 
                'revisions': [
                    'recufsQKq8TyiQOI9', 'receAX1QZmsUlXQAP'
                ]
            }, 
        'Mikola Matskevich': 
            {
                'assigned': 
                    [
                        'rec68mFqf6P4VGvZo'
                    ], 
                'revisions': [
                    
                ]
            }
    }
]

"""