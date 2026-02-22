import telebot
import os

# Pella will pull this from your 'Environment Variables'
API_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        # Step 1: Format text as a monospace block
        # <pre> is used for code blocks; <code> is for inline text
        formatted_text = f"<pre>{message.text}</pre>"
        
        # Step 2: Send the formatted message
        # 'HTML' parse_mode is required for the tags to work
        bot.send_message(message.chat.id, formatted_text, parse_mode='HTML')
        
        # Step 3: Delete the user's original message
        bot.delete_message(message.chat.id, message.message_id)
        
    except Exception as e:
        print(f"Error occurred: {e}")

# 'infinity_polling' keeps the bot running continuously
bot.infinity_polling()
      
