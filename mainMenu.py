import json
from telegram import  InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
global HELPER_BOT_USERNAME  # Имя специального бота для связи
HELPER_BOT_USERNAME = "@Motorinvest_HELP_bot"

main_menu_buttons = [
        [InlineKeyboardButton("Мобильное приложение VOYAH", callback_data=json.dumps({"s":'app_voyah'}))],
        [InlineKeyboardButton("Мультимедийная система и ПО", callback_data=json.dumps({"s":'app_multimedijnaya_sistema_i_po'}))],
        [InlineKeyboardButton("SIM-карта", callback_data=json.dumps({"s":'app_sim_card'}))],
		[InlineKeyboardButton("Сервис и гарантия", callback_data=json.dumps({"s":'app_service_garanty'}))],
		[InlineKeyboardButton("Запасные части", callback_data=json.dumps({"s":'app_spare_parts'}))],
		[InlineKeyboardButton("Помощь на дорогах", callback_data=json.dumps({"s":'app_road_help'}))],
    ]
