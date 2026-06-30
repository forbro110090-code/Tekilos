from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION_STRING = os.environ.get("SESSION_STRING")

app = Client("my_session", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

@app.on_message(filters.private & filters.text)
async def auto_reply(client, message):
    if not message.from_user.is_self:
        await message.reply_text("Привет! Я сейчас занят, отвечу позже. 🤖")

print("Бот успешно запущен!")
app.run()
