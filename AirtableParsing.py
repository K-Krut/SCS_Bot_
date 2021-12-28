# "OrderedDict([('id', 'rec1Ed9tKDZKd6xDb'), ('fields', OrderedDict([('Status', '🧑🏼\u200d💼 SM Editing Review'), " \
# "('Name', 'TiSo - Football event photos | Basic Photo Editing (<100 RAW Photos) | TiSo rec1Ed9tKDZKd6xDb'), " \
# "('Brand', ['Titanium Solar'])])), ('createdTime', '2021-12-20T19:17:03.000Z')])".encode('utf-8', 'namereplace')

# str.join('\n', [f'{i}: {self.__dict__[i]}' for i in self.__dict__.keys()])
# def __str__(self):
#      return '\n'.join([''.join([f'{j}: {i[j]}\n' for j in i.keys()]) for i in data.values()])


import airtable

API_KEY = 'keytmiDZHJP7bNZby'
BASE_ID = 'app8dUiwvFFBqZwct'
TABLE = '💻 Editing'
view_ = 'KKrut In Progress'
Data_ = airtable.Airtable(BASE_ID, API_KEY)
DICT_ = Data_.iterate(
    table_name=TABLE, view=view_, fields=['Name', 'Status', 'Brand'],
    filter_by_formula="{Status} != '✅ Editing Done'", max_records=10
)
# IF(
#   OR(
#     {Status} = "Recently Completed",
#     {Status} = "Completed/Archived"
#   ),
#   "✅Done✅",
#   IF(
#     {Target Completion Date} = BLANK(),
#     "🛑TARGET DATE NEEDED🛑",
#     IF(
#       AND(
#         OR(
#           {Status} = "In Progress",
#           {Status} = "Roadblocked"
#         ),
#         IS_BEFORE({Target Completion Date}, TODAY())
#       ),
#       "⏰OVERDUE⏰",
#       "🏃‍♂️In-progress🏃‍♂️"
#     )
#   )
# )

for i in DICT_:
    for j in i.get('fields').keys():
        print('\n'.join([f'{j}:  {i.get("fields")[j]}']))

