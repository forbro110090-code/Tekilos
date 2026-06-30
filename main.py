from pyrogram import Client, filters
import os

# Скрипт заберет токен из настроек Рендера
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = Client("my_bot_session", bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.text)
async def auto_reply(client, message):
    await message.reply_text("Привет! Я сейчас занят, отвечу позже. 🤖")

print("Бот успешно запущен!")
app.run()
