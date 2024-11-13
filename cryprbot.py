from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Constants
TOKEN: Final = '7619058464:AAHD0moNP90-IVpPHTagnSPNc7eBi94sCow'
BOT_USERNAME: Final = '@CryptoSwappybot'

# Start Command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi! What can I do for you?')

# Help Command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Hi! I am Kichu, A Scammer bot. Send your crypto and get money instantly through any device, '
        'even as cash through your charging port!!'
    )

# Swap Command
async def swap_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Swap your token')
    await update.message.reply_text('Enter the blockchain of your token')

# Support Command
async def support_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Contact me on Telegram @CryptoSwappybot')

# Function for Simple Text Responses
def get_simple_response(text: str) -> str:
    processed = text.lower()
    if 'hello' in processed:
        return 'Hi! What can I do for you?'
    return "I don't know that. Select a command from the menu!"

# Message Handler
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text
    processed = text.lower()
    
    # Debug Print
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group' and BOT_USERNAME in text:
        new_text = text.replace(BOT_USERNAME, '').strip()
        response = get_simple_response(new_text)
    else:
        response = get_simple_response(text)

    # Example of token selection handling
    if 'bitcoin' in processed:
        response = 'Selected blockchain: Bitcoin'

    print('Bot:', response)
    await update.message.reply_text(response)

# Error Handling
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# Main Function
if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Register Command Handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('swap', swap_command))
    app.add_handler(CommandHandler('support', support_command))

    # Register Message Handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    # Register Error Handler
    app.add_error_handler(error)

    # Polling the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
