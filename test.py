import datetime
import json
from _operator import or_
from functools import reduce
#
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
#
# # def get_views_records():
# #     arr = {}
# #     for j in get_views():
# #         print(j)
# #         # assigned_arr, revisions_arr = [], []
# #         for i in _get_view_records(j, ASSIGNED_FORMULA):
# #             # assigned_arr.append(i) if i['Status'] == '👨🏻‍💻 Editor Assigned'] else revisions_arr.append(i)
# #             # arr[j]['assigned'] = i
# #             print(i.get('fields')['Status'])
# #     return arr
# #         # return [[i.get('id') for i in _get_view_records(j, TASKS_IN_PROGRESS_FORMULA)] for j in get_views()]
# a = {
#     "KKrut": {
#         "assigned": [
#
#         ],
#         "revisions": [
#             "recufsQKq8Ty98666",
#             "receAX1QZmsUlXQAP"
#         ]
#     }
# }
# b = {
#     "KKrut": {
#         "assigned": [
#
#         ],
#         "revisions": [
#             "recufsQKq8Ty98666",
#             "receAX1QZmsjjjjjj"
#         ]
#     }
# }
# print(set(list(a)))
#
# d = {'key1': {8772, 9605},'key2': {10867, 10911, 10917},'key3': {11749,11750},'key4': {14721, 19755, 21281}}
# s = reduce(or_, d.values())
# print(s)
# h = reduce(or_, b.values())
# print(h)
# j = {'assigned': [], 'revisions': ['recufsQKq8Ty98666', 'receAX1QZmsjjjjjj']}

# def delete_records_json():
#    data_ = json.load(open('her.json', 'r'))
#    kek = list(data_.items())[1]
#    syka = {}
#    syka[kek[0]] = kek[1]
#    json.dump(syka, open('her.json', 'w'), indent=4)
#
#
# delete_records_json()
#



"""    kek = list(data_.items())[1]
    print(data_)
    blia = {}
    blia[kek[0]] = kek[1]
    print(blia)
    json.dump(blia, open('updates.json', 'w'), indent=4)"""


# print(list(data_.items())[1])
# print(dict(itertools.islice(data_.items(), 1)))
# for i in data_.items():
#     print(i)
# i.pop(list(data_.keys())[0])
# json.dump(data_, open('updates.json', 'w'), indent=4)
# json.dump(data, json.load(open('updates.json', 'w')))

"""value = { k : second_dict[k] for k in set(second_dict) - set(first_dict) }"""
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


[
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


# def list_difference(li1, li2):
#    return list(set(li1) - set(li2))
#
#
# a = [
#     "recufsQKq8TyiQOI9",
#     "receAX1QZmsUlXQAP",
#     "recufsQKq8Ty98666",
#     "receAX1QZmsUlXQAP"
#   ]
# b = [
#     "rechJHbemaoZUlNP7",
#     "rechve8lfn2FLbQE2",
#     "recjwSotuWvPJ0A7C",
#     "recufsQKq8TyiQOI9",
#     "receAX1QZmsUlXQAP",
#     "rec68mFqf6P4VGvZo"
#   ]
# print(list_difference(b, a))
# creators_ = json.load(open('Creators.json'))
# for i in creators_.items():
#    print(i[1]['view'])

res = json.load(open('her.json'))
if len(res) >= 2:
    res_1 = list(res.items())[-1]
    print(res_1)



    """[('1797329921', '<b><i>BlEn Team photos Basic editing</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Bluenergy'), ('1797329921', '<b><i> BlEn Roberto Life Style Photos Basic Edit</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Bluenergy'), ('1797329921', '<b><i>BlEn Group basic photo editing</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Bluenergy'), ('1797329921', '<b><i>BlEn Headshots Photos Basic Editing</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Bluenergy'), ('1797329921', '<b><i>BlEn Yacht Basic photo Editing</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Bluenergy'), ('1758551', '<b><i>Roberto CEO design guidance</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Roberto Gavilanes'), ('1758551', '<b><i>Blue energy Design guidance. </i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Bluenergy'), ('72235930', '<b><i>IGTV - Serge creator ft. Arthur J. Williams</i></b>\nStatus: ⭕️ Revision\nBrand: Serge Creator'), ('72235930', '<b><i>Podcast for Verification - Short Clip interview with Serge</i></b>\nStatus: ⭕️ Revision\nBrand: Serge Creator'), ('428907612', '<b><i>TrPo - Get calm to get the close</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: True Power'), ('428907612', '<b><i>TrPo - Can You Handle The word NO?</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: True Power'), ('428907612', '<b><i>TrPo - Always Sell The Install</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: True Power'), ('428907612', '<b><i>SmPo Podcast 3 trailer</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Team Smart Power'), ('428907612', '<b><i>Highlight video Podcast Fashion Island</i></b>\nStatus: ⭕️ Revision\nBrand: Titanium Solar'), ('5036498629', '<b><i>Leadership Quote 4</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Mani Ghadimi'), ('5036498629', '<b><i>Leadership Quote 3</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Mani Ghadimi'), ('5036498629', '<b><i>Branding Graphics - Blue Energy</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Bluenergy'), ('1653133613', '<b><i>Transcribe call 01/25</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Bluenergy'), ('1653133613', '<b><i>Call transcription 01/25</i></b>\nStatus: 👨🏻\u200d💻 Editor Assigned\nBrand: Bluenergy')]
"""