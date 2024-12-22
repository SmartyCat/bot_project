from telegram import Update

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)


def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(token="7743437176:AAHTR2dDX78NB80MSzdEJkBne2MyFWC4X-M")
    dispatcher = updater.dispatcher

    start_handler = CommandHandler("start", echo)

    dispatcher.add_handler(start_handler)

    message_handler = MessageHandler(Filters.text, echo)

    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
