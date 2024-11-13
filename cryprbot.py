from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes



TOKEN : Final= '7619058464:AAHD0moNP90-IVpPHTagnSPNc7eBi94sCow'
BOT_USERNAME : Final = '@CryptoSwappybot'

async def start_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi! What can I do for youu?')

async def help_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi! I am Kichu, A Scammer bot. Send your cryto and get money instantly through any device, even as cash through your charging port!!')

async def swap_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Swap your token')
    await update.message.reply_text('Enter the blockchain of your token')
    processed0 : str = text.lower()
    if 'bitcoin' in processed:
        return 'Selected blockchain : Bitcoin'


async def support_command(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Contact me on telegram @CryptoSwappybot')


#Responses

def handle_response(text: str) -> str:

    processed : str = text.lower()
    if 'hello' in processed:
        return 'Hi! What can I do for youu?'
    
    return "I don't know that. Select a command from the menu !! "

async def handle_response(update : Update, context : ContextTypes.DEFAULT_TYPE):
    message_type : str = update.message.chat.type
    text : str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type} : "{text}"')

    if message_type == 'group':
            if BOT_USERNAME in text:
                 new_text : str = text.replace(BOT_USERNAME, '').strip()
                 response : str = handle_response(new_text)
            else:
                 return
    else:
        response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update : Update, context : ContextTypes.DEFAULT_TYPE):
     print(f'Update {update} caused eroor {context.error}')
                 
if __name__ == '__main__':
     
     print("Starting bot...")
     app = Application.builder().token(TOKEN).build()

    # Commands
     app.add_handler(CommandHandler('start', start_command))
     app.add_handler(CommandHandler('help', help_command))
     app.add_handler(CommandHandler('swap', swap_command))
     app.add_handler(CommandHandler('support', support_command))

    #Messages
     app.add_handler(MessageHandler(filters.TEXT, handle_response))

    #Errors
     app.add_error_handler(error)

    #Polls the bot
     print('Polling...')
     app.run_polling(poll_interval = 3)

