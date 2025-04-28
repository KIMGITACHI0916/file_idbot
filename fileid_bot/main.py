from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        photo = update.message.photo[-1]  # highest quality photo
        await update.message.reply_text(f"Here is the file_id:\n{photo.file_id}")
    else:
        await update.message.reply_text("No photo found!")

app = ApplicationBuilder().token("7685810612:AAEZLD5N7ILobZ2yQ-ZPi5TyAsGwHzkvWl8").build()

app.add_handler(MessageHandler(filters.PHOTO, get_file_id))

app.run_polling()
