import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text("Hello! I’m your bot. How can I help you? 😊")

def help_command(update, context):
    update.message.reply_text("Send a message and I will reply!")

def echo(update, context):
    text = update.message.text
    update.message.reply_text(f"You said: {text}")

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
