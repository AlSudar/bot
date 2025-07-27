import json
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
import asyncio
from multimedijnayaSistemaIPo import handle_action_multimedia_i_po, show_multimedia_i_po
from roadHelpSubsections import handle_road_help_voyah, show_road_help_subsections
from serviceGarantySubsections import handle_action_service_garanty, show_service_garanty_subsections
from simCardSubsections import handle_action_simcard, show_simcard_subsections
from sparePartsSubsections import handle_action_spare_parts, show_spare_parts_subsections
from voyahSubsections import handle_action_voyah, show_voyah_subsections
from mainMenu import main_menu_buttons

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
    reply_markup = InlineKeyboardMarkup(main_menu_buttons)
    try:
        await query_or_update.message.reply_text(
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
        privacy_message = "Продолжая, Вы соглашаетесь с Политикой конфиденциальности и Обработкой персональных данных https://voyah.su/privacy.\nДля консультации и обработки Вашего обращения по вопросам, связанным с автомобилями VOYAH, у Вас могут быть запрошены такие данные, как: имя, контактный номер телефона, VIN автомобиля."
        keyboard = [[InlineKeyboardButton("Соглашаюсь", callback_data=json.dumps({"s": 'user_agree'})),
                     InlineKeyboardButton("Отказываюсь", callback_data=json.dumps({"s": 'user_disagree'}))]]
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
    data = json.loads(query.data)
    user_id = query.from_user.id

    # Получаем текущего пользователя из базы данных
    current_user = session.query(User).filter_by(chat_id=user_id).first()
    if data['s'] == "user_agree":  # Пользователь согласился с правилами
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
    elif data['s'] == "user_disagree":  # Пользователь отказался от участия
        if current_user:
            current_user.agreement_status = False  # Меняем статус отказа
            session.commit()
        await query.answer(text="К сожалению, без Вашего согласия мы не сможем обработать Ваши запросы.", show_alert=True)
    elif data['s'] == "app_voyah":
        await show_voyah_subsections(query, context)
    elif data["s"] == "mobile_app":
         await handle_action_voyah(query, data, context, send_message)
    elif data['s'] == "app_multimedijnaya_sistema_i_po":
        await show_multimedia_i_po(query, context)
    elif data["s"] == "multimedia_i_po":
         await handle_action_multimedia_i_po(query, data, context, send_message)
    elif data['s'] == "app_sim_card":
        await show_simcard_subsections(query, context)
    elif data['s'] == "sim_card":
        await handle_action_simcard(query, data, context, send_message)
    elif data['s'] == "app_service_garanty":
        await show_service_garanty_subsections(query, context)
    elif data['s'] == "service_garanty":
        await handle_action_service_garanty(query, data, context, send_message)
    elif data['s'] == "app_spare_parts":
        await show_spare_parts_subsections(query, context)
    elif data['s'] == "spare_parts":
        await handle_action_spare_parts(query, data, context, send_message)
    elif data['s'] == "app_road_help":
        await show_road_help_subsections(query, context)
    elif data['s'] == "road_help":
        await handle_road_help_voyah(query, data, context, send_message)
    elif data["s"] == "cancel":
        reply_markup = InlineKeyboardMarkup(main_menu_buttons)
        await query.edit_message_text(
        text="Выберите интересующий Вас раздел:",
        reply_markup=reply_markup
    )
    else:
        reply_markup = InlineKeyboardMarkup(main_menu_buttons)
        await query.edit_message_text(
        text="Выберите интересующий Вас раздел:",
        reply_markup=reply_markup)

async def send_message(query: CallbackQuery, message: str, context: ContextTypes.DEFAULT_TYPE, question: str = None):
   if question is not None:
    await query.edit_message_text(text=f"Ваш вопрос: {question}")

   await context.bot.send_message(chat_id=query.message.chat_id, text=message)
   await asyncio.sleep(1)
   await show_main_menu(query, context)

def main():

    app = ApplicationBuilder().token(TOKEN).build()


    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, any_message_handler))  # Обработчик всех текстовых сообщений
    app.add_handler(CallbackQueryHandler(button_callback))  # Добавляем обработчик нажатий на кнопки

    print("🚀 Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
