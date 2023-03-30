from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler, MessageHandler, PrefixHandler, filters
import os, model
from dotenv import load_dotenv

TOKEN = '6106399754:AAFSZYKa774kDE2aaozTwIs6n20UH0PQrAA'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=" Hello, I am Baymax, your personal healthcare companion. how can i help you?")


async def pneumonia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Please upload your chest X-ray image")


async def photo_xray(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Please wait while we analyze your X-ray image")

    # get image
    file_id = update.message.photo[-1].file_id
    file = await context.bot.get_file(file_id)
    file_path = os.path.join(os.getcwd(), f'storage/{file_id}.jpg')
    await file.download_to_drive(file_path)

    # predict
    prediction = model.get_prediction(file_path)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your X-ray image is {prediction}")


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)

    pneumonia_handler = CommandHandler('pneumonia', pneumonia)
    app.add_handler(pneumonia_handler)

    # get image
    photo_handler = MessageHandler(filters=filters.PHOTO, callback=photo_xray)

    # app.add_handler(echo_handler)
    app.add_handler(photo_handler)
    print("Bot is running")
    app.run_polling()
