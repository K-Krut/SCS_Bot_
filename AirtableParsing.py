# "OrderedDict([('id', 'rec1Ed9tKDZKd6xDb'), ('fields', OrderedDict([('Status', '🧑🏼\u200d💼 SM Editing Review'), " \
# "('Name', 'TiSo - Football event photos | Basic Photo Editing (<100 RAW Photos) | TiSo rec1Ed9tKDZKd6xDb'), " \
# "('Brand', ['Titanium Solar'])])), ('createdTime', '2021-12-20T19:17:03.000Z')])".encode('utf-8', 'namereplace')

# str.join('\n', [f'{i}: {self.__dict__[i]}' for i in self.__dict__.keys()])
# def __str__(self):
#      return '\n'.join([''.join([f'{j}: {i[j]}\n' for j in i.keys()]) for i in data.values()])
from typing import NamedTuple

import airtable
from config import BASE_ID, API_KEY


TABLE = '💻 Editing'
view_ = 'Vlad Legun In Progress'
FORMULA_1 = "AND({Status} != '✅ Editing Done', {Status} != '🤴🏻 Client Editing Approval')"
FORMULA_2 = "OR({Status} = '👨🏻‍💻 Editor Assigned', {Status} = '✋🏼 On Hold')"

Data_ = airtable.Airtable(BASE_ID, API_KEY)
DICT_ = Data_.iterate(
    table_name=TABLE, view=view_, fields=['Name', 'Status', 'Brand'],
    filter_by_formula=FORMULA_2, max_records=5
)


class Records(NamedTuple):
    name_ = str
    status_ = str
    brand_ = str


#
# def getting_data():
#     for i in DICT_:
#         print(i.get('fields').values())
#         for j in i.get('fields').items():
#             print(type(j))
#             processing(j)
#


def getting_data():
    return [processing(i.get('fields')) for i in DICT_]


def processing(data):
    return f'<b><i>{data["Name"].split(" | ")[0]}</i></b>\n' \
           f'Status: {data["Status"].replace("u200d", "")}\n' \
           f'Brand: {data["Brand"][0]}'

