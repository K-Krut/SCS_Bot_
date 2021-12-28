# "OrderedDict([('id', 'rec1Ed9tKDZKd6xDb'), ('fields', OrderedDict([('Status', '🧑🏼\u200d💼 SM Editing Review'), " \
# "('Name', 'TiSo - Football event photos | Basic Photo Editing (<100 RAW Photos) | TiSo rec1Ed9tKDZKd6xDb'), " \
# "('Brand', ['Titanium Solar'])])), ('createdTime', '2021-12-20T19:17:03.000Z')])".encode('utf-8', 'namereplace')



import airtable


view_ = 'KKrut In Progress'
Data_ = airtable.Airtable(BASE_ID, API_KEY)
for i in Data_.iterate(table_name=TABLE, view=view_, fields=['Name', 'Status', 'Brand'], max_records=1):
    print(i)
