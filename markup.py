from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_button_tasks_in_progress = InlineKeyboardButton('📝My tasks📝', callback_data='TASKS_IN_PROGRESS')
inline_button_back = InlineKeyboardButton('🔙', callback_data='🔙')

keyboard_ = InlineKeyboardMarkup(row_width=2).add(inline_button_tasks_in_progress)