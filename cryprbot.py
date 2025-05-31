from typing import Final
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
    ContextTypes
)

# Constants
TOKEN: Final = '#Enter your token'
#Enter your bot username
BOT_USERNAME: Final = '@CryptoSwappybot'

# Define conversation states
SELECT_BLOCKCHAIN, ENTER_TOKEN, ENTER_AMOUNT = range(3)

# Start Command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi! What can I do for you?')

# Swap Command Handler - Initial State
async def swap_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Swap your token.\nEnter the blockchain of your token (e.g., Bitcoin, Ethereum):')
    return SELECT_BLOCKCHAIN

# Handle Blockchain Selection
async def handle_blockchain_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.lower()

    # Example check for "bitcoin"
    if 'bitcoin' in user_input:
        await update.message.reply_text('Selected blockchain: Bitcoin')
        await update.message.reply_text('Enter your token:')
        return ENTER_TOKEN  # Move to the next state

    # If the input is not recognized
    await update.message.reply_text('Unsupported blockchain. Please enter a valid blockchain (e.g., Bitcoin, Ethereum):')
    return SELECT_BLOCKCHAIN  # Stay in the same state

# Handle Token Input
async def handle_token_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_token = update.message.text
    context.user_data['token'] = user_token  # Store the token in context for later use
    await update.message.reply_text(f"Selected token: {user_token}")
    await update.message.reply_text("Enter the amount:")
    return ENTER_AMOUNT  # Move to the next state

# Handle Amount Input
async def handle_amount_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_amount = update.message.text
    context.user_data['amount'] = user_amount  # Store the amount in context for later use
    selected_token = context.user_data.get('token', 'unknown token')
    
    # Respond with the entered details
    await update.message.reply_text(f"Amount entered: {user_amount} for token: {selected_token}")
    await update.message.reply_text("Transaction complete. Thank you!")
    return ConversationHandler.END  # End the conversation

# Cancel Command
async def cancel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Conversation canceled. Use /swap to start again.")
    return ConversationHandler.END

# Error Handling
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# Main Function
if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Conversation Handler for Swap Command
    swap_conv_handler = ConversationHandler(
        entry_points=[CommandHandler('swap', swap_command)],
        states={
            SELECT_BLOCKCHAIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_blockchain_selection)],
            ENTER_TOKEN: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_token_input)],
            ENTER_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_amount_input)],
        },
        fallbacks=[CommandHandler('cancel', cancel_command)],
    )

    # Register Command Handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', start_command))  # Reused start_command for help message
    app.add_handler(CommandHandler('support', start_command))  # Reused start_command for support message

    # Register Conversation Handler
    app.add_handler(swap_conv_handler)

    # Register Error Handler
    app.add_error_handler(error)

    # Polling the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
