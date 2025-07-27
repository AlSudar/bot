import json
from typing import Awaitable, Callable
from telegram import  InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Update
from telegram.ext import (
    ContextTypes
)
from mainMenu import HELPER_BOT_USERNAME

async def show_multimedia_i_po(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    subsections_buttons = [
        [InlineKeyboardButton("О замене чипа мультимедийной системы - NXP на Snapdragon 8155", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'about_cheap_nxp'}))],
		[InlineKeyboardButton("Хотите узнать, имеется ли более новое ПО на автомобиль?", callback_data=json.dumps({"s": 'multimedia_i_po', "ss": 'update_po'}))],
		[InlineKeyboardButton("Как обновить ПО мультимедийной системы на более свежее?", callback_data=json.dumps({"s": 'multimedia_i_po', 'ss': "how_update_po" }))],
		[InlineKeyboardButton("В мультимедийной системе автомобиля установлено не свежее ПО", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'old_po_in_car'}))],
		[InlineKeyboardButton("После обновления ПО мультимедиа, автомобиль работает неадекватно", callback_data=json.dumps({"s": 'multimedia_i_po', "ss": 'errors_after_update'}))],
		[InlineKeyboardButton("Дилер обновил ПО мультимедиа, после этого пропала часть функций", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'hide_functions_after_update'}))],
		[InlineKeyboardButton("Обновление ПО без визита к Дилеру, то есть через интернет.", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'update_po_internet'}))],
		[InlineKeyboardButton("В автомобиле не работает интернет", callback_data=json.dumps({"s": 'multimedia_i_po', "ss": 'internet_error'}))],
		[InlineKeyboardButton("Как перезагрузить мультимедийную систему?", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'reload_multimedia'}))],
		[InlineKeyboardButton("VOYAH STORE", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'voyah_store'}))],
		[InlineKeyboardButton("Как сохранять режимы вождения при перезапуске автомобиля?", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'save_settings'}))],
		[InlineKeyboardButton("Как активировать голосовое управление?", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'voice_control'}))],
		[InlineKeyboardButton("Как скачать стороннее приложение?", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'party_application'}))],
        [InlineKeyboardButton("Назад", callback_data=json.dumps({"s": 'cancel'}))]
	]

    reply_markup = InlineKeyboardMarkup(subsections_buttons)
    await query.edit_message_text(
        text="Выберите интересующий Вас раздел мультимедийной системы и ПО:",
        reply_markup=reply_markup
    )


async def show_new_po_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("FREE", callback_data=json.dumps({"s": 'multimedia_i_po', "ss": 'update_po_free'}))],
        [InlineKeyboardButton("DREAM", callback_data=json.dumps({"s": 'multimedia_i_po', "ss": 'update_po_dream'}))],
        [InlineKeyboardButton("PASSION", callback_data=json.dumps({"s": 'multimedia_i_po', "ss": 'update_po_passion'}))]
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Выберите Вашу модель VOYAH",
        reply_markup=reply_markup
    )

async def show_variants_free_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("Да", callback_data=json.dumps({"s": 'multimedia_i_po', "ss": 'update_po_free_know_cheep'}))],
        [InlineKeyboardButton("Нет", callback_data=json.dumps({"s": 'multimedia_i_po', "ss": 'update_po_free_unknow_cheep'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Вы знаете, какой чип установлен в мультимедии Вашего автомобиля?",
        reply_markup=reply_markup
    )

async def show_know_cheap_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("NXP", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'free_cheep_nxp'}))],
        [InlineKeyboardButton("Snapdragon 8155", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'free_sheep_snapdragon'}))],
        [InlineKeyboardButton("VOYAH FREE SPORT EDITION", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'free_cheep_sport_edition'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Выберите чип",
        reply_markup=reply_markup
    )

async def show_unknow_cheap_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("Самостоятельно посмотреть версию ПО в настройках мультимедийной системы", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'free_unknow_cheep_1'}))],
        [InlineKeyboardButton("Не удалось разобраться с версиями ПО", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'free_unknow_cheep_help'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Выберите из предложенных вариантов",
        reply_markup=reply_markup
    )

async def show_variants_dream_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("Дорестайлинговый (H56/H56A)", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'dream_after_restailing'}))],
        [InlineKeyboardButton("Рестайнговый (H56B), импорт из Китая, купленный у Дилера", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'dream_before_restailing'}))],
        [InlineKeyboardButton("Произведенный в РФ", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'dream_rf'}))],
        [InlineKeyboardButton("Самостоятельно посмотреть версию ПО в настройках мультимедиа", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'dream_check_po'}))],
        [InlineKeyboardButton("Не удалось разобраться с версиями ПО", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'dream_help'}))]
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Выберите из предложенных вариантов",
        reply_markup=reply_markup
    )

