from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = "7685810612:AAEZLD5N7ILobZ2yQ-ZPi5TyAsGwHzkvWl8"

async def catch_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        photo = update.message.photo[-1]
        await update.message.reply_text(f"Here is your file_id:\n\n{photo.file_id}")

async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, catch_photo))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
