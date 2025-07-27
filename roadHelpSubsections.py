import json
from typing import Awaitable, Callable, Optional, TypedDict
from telegram import  InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Update
from telegram.ext import (
    ContextTypes
)

class SectionData(TypedDict, total=False):
    s: str
    t: str
    ss: Optional[str]

async def show_road_help_subsections(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    """Отображаем подразделы мобильной аппликации."""
    subsections_buttons = [
    [InlineKeyboardButton("Номер для обращения клиентов за получением услуг Помощи на дорогах", callback_data=json.dumps({"s": 'road_help', "t": 'tel_number'}))],
    [InlineKeyboardButton("Что в себя включает Помощь на дорогах", callback_data=json.dumps({"s": 'road_help', "t": 'about'}))],
    [InlineKeyboardButton("Период действия программы Помощь на дорогах", callback_data=json.dumps({"s": 'road_help', "t": 'validity_period'}))],
    [InlineKeyboardButton("Ограничено ли количество обращений?", callback_data=json.dumps({"s": 'road_help', "t": 'requests_limited'}))],
    [InlineKeyboardButton("Радиус действия", callback_data=json.dumps({"s": 'road_help', "t": 'range'}))],
    [InlineKeyboardButton("Продление программы", callback_data=json.dumps({"s": 'road_help', "t": 'program_extension'}))],
    [InlineKeyboardButton("Назад", callback_data=json.dumps({"s": 'cancel'}))]
    ]

    reply_markup = InlineKeyboardMarkup(subsections_buttons)
    await query.edit_message_text(
        text="Выберите интересующий Вас раздел мобильного приложения VOYAH:",
        reply_markup=reply_markup
    )


async def handle_road_help_voyah(query: CallbackQuery, action_type: SectionData, context: ContextTypes.DEFAULT_TYPE, callback: Callable[
    [
        Update | CallbackQuery,
        ContextTypes.DEFAULT_TYPE
    ],
    Awaitable[None]
]):
    """Основная логика обработки действий (выбор разделов и подразделов)."""
    messages = {
    'tel_number': {
        'text': 'Номер для обращения клиентов за получением услуг "Помощи на дорогах": 8-800-600-69-61',
        'question': 'Номер для обращения клиентов за получением услуг "Помощи на дорогах"'
    },
    'about': {
        'text': 'С подробным перечнем доступных услуг Вы можете ознакомиться перейдя по ссылке: https://voyah.su/assistance?footer',
        'question': 'Что в себя включает Помощь на дорогах?'
    },
    'validity_period': {
        'text': 'Услуги действуют в течение 1 года с момента покупки автомобиля',
        'question': 'Период действия программы Помощь на дорогах?'
    },
    'range': {
        'text': 'Услуги оказываются на всей территории Российской Федерации, Республики Беларусь и Республики Казахстан на расстоянии не далее, чем 200 (двести) километров от места ДТП/Неисправности.',
        'question': 'Радиус действия'
    },
    'requests_limited': {
        'text': 'В рамках действия программы количество обращений не ограничено.',
        'question': 'Ограничено ли количество обращений?'
    },
    'program_extension': {
        'text': 'Теперь для всех автомобилей приобретенных в авторизованной дилерской сети VOYAH, со 2 года владения, доступно продление программы "Помощь на дорогах", которая действует при прохождении планового Технического обслуживания у авторизованного дилерского центра и распространяется на автомобили VOYAH возрастом до 10 лет.\nОбновленная программа длится до момента очередного обращения клиента для прохождения очередного Технического обслуживания, но не более 365 дней с момента продления или 15 000 км пробега для EV и 10 000 км для EVR - в зависимости от того, что наступит раньше.Информацию об участии в программе уточняйте у Вашего дилера VOYAH.',
        'question': 'Продление программы'
    }
}
    await callback(query, messages[action_type['t']]['text'], context, messages[action_type['t']]['question'])
