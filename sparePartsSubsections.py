import json
from typing import Awaitable, Callable, Optional, TypedDict
from telegram import  InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Update
from telegram.ext import (
    ContextTypes
)

from mainMenu import HELPER_BOT_USERNAME

class SectionData(TypedDict, total=False):
    s: str
    t: str
    ss: Optional[str]

async def show_spare_parts_subsections(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    """Отображаем подразделы мобильной аппликации."""
    subsections_buttons = [
    [InlineKeyboardButton("Стоимость запасной части", callback_data=json.dumps({"s": 'spare_parts', "t": 'spare_cost'}))],
    [InlineKeyboardButton("Подбор каталожного номера запасной части", callback_data=json.dumps({"s": 'spare_parts', "t": 'number_selection'}))],
    [InlineKeyboardButton("Возможность покупки запасной части у Импортера/Изготовителя", callback_data=json.dumps({"s": 'spare_parts', "t": 'buy_spare'}))],
    [InlineKeyboardButton("Долгий срок поставки запасной части", callback_data=json.dumps({"s": 'spare_parts', "ss": 'delivery_time'}))],
    [InlineKeyboardButton("Моторное масло для двигателя внутреннего сгорания", callback_data=json.dumps({"s": 'spare_parts', "t": 'motor-oil'}))],
    [InlineKeyboardButton("Назад", callback_data=json.dumps({"s": 'cancel'}))]
    ]

    reply_markup = InlineKeyboardMarkup(subsections_buttons)
    await query.edit_message_text(
        text="Выберите интересующий Вас раздел мобильного приложения VOYAH:",
        reply_markup=reply_markup
    )


async def show_delivery_time_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("Да", callback_data=json.dumps({"s": 'spare_parts', "t": 'delivery_time_yes'}))],
        [InlineKeyboardButton("Нет", callback_data=json.dumps({"s": 'spare_parts', "t": 'delivery_time_no'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Запасные части ожидаются для выполнения гарантийного ремонта?",
        reply_markup=reply_markup
    )

async def handle_action_spare_parts(query: CallbackQuery, action_type: SectionData, context: ContextTypes.DEFAULT_TYPE, callback: Callable[
    [
        Update | CallbackQuery,
        ContextTypes.DEFAULT_TYPE
    ],
    Awaitable[None]
]):
    """Основная логика обработки действий (выбор разделов и подразделов)."""
    messages = {
    'spare_cost': {
        'text': 'Каждый дилерский центр самостоятельно определяет, за какую стоимость реализовывать запасные части.  Одни дилеры для сохранения и привлечения клиентов, устанавливает цены ниже, предоставляют скидки. Другие устанавливает цены выше, предоставляя, при этом, более высокий уровень комфорта. Изготовитель/Импортер устанавливает рекомендуемые розничные цены на реализуемые запасные части, однако финальную стоимость запосной части определяет сам дилер.',
        'question': 'Стоимость запасной части'
    },
    'number_selection': {
        'text': 'Информация, предназначенная для владельца автомобиля, представлена в документации, передаваемой покупателю при продаже автомобиля, а именно в Сервисной книжке и Руководстве по эксплуатации.\nСведения, содержащиеся в каталогах запасных частей, в том числе и каталожные номера, предназначены исключительно для внутреннего использования Официальными Дилерами.\nПо вопросу приобретения оригинальных запасных частей рекомендуем обращаться в Официальные Дилерские центры, контактные данные и адреса которых указаны на официальном сайте: https://voyah.su/voyah-space/dealerships.',
        'question': 'Подбор каталожного номера запасной части'
    },
    'buy_spare': {
        'text': 'Информируем Вас, что реализацией запасных частей в розницу занимаются только дилерские центры VOYAH. Вы найдете их актуальный список с телефонами на официальном на официальном сайте: https://voyah.su/voyah-space/dealerships. Рекомендуем определиться с наличием детали у своего дилера, в случае отсутствия, осуществить у него предварительный заказ детали.',
        'question': 'Возможность покупки запасной части у Импортера/Изготовителя'
    },
    'motor-oil': {
        'text': 'Спецификация моторного масла для автомобилей VOYAH FREE EVR в комплектации H97, H97A, а также DREAM EVR в комплектации H56, H56A - SAE5W-30. Уровень качества: не ниже SN. \nСпецификация моторного масла для автомобилей VOYAH FREE EVR в комплектации H97C, а также DREAM EVR в комплектации H56B - SAE0W-20. Уровень качества: не ниже SP. \nОбязательно используйте моторное масло с характеристиками, подходящими для двигателя данного автомобиля. Использование моторного масла с другими характеристиками может привести к повреждению двигателя. Полный заправочный объем ДВС - 4 литра.',
        'question': 'Моторное масло для двигателя внутреннего сгорания'
    },
        'delivery_time_yes': {
        'text': f'Чтобы мы смогли уточнить срок поставки запасных частей для ремонта Вашего автомобиля VOYAH, напишите нашей поддержке {HELPER_BOT_USERNAME} и укажите Ваше имя, контактный номер телефона, VIN автомобиля, в какой дилерский центр Вы обращались, а также опишите какой ремонт ожидается.',
        'question': 'Долгий срок поставки запасной части, запасные части ожидаются для выполнения гарантийного ремонта'
    },
        'delivery_time_no': {
        'text': 'Наша организация осуществляет оптовую поставку запасных частей. Розничную продажу запасных частей осуществляет дилерский центр. Запасные части для ремонта автомобилей находятся на их складах. Заказ запасной части в нашей организации осуществляется на пополнение складов дилеров, и не имеет привязки к конкретному VIN автомобиля. Т.е. в нашу организацию не направляется заказ детали для ремонта автомобиля.',
        'question': 'Долгий срок поставки запасной части, запасные части ожидаются не для выполнения гарантийного ремонта'
    },
}


    if 'ss' in action_type and action_type['ss'] == 'delivery_time':
      await show_delivery_time_subsection(query, context)
    else:
     await callback(query, messages[action_type['t']]['text'], context, messages[action_type['t']]['question'])
