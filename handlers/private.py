import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/a0f27a6db57911bf3df71.jpg",
        caption=f"""**ðð¡ð¢ð¬ ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦ ðð®ð¬ð¢ð ð¶ ðð¨ð­ ðð®ð§ ðð§ ðð«ð¢ð¯ðð­ð ð¥ ðð©ð¬ ð«ððð«ð¯ðð« ð ðððð¥ â¤ï¸ ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð¬ð¢ð ð§ ðð§ ðð ððð¯ðð¥ð¨ð©ðð ðð² = [Aman ð¬â¤ï¸](https://t.me/itzamanrajput)

âââââââââââââââââââ
â£â
â£â ð¾ð§ððð©ð¤ð§ : [ðððð](https://t.me/itzamanrajput)
â£â
â£â ððªð¥ð¥ð¤ð§ð© : [ððð ðððð](https://t.me/Friends_Chatting_Group3)
â£â
âââââââââââââââââââ
ââââââââââââââââââââââââ

ðð ðð¨ð® ððð¯ð ðð§ð² ðð®ðð¬ð­ð¢ð¨ð§ð¬ ðð§ð ððð¥ð© ðð¡ðð§ ðð¦ ðð² ðð¨ð¬ð¬ = [Aman  â¤ï¸](https://t.me/itzamanrajput)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ Já´ÉªÉ´ Há´Êá´ & Sá´á´á´á´Êá´ â¨", url=f"https://t.me/Friends_Chatting_Group3")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/a0f27a6db57911bf3df71.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ CÊÉªá´á´ Má´ Tá´ Gá´á´ Rá´á´á´ ð", url=f"https://404error")
                ]
            ]
        ),
    )
