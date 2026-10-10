import random
from pyrogram import Client,enums
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, WebAppInfo
from Script import text
from config import ADMIN, PICS, VERSION

@Client.on_callback_query()
async def callback_query_handler(client, query: CallbackQuery):
    if query.data == "start":
        await query.message.edit_media(
            InputMediaPhoto(
                media=random.choice(PICS),
                caption=text.START.format(query.from_user.mention)
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('ℹ️ 𝖠𝖻𝗈𝗎𝗍', callback_data='about'),
                 InlineKeyboardButton('📚 𝖧𝖾𝗅𝗉', callback_data='help')],
                [InlineKeyboardButton('💬 𝖥𝖾𝖾𝖽𝖻𝖺𝖼𝗄 💬', url='https://telegram.me/TechifySupport', style=enums.ButtonStyle.PRIMARY)]
            ])
        )

    elif query.data == "help":
        await query.message.edit_media(
            InputMediaPhoto(
                media=random.choice(PICS),
                caption=text.HELP
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('📢 𝖴𝗉𝖽𝖺𝗍𝖾𝗌', url='https://telegram.me/Techifybots')],
                [InlineKeyboardButton('↩️ 𝖡𝖺𝖼𝗄', callback_data="start", style=enums.ButtonStyle.PRIMARY),
                 InlineKeyboardButton('❌ 𝖢𝗅𝗈𝗌𝖾', callback_data="close", style=enums.ButtonStyle.DANGER)]
            ])
        )

    elif query.data == "about":
        await query.message.edit_media(
            InputMediaPhoto(
                media=random.choice(PICS),
                caption=text.ABOUT.format(VERSION)
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('📂 𝖲𝗈𝗎𝗋𝖼𝖾 𝖢𝗈𝖽𝖾',url='https://github.com/TechifyBots/ShortLink-Bot')],
                [InlineKeyboardButton('☕ 𝖣𝗈𝗇𝖺𝗍𝖾', callback_data='donate'),
                 InlineKeyboardButton('👨‍💻 𝖢𝗋𝖾𝖺𝗍𝗈𝗋', user_id=int(ADMIN))],
                [InlineKeyboardButton('↩️ 𝖡𝖺𝖼𝗄', callback_data='start', style=enums.ButtonStyle.PRIMARY)]
            ])
        )

    elif query.data == "donate":
        await query.message.edit_media(
            InputMediaPhoto(
                media=random.choice(PICS),
                caption=text.DONATE
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('💳 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖳𝗁𝖾 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋', web_app=WebAppInfo(url='https://techifybots.vercel.app/pay'))],
                [InlineKeyboardButton('↩️ 𝖡𝖺𝖼𝗄', callback_data='about', style=enums.ButtonStyle.PRIMARY),
                 InlineKeyboardButton('❌ 𝖢𝗅𝗈𝗌𝖾', callback_data='close', style=enums.ButtonStyle.DANGER)]
            ])
        )

    elif query.data == "close":
        await query.message.delete()
