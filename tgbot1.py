import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from googleapiclient.discovery import build

# API Keys
TELEGRAM_BOT_TOKEN = "7644990389:AAEfIA3KuawO3RudiuKQd9WBHpRfiMJWcpk"
YOUTUBE_API_KEY = "AIzaSyDE1zi98M_QTFR7PJvjVXfLWlxebe2z_-s"

# Logging settings
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Search on YouTube
def get_random_cat_video():
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=random.choice(["cats", "funny cats", "cute kittens", "pets", "cat compilation"]),
        part="snippet",
        type="video",
        maxResults=10
    )
    response = request.execute()
    video = random.choice(response['items'])
    return f"https://www.youtube.com/watch?v={video['id']['videoId']}"

# Message
async def handle_message(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello!")
    video_link = get_random_cat_video()
    await update.message.reply_text(f"Here's a cat video for you: {video_link}")

# Launcher
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
