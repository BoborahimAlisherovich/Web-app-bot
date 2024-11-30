from aiogram import Bot, Dispatcher, F, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

API_TOKEN = "7150380677:AAHOQ-WwfPN1Xd-W4_-KOhLXJPT0aWLgh0M"

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher()

current_link_message_id = None


@dp.message(F.text)
async def handle_link(message: types.Message):
    global current_link_message_id

    new_link = message.text.strip()

    if not new_link.startswith("http://") and not new_link.startswith("https://"):
        await message.reply(" link yuboring")
        return

    if current_link_message_id:
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=current_link_message_id)
        except Exception as e:
            print(f"Xatolik xabarni o'chirishda: {e}")

    web_app_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Web3 App-ni ochish", web_app=WebAppInfo(url=new_link))]
        ]
    )


    sent_message = await message.reply("Havolangizga o'tish uchun tugmani bosing:", reply_markup=web_app_button)


    current_link_message_id = sent_message.message_id


if __name__ == "__main__":
    dp.run_polling(bot)
