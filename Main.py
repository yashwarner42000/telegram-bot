import time
import threading
import telebot

TOKEN = '8868118715:AAH_lOPyrfrkgnF1DwrH7t2jeRx7p5y6B4M'
bot = telebot.TeleBot(TOKEN)

# --- MEDIA FILE IDs ---
PHOTO_ID = 'AgACAgUAAxkBAAMPapZYXc6VQTwdO-gDFzOlGRCtBbgAAtsRaxu92rBUxOtU05H1s64BAAMCAAN3AAM9BA'

VIDEO_IDS = [
    'BAACAgUAAxkBAAMNapZYVHsK8ARhPKLqIdzIV7ueDhEAAkIhAAK92rBU_Z_77njOuAw9BA',
    'BAACAgUAAxkBAAMRapZYXSQcXFdPSDponVkktzYdaG0AAkMhAAK92rBUdacEov_7_SE9BA',
    'BAACAgUAAxkBAAMTapZYY5s-uXDiDHrtvy5_yxpDFigAAkQhAAK92rBUWKKxKd06tHw9BA',
    'BAACAgUAAxkBAAMVapZYaG89YQ1lfXiPilgvdOaIAmwAAkYhAAK92rBUK4QV7-u7EUY9BA',
    'BAACAgUAAxkBAAMXapZYaoA4FuHYlljF0cqSdzEz-mcAAkchAAK92rBUOEBhecuxDwg9BA',
    'BAACAgUAAxkBAAMbapZYcV2wg-NCZBV_HcxP5qSyTBwAAkkhAAK92rBUDl4eYr_s0z49BA'
]

def delete_message_later(chat_id, message_id, delay_seconds=120):
    """Deletes a message after a specified delay in seconds."""
    time.sleep(delay_seconds)
    try:
        bot.delete_message(chat_id, message_id)
        print(f"Message {message_id} deleted successfully.")
    except Exception as e:
        print(f"Failed to delete message {message_id}: {e}")

@bot.message_handler(commands=['start'])
def send_auto_delete_media(message):
    chat_id = message.chat.id
    
    # 1. Send 1 Photo
    try:
        photo_msg = bot.send_photo(
            chat_id, 
            PHOTO_ID, 
            caption="📷 Photo (Self-destructs in 2 mins)"
        )
        threading.Thread(
            target=delete_message_later, 
            args=(chat_id, photo_msg.message_id, 120)
        ).start()
    except Exception as e:
        print(f"Error sending photo: {e}")

    # 2. Send 6 Videos
    for index, video_id in enumerate(VIDEO_IDS, start=1):
        try:
            video_msg = bot.send_video(
                chat_id, 
                video_id, 
                caption=f"🎥 Video {index}/6 (Self-destructs in 2 mins)"
            )
            threading.Thread(
                target=delete_message_later, 
                args=(chat_id, video_msg.message_id, 120)
            ).start()
        except Exception as e:
            print(f"Error sending video {index}: {e}")

print("Bot is running... Open Telegram and send /start")
bot.infinity_polling()
