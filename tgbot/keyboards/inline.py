from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Example of inline keyboard
def very_simple_keyboard():
    buttons = [
        [
            InlineKeyboardButton(text="📝 Создать заказ", callback_data="create_order"),
            InlineKeyboardButton(text="📋 Мои заказы", callback_data="my_orders"),
        ],
    ]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=buttons,
    )
    return keyboard
