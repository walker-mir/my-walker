from telethon import TelegramClient, events
import os

API_ID = int(os.environ.get("API_ID") or input("API_ID: "))
API_HASH = os.environ.get("API_HASH") or input("API_HASH: "))
SESSION = os.environ.get("SESSION_NAME", "userbot_session")

client = TelegramClient(SESSION, API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.raw_text.lower() == "ping":
        await event.reply("pong ✅")
    elif event.message.media:
        path = await event.message.download_media()
        await event.reply(f"Файл сохранён: {path}")

if __name__ == "__main__":
    print("🔹 Запуск userbot. При первом запуске введи номер и код из Telegram.")
    client.start()
    client.run_until_disconnected()
