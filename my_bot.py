from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    ContextTypes
)
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Подключение к базе данных SQLite
engine = create_engine('sqlite:///users.db')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    chat_id = Column(Integer, unique=True)
    agreement_status = Column(Boolean, default=False)

Base.metadata.create_all(engine)

# Токен, полученный от BotFather
TOKEN = '8016334625:AAGdkO4xslCeNyZHkhhBNfMPqIN148PbPfA'

async def show_main_menu(query_or_update: Update | CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    """Показываем главное меню после согласия с правилами или по запросу пользователя."""
    menu_buttons = [
        [InlineKeyboardButton("Мобильное приложение VOYAH", callback_data='app_voyah')],
        [InlineKeyboardButton("SIM-карта", callback_data='sim_card')],
        [InlineKeyboardButton("Помощь на дорогах", callback_data='road_help')],
        [InlineKeyboardButton("Запасные части", callback_data='spare_parts')],
        [InlineKeyboardButton("Связь со специалистом", url=f't.me/{HELPER_BOT_USERNAME}')],  # Прямая ссылка на чат с другим ботом
    ]
    reply_markup = InlineKeyboardMarkup(menu_buttons)
    try:
        await query_or_update.edit_message_text(
            text="Выберите интересующий Вас раздел:",
            reply_markup=reply_markup
        )
    except AttributeError:
        await query_or_update.message.reply_text(
            text="Выберите интересующий Вас раздел:",
            reply_markup=reply_markup
        )

async def request_agreement(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Запрашиваем согласие с политикой конфиденциальности."""
    user_id = update.effective_user.id
    current_user = session.query(User).filter_by(chat_id=user_id).first()

    if not current_user or current_user.agreement_status != True:
        privacy_message = "Продолжая, Вы соглашаетесь с Политикой конфиденциальности и Обработкой персональных данных https://voyah.su/privacy."
        keyboard = [[InlineKeyboardButton("Соглашаюсь", callback_data="agree"),
                     InlineKeyboardButton("Отказываюсь", callback_data="disagree")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(privacy_message, reply_markup=reply_markup)
    else:
        await show_main_menu(update, context)

async def any_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик любых входящих сообщений (кроме '/start')."""
    await request_agreement(update, context)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обрабатываем нажатия на кнопки."""
    query = update.callback_query
    data = query.data
    user_id = query.from_user.id

    # Получаем текущего пользователя из базы данных
    current_user = session.query(User).filter_by(chat_id=user_id).first()

    if data == "agree":  # Пользователь согласился с правилами
        # Если пользователя нет в базе данных, создаём его
        if not current_user:
            new_user = User(first_name=update.effective_user.first_name,
                            last_name=update.effective_user.last_name,
                            chat_id=user_id,
                            agreement_status=True)
            session.add(new_user)
            session.commit()
            logger.info(f"Новый пользователь {new_user.first_name} ({user_id}) принял правила.")
        else:
            current_user.agreement_status = True  # Меняем статус согласия
            session.commit()
            logger.info(f"Пользователь {current_user.first_name} ({user_id}) подтвердил согласие.")

        await query.answer(text="Спасибо за согласие!")
        await show_main_menu(query, context)  # Показываем основное меню
    elif data == "disagree":  # Пользователь отказался от участия
        if current_user:
            current_user.agreement_status = False  # Меняем статус отказа
            session.commit()
        await query.answer(text="К сожалению, без Вашего согласия мы не сможем обработать Ваши запросы.", show_alert=True)
    elif data == "app_voyah":  # Пользователь выбрал категорию "Мобильное приложение VOYAH"
        await show_app_subsections(query, context)
    else:
        if not current_user or current_user.agreement_status != True:  # Проверяем статус согласия пользователя
            await query.answer(text="Сначала необходимо дать согласие на обработку Ваших персональных данных.", show_alert=True)
            return
        await handle_action(query, data)

async def show_app_subsections(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    """Отображаем подразделы мобильной аппликации."""
    subsections_buttons = [
        [InlineKeyboardButton("1. Для чего нужно это приложение?", callback_data='sub_app_1')],
        [InlineKeyboardButton("2. Кто может воспользоваться приложением?", callback_data='sub_app_2')],
        [InlineKeyboardButton("3. К каким автомобилям можно подключить мобильное приложение?", callback_data='sub_app_3')],
        [InlineKeyboardButton("4. Будет ли доступно подключение к приложению для модели VOYAH PASSION?", callback_data='sub_app_4')],
        [InlineKeyboardButton("5. Как подключить мобильное приложение к автомобилю VOYAH?", callback_data='sub_app_5')],
    ]
    reply_markup = InlineKeyboardMarkup(subsections_buttons)
    await query.edit_message_text(
        text="Выберите интересующий Вас раздел мобильного приложения VOYAH:",
        reply_markup=reply_markup
    )

async def show_connection_subsection(query: CallbackQuery, context: ContextTypes.DEFAULT_TYPE):
    """Отображение подразделов подключения приложения к авто."""
    connection_subbuttons = [
        [InlineKeyboardButton("5.1 Автомобиль VOYAH, произведённый в РФ", callback_data='connect_russia')],
        [InlineKeyboardButton("5.2 Автомобиль VOYAH, произведённый в Китае, но приобретённый у официального дилера в РФ", callback_data='connect_china')],
        [InlineKeyboardButton("5.3 Автомобиль VOYAH, приобретённый по схеме параллельного импорта или в РБ", callback_data='connect_import')],
    ]
    reply_markup = InlineKeyboardMarkup(connection_subbuttons)
    await query.edit_message_text(
        text="Выберите страну происхождения автомобиля:",
        reply_markup=reply_markup
    )

async def send_message(query: CallbackQuery, message: str):
    """Отправляем финальное сообщение пользователю."""
    await query.edit_message_text(message)

async def handle_action(query: CallbackQuery, action_type: str):
    """Основная логика обработки действий (выбор разделов и подразделов)."""
    messages = {
        'sub_app_1': "Приложение VOYAH – это экосистема, которая позволяет управлять функциями Вашего VOYAH с телефона, в любой момент времени иметь полную информацию об автомобиле, всегда держать под рукой карту электрозарядных станций и телефон для быстрой связи с сервисом «Помощь на дорогах».",
        'sub_app_2': "Любой пользователь обладающий смартфоном. В случае если Вы не являетесь владельцем автомобиля VOYAH или Ваш автомобиль не представляется возможным подключить к приложению, то для Вас в приложении доступнен функционал зарядки автомобиля.",
        'sub_app_3': "Подключение к приложению доступно для автомобилей: VOYAH FREE, VOYAH DREAM. Приложение VOYAH может использоваться с автомобилями VOYAH FREE, VOYAH DREAM всех модификаций и годов выпуска. Однако для автомобилей приобретенных по схеме параллельного импорта, а также в РБ, существуют определенные условия для подключения автомобиля (см. в разделе 'Как подключить мобильное приложение к автомобилю VOYAH?'). Рекомендуем обратиться к официальным дилерам для уточнения деталей по этому впоросу. Список дилерских центров представлен на сайте https://voyah.su/voyah-space/dealerships?mobile",
        'sub_app_4': "Для VOYAH PASSION приложение находится в стадии разработки, адаптации, тестирования. Ожидается, что приложение будет доступно для пользователей, к моменту запуска производства данной модели в РФ. ",
        'sub_app_5': "Подключение мобильного приложения к автомобилю доступно для владельцев гибридных и полностью электрических автомобилей FREE и гибридных DREAM. На автомобилях VOYAH произведенных в РФ предустановлено все необходимое оборудование для подключения автомобиля к мобильному приложению. При продаже автомобиля, официальный дилер продавец передает Вам права в приложении как владельцу автомобиля.",
        'connect_russia': "Подключение мобильного приложения к автомобилю доступно для владельцев гибридных и полностью электрических автомобилей FREE и гибридных DREAM. Стоимость установки необходимого оборудования и подключения автомобиля к мобильному приложению VOYAH составляет:\nДля автомобилей VOYAH FREE - 70 000 ₽\nДля автомобилей VOYAH DREAM - 75 000 ₽",
        'connect_china': "Подключение мобильного приложения к автомобилю доступно для владельцев гибридных и полностью электрических автомобилей FREE и гибридных DREAM, ввезенных способом параллельного импорта и подключенных к сервисной программе «ГАРАНТИЯ + ПОДДЕРЖКА» (с более подробным описанием программы, Вы можете ознакомиться по сылке: https://voyah.su/kratkie-usloviya-garantii/warranty-for-gray-cars?footer).",
        'connect_import': "Подключение мобильного приложения к автомобилю доступно для владельцев гибридных и полностью электрических автомобилей FREE и гибридных DREAM, ввезённых способом параллельного импорта..."
    }

    if action_type.startswith('sub_app'):
        if action_type == 'sub_app_5':
            await show_connection_subsection(query, context)
        else:
            await send_message(query, messages[action_type])
    elif action_type.startswith('connect'):
        await send_message(query, messages[action_type])


def main():
    global HELPER_BOT_USERNAME  # Имя специального бота для связи
    HELPER_BOT_USERNAME = "@Motorinvest_HELP_bot"

    app = ApplicationBuilder().token(TOKEN).build()


    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, any_message_handler))  # Обработчик всех текстовых сообщений
    app.add_handler(CallbackQueryHandler(button_callback))  # Добавляем обработчик нажатий на кнопки

    print("🚀 Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