async def show_variants_passions_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("Узнать последнюю, актуальную версию", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'passions_last_versions'}))],
        [InlineKeyboardButton("Самостоятельно посмотреть версию ПО в настройках мультимедиа", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'passions_last_versions_yourself'}))],
        [InlineKeyboardButton("Не удалось разобраться с версиями ПО", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'passion_help'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Выберите из предложенных вариантов",
        reply_markup=reply_markup
    )

async def show_update_po_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("Да", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'update_po_yes'}))],
        [InlineKeyboardButton("Нет", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'update_new_po_no'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="ПО мультимедийной системы на Вашем VOYAH работает некорректно?",
        reply_markup=reply_markup
    )
async def show_error_car_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("Да", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'error_car_yes'}))],
        [InlineKeyboardButton("Нет", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'error_car_no'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Установлено ли в автомобиле ПО от сторонних поставщиков, то есть установленное не в авторизованном дилерском центре VOYAH?",
        reply_markup=reply_markup
    )

async def show_internet_error_car_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    connection_subbuttons = [
        [InlineKeyboardButton("Да", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'internet_error_yes'}))],
        [InlineKeyboardButton("Нет", callback_data=json.dumps({"s": 'multimedia_i_po', "t": 'internet_error_no'}))],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Закончился лимит трафика Интернета или не пополнили своевременно баланс?",
        reply_markup=reply_markup
    )

