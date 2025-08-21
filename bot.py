from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import re

# Токен, полученный от @BotFather
TOKEN = "7393539832:AAGz78dKT8jeuZl9fJzdXEraycUFHKOMVo0"  # Замени на свой токен

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("напиши да)")

# Обработка текстовых сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()  # Приводим текст к нижнему регистру
    # Проверяем точные совпадения или сообщения, где "да" — отдельное слово в конце с возможными символами до и после
    if text in ["да", "ну да", "мда"] or re.search(r"[?!)(.,:;_-]*\s*\bда\b[?!)(.,:;_-]*$", text):
        await update.message.reply_text("ПИЗДА!")

def main():
    # Создаем приложение
    app = Application.builder().token(TOKEN).build()

    # Регистрируем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    print("Бот запущен...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
