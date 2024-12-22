from telegram import Update

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext,
)


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(token="601285821:AAFxvWDSPSfm4tAV1D01f34uq66Wk4HRoG0")
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", echo)

    dispatcher.add_handler(start_handler)

    message_handler = MessageHandler(filters.text, echo)

    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
