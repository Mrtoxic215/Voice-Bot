from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from gtts import gTTS
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("नमस्ते! कोई भी हिंदी में टेक्स्ट भेजिए, मैं उसे आवाज़ में बदल दूंगा।")

async def text_to_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    tts = gTTS(text=text, lang='hi')
    tts.save("voice.mp3")
    await update.message.reply_voice(voice=open("voice.mp3", "rb"))
    os.remove("voice.mp3")

def main():
    app = ApplicationBuilder().token("7449224718:AAFwB-iCGJ2UohorxUXyURi06GNekOStX0g").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), text_to_voice))

    app.run_polling()

if __name__ == "__main__":
    main()
