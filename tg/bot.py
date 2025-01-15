from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram.constants import ParseMode
from config.env import TELEGRAM_BOT_TOKEN
from tg.texts import WELCOME
import logging
from tg.user import TelegramUser

logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # check if chat user exists
    # if exists return start command default info
    # else
    # create user
    # create user wallet

    await context.bot.send_message(chat_id=update.effective_chat.id, text=WELCOME)

async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello settings")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = TelegramUser(update.message.from_user.first_name, update.message.from_user.last_name, update.message.from_user.username, update.message.from_user.id)
    user.create()
    # if (user.create()):
    #     print("user created")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=handle_response(update.message.text), parse_mode=ParseMode.MARKDOWN , reply_markup=reply_markup)

async def new_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    # await query.edit_message_text(text=handle_response(query.data))
    await query.edit_message_text(text=handle_response(query.data), parse_mode=ParseMode.MARKDOWN , reply_markup=reply_markup)

reply_markup = {
    "inline_keyboard": [
        [{"text": "🟢 Switch to Sell", "callback_data": "start_command"}, {"text": "Refresh", "callback_data": "start"}],
        [{"text": "0.5 SOL", "callback_data": "buy_0.5"}, {"text": "1 SOL", "callback_data": "buy_1"}, {"text": "2 SOL", "callback_data": "buy_2"}],
        [{"text": "5 SOL", "callback_data": "buy_5"}, {"text": "10 SOL", "callback_data": "buy_10"}, {"text": "X SOL", "callback_data": "buy_x"}],
        [{"text": "Limit Orders", "callback_data": "limit_orders"}, {"text": "Generate PnL", "callback_data": "generate_pnl"}],
        [{"text": "Back", "callback_data": "back"}, {"text": "Close", "callback_data": "close"}],
    ]
}

def handle_response(text: str):
    print(text)
    return """
🌸 *Bloom Buy*

🌍 Trump is Back · [$TBACK](https://example.com)
`2Kxc8RQV9qvqjrfFKXVkSbUeR9Gmp4359VcpcXeSTwSV`
*Dex:* Raydium V4

💰 *Market Cap:* $24.26K  
💵 *Price:* $0.02426  
💧 *Liquidity:* $7.44K  

🟢 Renounced  
🟢 Freeze  

🤔 No active limit orders  

🖥️ *W1:* `0.321 SOL`

[CA](https://example.com) · [DEX](https://example.com) · [BRD](#) · [PHO](#) · [NEO](#) · [GMGN](#) · [PF](#) · [DOCS](#)

_Last updated:_ `15:08:53.789`
"""

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f'Update {update} caused error {context.error}')
    

def start_bot():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Commands Handler
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("settings", new_start))
    application.add_handler(CallbackQueryHandler(button))
    # application.add_handler(CommandHandler("narratives", narratives))
    # application.add_handler(CommandHandler("wallets", wallets))
    # application.add_handler(CommandHandler("referral", referral))
    # application.add_handler(CommandHandler("withdraw", withdraw))
    # application.add_handler(CommandHandler("help", help))

    # Messages Handler
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors Handler
    application.add_error_handler(error)
    
    application.run_polling()