async def handle_action_multimedia_i_po(query: CallbackQuery, action_type: str, context: ContextTypes.DEFAULT_TYPE, callback: Callable[
    [
        Update | CallbackQuery,
        ContextTypes.DEFAULT_TYPE
    ],
    Awaitable[None]
]):
   messages = {
    'about_cheap_nxp': {
        'text': 'Вы можете приобрести в любом официальном дилерском центре VOYAH - блок мультимедийной системы (составляющим компонентом которого является чип) и заменить его. Стоимость блока мультимедийной системы и работ необходимо уточнять у Вашего дилера VOYAH. Дополнительно обращаем внимание, что отдельно чипы (от блока мультимедийной системы) не поставляются и не меняются в РФ.',
        'question': 'О замене чипа мультимедийной системы - NXP на Snapdragon 8155'
    },
    'old_po_in_car': {
        'text': 'Обращаем внимание, что текущая версия ПО обеспечивает стабильность и безопасность работы мультимедийной системы Вашего VOYAH.\nУстановленное ПО прошло всестороннее тестирование, соответствует необходимым требованиям и обеспечивает необходимую функциональность. Если нет выявленных проблем с производительностью или безопасностью, в обновлении нет необходимости. Одна из основных задач ПО мультимедийной ситемы, в числе прочего, обеспечивать тот функционал, который указан в "Спецификации" к Вашему VOYAH. Само по себе отсутствие обовления ПО не является недостатком автомобиля или его неисправностью.',
        'question': 'В мультимедийной системе автомобиля установлено не свежее ПО'
    },
    'update_po_internet': {
        'text': 'Данная возможность на данный момент не предусмотрена на автомобилях VOYAH в РФ, однако не исключено, что в будущем данная возможность будет реализована. На текущий момент обновление ПО без визита в авторизованный дилерский центр VOYAH - невозможно.',
        'question': 'Обновление ПО без визита к Дилеру, то есть через интернет.'
    },
    'reload_multimedia': {
        'text': 'Перезагрузить мультимедийную систему возможно следующим путем: \nЗажав на рулевом колесе кнопки "*" и "трубка" и удерживать в течение 10 сек.',
        'question': 'Как перезагрузить мультимедийную систему?'
    },
    'voyah_store': {
        'text': 'VOYAH STORE - магазин приложений с предустановленными популярными приложениями навигации, музыки, интернет-радио, просмотром фильмов. VOYAH STORE доступен для установки на автомобилях приобретенных у официальных дилеров бренда: VOYAH FREE в комплектации H97C (Sport Edition), а также DREAM EVR в комплектации H56B.\nО сроках доступности VOYAH STORE для автомобилей VOYAH FREE в комплектации H97, H97A, H97Z, а также DREAM EVR в комплектации H56, H56A, H56Z будет сообщено дополнительно. На данный момент VOYAH STORE для указанных моделей находится в стадии разработки, адаптации, тестирования.',
        'question': 'VOYAH STORE'
    },
    'save_settings': {
        'text': 'Режим вождения принудительно переходит в самый экологичный при каждом запуске автомобиля для удовлетворения экологических требований в различных странах.',
        'question': 'Как сохранять режимы вождения при перезапуске автомобиля? '
    },
    'voice_control': {
        'text': 'Голосовое управление не включено в список комплектации автомобиля, но мы работаем над его реализацией для использования на русском языке.',
        'question': 'Как активировать голосовое управление?'
    },
    'party_application': {
        'text': 'Установка непроверенных сторонних приложений, в т.ч из таких магазинов приложений как Rustore, не может гарантировать исправную работу мультимедийной системы автомоибля. Необходимый набор навигационных и развлекательных приложений можно скачать в магазине приложений VOYAH STORE. Подробнее см. в разделе "VOYAH STORE".',
        'question': 'Как скачать стороннее приложение?'
    },
    'free_cheep_nxp': {
		'text': 'Последняя версия ПО для мультимедийной системы с чипом NXP - rc45',
        'question': 'Имеется ли на автомобиле VOYAH FREE, с чипом NXP новая версия ПО?'
	},
    'free_sheep_snapdragon': {
		'text': 'Последняя версия ПО для мультимедийной системы с чипом 8155 - rc 2.1.',
        'question': 'Имеется ли на автомобиле VOYAH FREE, с чипом Snapdragon 8155 новая версия ПО?'
	},
    'free_cheep_sport_edition': {
		'text': 'Последняя версия ПО для мультимедийной системы VOYAH FREE SPORT EDITION импортированных из Китая и произведенных в РФ - 4.1, 5.1 (идентичное ПО, не имеющее между собой отличий).',
        'question': 'Имеется ли на автомобиле VOYAH FREE, с чипом VOYAH FREE SPORT EDITION новая версия ПО?'
	},
    'free_unknow_cheep_1': {
		'text': 'Чтобы узнать, какая версия ПО установлена в мультимедийной системе Вашего VOYAH FREE, перейдите в настройки - система. Во второй части названия "Версия программного обеспечения" указана установленная версия, например: AE.01.20240918125630.rc5.1.user. То есть rc5.1 и есть версия ПО в указанном случае.',
        'question': 'Имеется ли на автомобиле VOYAH FREE, новая версия ПО?'
	},
    'hide_functions_after_update': {
		'text': f'Укажите VIN автомобиля, вложите фото экрана мультимедийной системы перейдя в пункт "настройки" -> "система". Отправьте информацию нашей поддержке - {HELPER_BOT_USERNAME}.Мы ознакомимся с предоставленной Вами информацией и предоставим ответ.',
        'question': 'После обновления ПО мультимедиа, автомобиль работает неадекватно'
	},
    'dream_after_restailing': {
		'text': 'Последняя версия ПО для мультимедийной системы - rc 1.6.',
        'question': 'Имеется ли на автомобиле VOYAH DREAM (Дорестайлинговый (H56/H56A)), новая версия ПО?'
	},
    'dream_before_restailing': {
		'text': 'Последняя версия ПО для мультимедийной системы -rc 4.1, rc 7.1.',
        'question': 'Имеется ли на автомобиле VOYAH DREAM ((Рестайнговый (H56B), импорт из Китая, купленный у Дилера), новая версия ПО?'
	},
    'dream_rf': {
		'text': 'Последняя версия ПО для мультимедийной системы - rc 7.1.',
        'question': 'Имеется ли на автомобиле VOYAH DREAM (произведенный в РФ), новая версия ПО?'
	},
    'dream_check_po': {
		'text': 'Чтобы узнать, какая версия ПО установлена в мультимедийной системе Вашего VOYAH DREAM, перейдите в настройки - система. Во второй части названия "Версия программного обеспечения" указана установленная версия, например: AE.01.20240918125630.rc4.1.user. То есть rc4.1 и есть версия ПО в указанном случае.',
        'question': 'Имеется ли на автомобиле VOYAH DREAM, новая версия ПО?'
	},
    'passions_last_versions': {
		'text': 'Последняя версия ПО для мультимедийной системы - 2.5.33.4-20240815173729',
        'question': 'Имеется ли на автомобиле VOYAH PASSIONS, новая версия ПО? Интересует последняя, актуальная версия'
	},
    'passions_last_versions_yourself': {
		'text': 'Самостоятельно посмотреть версию ПО в настройках мультимедиа',
        'question': 'Имеется ли на автомобиле VOYAH PASSIONS, новая версия ПО?'
	},
    'free_unknow_cheep_help': {
		'text': f'Укажите VIN автомобиля, вложите фото экрана мультимедийной системы перейдя в пункт "настройки" -> "система". Отправьте информацию нашей поддержке - {HELPER_BOT_USERNAME}.Мы ознакомимся с предоставленной Вами информацией и предоставим ответ.',
        'question': 'Имеется ли на автомобиле VOYAH FREE, новая версия ПО?'
	},
    'dream_help': {
		'text': f'Укажите VIN автомобиля, вложите фото экрана мультимедийной системы перейдя в пункт "настройки" -> "система". Отправьте информацию нашей поддержке - {HELPER_BOT_USERNAME}.Мы ознакомимся с предоставленной Вами информацией и предоставим ответ.',
        'question': 'Имеется ли на автомобиле VOYAH Dream, новая версия ПО?'
	},
    'passion_help': {
		'text': f'Укажите VIN автомобиля, вложите фото экрана мультимедийной системы перейдя в пункт "настройки" -> "система". Отправьте информацию нашей поддержке - {HELPER_BOT_USERNAME}.Мы ознакомимся с предоставленной Вами информацией и предоставим ответ.',
        'question': 'Имеется ли на автомобиле VOYAH Passion, новая версия ПО?'
	},
    'update_po_yes': {
		'text': 'Для более точного определения неисправности существующей на Вашем автомобиле, рекомендуем провести диагностику у любого официального дилера VOYAH в России. С полным списком дилеров Вы можете ознакомится на нашем официальном сайте: https://voyah.su/voyah-space/dealerships, запись возможно осуществить заполнив форму обратной связи: https://voyah.su/voyah-service/service-form?mobile',
        'question': 'Как обновить ПО мультимедийной системы на более свежее? ПО мультимедийной системы на Вашем VOYAH работает некорректно'
	},
    'update_new_po_no': {
		'text': 'Обновление ПО осуществляется при проявлении неисправностей/некорректной работе автомобиля. Если неисправность/нарекания отсутствует, но Вы желаете установить новое ПО, то данная услуга является платной.',
        'question': 'Как обновить ПО мультимедийной системы на более свежее? ПО мультимедийной системы на Вашем VOYAH работает корректно'
	},
    'error_car_yes': {
		'text': '1 - возможно, что проблема из-за стороннего ПО. Вы можете самостоятельно удалить дополнительные ПО в разделе "Настройки - система" нажать "Сброс до заводских".\n2 - рекомендуем обратиться к установщикам стороннего ПО для устранения проблемы или отката ПО на штатное.',
        'question': 'Почему после обновления ПО в мультимедийной системе, некоторые функции автомобиля работают неадекватно? В автомобиле установлено ПО от сторонних поставщиков'
	},
    'error_car_no': {
		'text': 'Для более точного определения неисправности существующей на Вашем автомобиле, рекомендуем провести диагностику у любого официального дилера VOYAH в России. С полным списком дилеров Вы можете ознакомиться на нашем официальном сайте: https://voyah.su/voyah-space/dealerships, запись возможно осуществить, заполнив форму обратной связи: https://voyah.su/voyah-service/service-form?mobile ',
        'question': 'Почему после обновления ПО в мультимедийной системе, некоторые функции автомобиля работают неадекватно? В автомобиле не установлено ПО от сторонних поставщиков'
	},
    'internet_error_yes': {
		'text': 'Требуется пополнить баланс SIM-карты, как это осуществить см. в разделе "SIM для доступа к интернету в мультимедийной системе"',
        'question': 'Почему в автомобиле не работает интернет? Израсходован "Интернет" или не пополнен баланс'
	},
    'internet_error_no': {
		'text': 'В случае если проблема не связана с наличием трафика или в нулевым балансом, то проблема может быть в самой SIM - карта в блоке T-BOX (износилась, повредилась и т.д), в котором установлена SIM - карта или в ПО мультимедийной системы. Для более точного определения неисправности существующей на Вашем автомобиле, рекомендуем провести диагностику у любого официального дилера VOYAH в России. С полным списком дилеров Вы можете ознакомиться на нашем официальном сайте: https://voyah.su/voyah-space/dealerships, запись возможно осуществить, заполнив форму обратной связи: https://voyah.su/voyah-service/service-form?mobile ',
        'question': 'Почему в автомобиле не работает интернет?'
	},


}

   if 'ss' in action_type and action_type['ss'] == 'update_po':
       await show_new_po_subsection(query, context)
   elif 'ss' in action_type and action_type['ss'] == 'update_po_free':
       await show_variants_free_subsection(query, context)
   elif 'ss' in action_type and action_type['ss'] == 'update_po_dream':
       await show_variants_dream_subsection(query, context)
   elif 'ss' in action_type and action_type['ss'] == 'update_po_passion':
       await show_variants_passions_subsection(query, context)
   elif 'ss' in action_type and action_type['ss'] == 'update_po_free_know_cheep':
       await show_know_cheap_subsection(query, context)
   elif 'ss' in action_type and action_type['ss'] == 'update_po_free_unknow_cheep':
       await show_unknow_cheap_subsection(query, context)
   elif 'ss' in action_type and action_type['ss'] == 'how_update_po':
       await show_update_po_subsection(query, context)
   elif 'ss' in action_type and action_type['ss'] == 'errors_after_update':
       await show_error_car_subsection(query, context)
   elif 'ss' in action_type and action_type['ss'] == 'internet_error':
       await show_internet_error_car_subsection(query, context)
   else:
       await callback(query, messages[action_type['t']]['text'], context, messages[action_type['t']]['question'])
