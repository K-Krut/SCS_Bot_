"""Tables"""

TABLE_EDITING = '💻 Editing'
TABLE_REVISIONS = '📝 Revisions'

"""Formulas"""

FORMULA_1 = "AND({Status} != '✅ Editing Done', {Status} != '🤴🏻 Client Editing Approval')"
TASKS_IN_PROGRESS_FORMULA = "OR({Status} = '👨🏻‍💻 Editor Assigned', " \
                            "{Status} = '✋🏼 On Hold', " \
                            "{Status} = '👍🏼 Ready To Go')"

EDITOR_ASSIGNED_FORMULA = "{Status} = '👨🏻‍💻 Editor Assigned'"
EDITOR_REVISION_FORMULA = "{Status} = '⭕️ Revision'"
ASSIGNED_FORMULA = "OR({Status} = '⭕️ Revision', {Status} = '👨🏻‍💻 Editor Assigned')"

"""Fields"""

EDITING_FIELDS = ['Name', 'Status', 'Brand']
TECHNICAL_SUPPORT_FIENDS = ["Created By (Text)", 'Details', '🚦 Actual Status Text', '🚦 Next Status',
                            'Name (from 💻 Editing)', 'Airtbale Record URL', 'Attachments']


"""Views"""
TECHNICAL_SUPPORT_VIEW = "Technical Support View"


"""Chats and Channels"""
TECHNICAL_SUPPORT_CHANNEL = "-1001175426622"


"""Other"""
URL_REGULAR = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]" \
              r"+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"


