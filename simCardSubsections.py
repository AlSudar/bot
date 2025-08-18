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

async def show_simcard_subsections(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    """Отображаем подразделы мобильной аппликации."""
    subsections_buttons = [
    [InlineKeyboardButton("Какое количество SIM - карт установлено в автомобиле VOYAH?", callback_data=json.dumps({"s": 'sim_card', "t": 'count_simcards'}))],
    [InlineKeyboardButton("Кто активирует SIM - карту?", callback_data=json.dumps({"s": 'sim_card', "t": 'who_active_simcard'}))],
    [InlineKeyboardButton("Тарифы SIM - карт", callback_data=json.dumps({"s": 'sim_card', "t": 'tarrif_simcard'}))],
    [InlineKeyboardButton("Что будет с SIM - картой после истечения предоплаченного срока?", callback_data=json.dumps({"s": 'sim_card', "t": 'simcard_before_deactive'}))],
    [InlineKeyboardButton("Как узнать номер SIM - карты для пополнения", callback_data=json.dumps({"s": 'sim_card', "ss": 'simcard_number'}))],
    [InlineKeyboardButton("Возможно ли переоформить SIM - карту?", callback_data=json.dumps({"s": 'sim_card', "ss": 're_register_simcard'}))],
    [InlineKeyboardButton("Возможно ли заменить SIM - карту на свою?", callback_data=json.dumps({"s": 'sim_card', "t": 'swap_simcard'}))],
    [InlineKeyboardButton("Не работает SIM - карта (интернет) в мультимедийной системе", callback_data=json.dumps({"s": 'sim_card', "ss": 'simcard_error'}))],
    [InlineKeyboardButton("Как узнать баланс или остаток интернет трафика SIM - карты?", callback_data=json.dumps({"s": 'sim_card', "t": 'simcard_balance'}))],
     [InlineKeyboardButton("Когда необходимо пополнить SIM - карту", callback_data=json.dumps({"s": 'sim_card', "t": 'when_simcard_balance'}))],
    [InlineKeyboardButton("Назад", callback_data=json.dumps({"s": 'cancel'}))]
    ]

    reply_markup = InlineKeyboardMarkup(subsections_buttons)
    await query.edit_message_text(
        text="Выберите интересующий Вас раздел:",
        reply_markup=reply_markup
    )

async def show_check_number_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("Запросить дилерский центр в котором приобретался автомобиль", callback_data=json.dumps({"s": 'sim_card', "t": 'get_diller_center'}))],
         [InlineKeyboardButton("Проверить наличие блистера из под SIM - карты в бардачке ", callback_data=json.dumps({"s": 'sim_card', "t": 'get_simcard_blister'}))],
          [InlineKeyboardButton("Не удалось выяснить номер у дилера, а также отсутствует блистер", callback_data=json.dumps({"s": 'sim_card', "t": 'not_simcard_blister'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Выберите подходящий вариант:",
        reply_markup=reply_markup
    )

async def show_re_register_simcard_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    """Отображение подразделов подключения приложения к авто."""
    connection_subbuttons = [
        [InlineKeyboardButton("Владельцем автомобиля является физ. лицо", callback_data=json.dumps({"s": 'sim_card', "t": 'simcard_register_fiz'}))],
         [InlineKeyboardButton("Владельцем автомобиля является юр. лицо", callback_data=json.dumps({"s": 'sim_card', "t": 'simcard_register_ur'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Выберите подходящий вариант:",
        reply_markup=reply_markup
    )

async def show_simcard_error_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    """Отображение подразделов подключения приложения к авто."""
    connection_subbuttons = [
        [InlineKeyboardButton("Да", callback_data=json.dumps({"s": 'sim_card', "ss": 'simcard_error_before_work'}))],
         [InlineKeyboardButton("Нет", callback_data=json.dumps({"s": 'sim_card', "t": 'simcard_error_after_work'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Ранее интернет работал?",
        reply_markup=reply_markup
    )

async def show_simcard_error_before_work_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("Да", callback_data=json.dumps({"s": 'sim_card', "t": 'smcrd_error_bfr_wrk_yes'}))],
         [InlineKeyboardButton("Нет", callback_data=json.dumps({"s": 'sim_card', "t": 'smcrd_error_bfr_wrk_no'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Закончился лимит трафика Интернета или не пополнили баланс?",
        reply_markup=reply_markup
    )

async def handle_action_simcard(query: CallbackQuery, action_type: SectionData, context: ContextTypes.DEFAULT_TYPE, callback: Callable[
    [
        Update | CallbackQuery,
        ContextTypes.DEFAULT_TYPE
    ],
    Awaitable[None]
]):
    """Основная логика обработки действий (выбор разделов и подразделов)."""
    messages = {
    'count_simcards': {
        'text': 'В автомобиле может быть установлено до двух SIM - карт. Одна SIM - карта установлена в блоке T-BOX и обеспечивает интернетом мультимедийную систему автомобиля (чтобы Вы могли пользоваться приложениями, которым требуется наличие интернета). В блоке T-BOX может быть установлена как физическая SIM - карта, так и Симчип. Вторая SIM - карта установлена в блоке телематики (в случае, если Ваш автомобиль оборудован/дооборудован данным блоком) для обеспечения связи между мобильным приложением VOYAH и автомобилем.',
        'question': 'Какое количество SIM - карт установлено в автомобиле VOYAH?'
    },
    'who_active_simcard': {
        'text': 'Активацию SIM - карты, установленной в мультимедийной системе автомобиля осуществляет дилерский центр, в котором Вы приобретаете автомобиль, при подготовке VOYAH к выдаче Вам - покупателю.\nАктивацию SIM - карты установленной в блоке телематики (в случае, если Ваш автомобиль оборудован/дооборудован данным блоком), осуществляется в том месте, где устанавливается данный блок. Если блок телематики установлен Изготовителем на заводе, то активацию SIM - карты осуществляет Завод. Если блок телематики устанавливается официальным дилером в качестве дооборудования автомобиля, то активацию осуществляет дилер - установщик.',
        'question': 'Кто активирует SIM - карту?'
    },
    'tarrif_simcard': {
        'text': 'В автомобилях VOYAH, приобретенных у официальных дилеров, для обеспечения интернетом мультимедийной системы, установлена SIM - карта оператора Мегафон с тарифом  –  "Мегафон Онлайн Корпоративный" включающий в себя 30 ГБ интернет трафика в месяц. Данный тариф разработан специально для нашей компании. Каждому покупателю предоставляется 3 месяца предоплаченного периода (то есть безвозмездное пользование), а по истечению 3 месяца  подключается тариф, оплата по которому составляет 450 рублей в месяц. Указанная сумма списывается 1 числа каждого месяца, для поддержания постоянного доступа к интеренту в мультимедийной системе автомобиля, требуется своевременно пополнять номер. \nSIM - карту установленную в блок телематики не требуется пополнять, так как предоплаченный период по ней составляет весь гарантийный период автомобиля.',
        'question': 'Тарифы SIM - карт'
    },
    'simcard_before_deactive': {
        'text': 'SIM - карта рассчитана на весь период гарантии автомобиля. После завершения предоплаченного периода, если Вы пожелаете пользоваться SIM - картой далее, то Вам необходимо оплачивать абонентскую плату. (см. "Тарифы SIM - карт").',
        'question': 'Что будет с SIM - картой после истечения предоплаченного срока?'
    },
    'swap_simcard': {
        'text': 'Если Вы желаете заменить SIM - карту на свою собственную (в блоке T-BOX или в блоке телематики), то Вы можете обратиться к любому официальному дилеру для проведения работ по замене SIM - карты. Просим обратить внимание, что данные работы являются платными.',
        'question': 'Возможно ли заменить SIM - карту на свою?'
    },
    'simcard_balance': {
        'text': 'Укажите Ваше имя, контактный номер телефона по которому с Вами можно свзаться, VIN автомобиля, а также номер SIM -карты (если он Вам известен). Мы уточним информацию у оператора сети Мегафон и предоставим ответ.',
        'question': 'Как узнать баланс или остаток интернет трафика SIM - карты?'
    },
    'get_diller_center': {
        'text': 'Требуется запросить дилерский центр в котором приобретался автомобиль, именно дилерскому центру передается блистер с SIM - карты для активации. Дилерский центр при выдаче нового автомобиля подписывает с покупателем Согласие об использовании SIM - карты в автомобиле, в котором указывается номер SIM - карты.',
        'question': 'Как узнать номер SIM - карты для пополнения?'
    },
    'get_simcard_blister': {
        'text': 'Проверьте наличие блистера из под SIM - карты в бардачке или сопровождающей автомобиль документации.',
        'question': 'Как узнать номер SIM - карты для пополнения?'
    },
    'not_simcard_blister': {
        'text': f'Чтобы мы смогли уточнить номер SIM - карты установленной на Вашем VOYAH , напишите нашей поддержке {HELPER_BOT_USERNAME} и укажите Ваше имя, контактный номер телефона, VIN автомобиля, а также укажите кратко суть обращения.',
        'question': 'Как узнать номер SIM - карты для пополнения?'
    },
    'simcard_register_fiz': {
        'text': 'SIM - карта изначально оформлена на Импортера/Изготовителя и переоформление на физическое лицо не предусмотрено. ',
        'question': 'Возможно ли переоформить SIM - карту если владелец автомобиля физ.лицо?'
    },
    'simcard_register_ur': {
        'text': f'SIM - карта изначально оформлена на Импортера/Изготовителя, переоформление на юр. лицо осуществить возможно. Просим вас написать нашей поддержке {HELPER_BOT_USERNAME} указать Вас VIN автомобиля, в ответ мы предоставим Вам информацию, каким образом можно осуществить переоформление.',
        'question': 'Возможно ли переоформить SIM - карту если владелец автомобиля юр.лицо?'
    },
    'simcard_error_after_work': {
        'text': 'Требуется обратиться в дилерский центр, в котором приобретался автомобиль для активации SIM - карты.',
        'question': 'Не работает SIM - карта (интернет) в мультимедийной системе, ранее интернет не работал'
    },
    'smcrd_error_bfr_wrk_yes': {
        'text': 'Требуется пополнить баланс SIM - карты. Предоставление трафика 30 ГБ в соответствии с тарифом «Мегафон Онлайн Корпоративный" для обеспечения интернетом мультимедийной системы возобновится 1 числа следующего месяца при условии пополнения баланса SIM-карты на 450 рублей. Пополнение баланса SIM-карты следует осуществить в последний день текущего месяца, по причине того, что в случае если баланс будет пополнен раньше, то при исчерпании трафика 30 ГБ предусмотренного тарифом, подключится помегабайтная тарификация (оплата взимается за каждый расходуемый мегабайт интернета) и внесенная Вами сумма будет расходоваться.',
        'question': 'Не работает SIM - карта (интернет) в мультимедийной системе. Возможно был израсходован выделенный трафик или не был пополнен баланс'
    },
    'smcrd_error_bfr_wrk_no': {
        'text': 'В случае если проблема не связана с наличием трафика или в нулевым балансом, то проблема может быть: \n• в некоторых случаях бывает, что дата списания уже прошла (то есть дата больше, чем первое число месяца), баланс SIM- карты был пополнен своевременно, однако сумма оплаты по тарифу по техническим причинам не списалась оператором. Для того, чтобы интернет возобновил свою работу, требуется убедиться, что на балансе SIM- карты имеется 450 рублей, исключить потребление трафика мультимедийной системой автомобиля (необходимо выключить автомобиль, чтобы мультимедиа полностью погасла, желательно покинуть автомобиль и закрыть его), подождать около 15 минут, не открывая и не запуская автомобиль в период ожидания. За время ожидания должно произойти списание абонентской платы по тарифу. Далее Вы открываете автомобиль и эксплуатируете его в обычном режиме. Обращаем внимание, что если не выключать автомобиль и не выдерживать паузу необходимую для списания абонентской платы, производить пополнение баланса с одновременным потреблением трафика интернета мультимедийной системой, то внесенная Вами сумма на баланс SIM-карты, будет расходоваться на помегабайтный трафик до бесконечности. Рекомендуем пополнять баланс вечером в последний день месяца, тогда автомобиль длительное время выключен и абонентская плата беспрепятственно списывается; \n• проблема может возникнуть в самой SIM – карте, установленной в блоке T-BOX (износилась, повредилась и т.д) или в ПО мультимедийной системы, неисправность самого блока T-BOX. Для более точного определения неисправности существующей на Вашем автомобиле, рекомендуем провести диагностику у любого официального дилера VOYAH в России. С полным списком дилеров Вы можете ознакомится на нашем официальном сайте: https://voyah.su/voyah-space/dealerships, запись возможно осуществить, заполнив форму обратной связи: https://voyah.su/voyah-service/service-form?mobile',
        'question': 'Не работает SIM - карта (интернет) в мультимедийной системе. Проблема не связана с выделенным трафиком или пополнением баланса'
    },
    'when_simcard_balance': {
        'text': 'Предоставление трафика 30 ГБ в соответствии с тарифом «Мегафон Онлайн Корпоративный" для обеспечения интернетом мультимедийной системы возобновляется 1 числа каждого месяца при условии пополнения баланса SIM-карты на 450 рублей. Пополнение баланса SIM-карты следует осуществить в последний день текущего месяца, по причине того, что в случае если баланс будет пополнен раньше, то при исчерпании трафика 30 ГБ предусмотренного тарифом, подключится помегабайтная тарификация (оплата взимается за каждый расходуемый мегабайт интернета) и внесенная Вами сумма будет постепенно расходоваться. Рекомендуем пополнять баланс вечером в последний день месяца, тогда автомобиль длительное время выключен и абонентская плата беспрепятственно списывается. Если до даты списания (1 число каждого месяца) еще далеко, а Вам требуется воспользоваться интернетом в мультимедийной системе, то Вы можете производить пополнение баланса на произвольную сумму, внесенная Вами сумма на баланс SIM-карты, будет расходоваться на помегабайтный трафик.',
        'question': 'Когда необходимо пополнить SIM - карту?'
	}
}

    if 'ss' in action_type and action_type['ss'] == 'simcard_number':
       await show_check_number_subsection(query, context)
    elif 'ss' in action_type and action_type['ss'] == 're_register_simcard':
       await show_re_register_simcard_subsection(query, context)
    elif 'ss' in action_type and action_type['ss'] == 'simcard_error':
       await show_simcard_error_subsection(query, context)
    elif 'ss' in action_type and action_type['ss'] == 'simcard_error_before_work':
       await show_simcard_error_before_work_subsection(query, context)
    else:
     await callback(query, messages[action_type['t']]['text'], context, messages[action_type['t']]['question'])
