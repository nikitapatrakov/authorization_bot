from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

from config import setting

def keyboard_start():
    builder =InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Cсылка на группу", url=str(setting.url_group)))
    return builder.as_markup()