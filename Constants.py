TABLE = '💻 Editing'
view_ = 'Vlad Legun In Progress'


""" Formulas """


FORMULA_1 = "AND({Status} != '✅ Editing Done', {Status} != '🤴🏻 Client Editing Approval')"
TASKS_IN_PROGRESS_FORMULA = "OR({Status} = '👨🏻‍💻 Editor Assigned', " \
                            "{Status} = '✋🏼 On Hold', " \
                            "{Status} = '👍🏼 Ready To Go')"

EDITOR_ASSIGNED_FORMULA = "{Status} = '👨🏻‍💻 Editor Assigned'"
EDITOR_REVISION_FORMULA = "{Status} = '⭕️ Revision'"
ASSIGNED_FORMULA = "OR({Status} = '⭕️ Revision', {Status} = '👨🏻‍💻 Editor Assigned')"

""" FIELDS """

FIELDS = ['Name', 'Status', 'Brand']