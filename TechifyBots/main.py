from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
import httpx
import asyncio
from config import *
import random
from .database import tb
from shortzy import Shortzy
from config import *
from Script import text

async def short_link(link, user_id):
    usite = await tb.get_value("shortner", user_id=user_id)
    uapi = await tb.get_value("api", user_id=user_id) 
    shortzy = Shortzy(api_key=uapi, base_site=usite)
    return await shortzy.convert_from_text(link)

async def save_data(tst_url, tst_api, user_id):
    shortzy = Shortzy(api_key=tst_api, base_site=tst_url)
    link=f"https://telegram.me/TechifyBots"
    short = await shortzy.convert(link)        
    if short.startswith("http"):
        await tb.set_shortner(user_id=user_id, shortner=tst_url, api=tst_api)
        return True
    else:
        return False

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(client, message):
    if await tb.get_user(message.from_user.id) is None:
        await tb.add_user(message.from_user.id, message.from_user.first_name)
        bot = await client.get_me()
        await client.send_message(
            LOG_CHANNEL,
            text.LOG.format(
                message.from_user.id,
                getattr(message.from_user, "dc_id", "N/A"),
                message.from_user.first_name or "N/A",
                f"@{message.from_user.username}" if message.from_user.username else "N/A",
                bot.username
            )
        )
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=text.START.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("ℹ️ 𝖠𝖻𝗈𝗎𝗍", callback_data="about"),
             InlineKeyboardButton("📚 𝖧𝖾𝗅𝗉", callback_data="help")],
            [InlineKeyboardButton("💬 𝖥𝖾𝖾𝖽𝖻𝖺𝖼𝗄 💬", url="https://telegram.me/TechifySupport")]
        ])
    )

@Client.on_message(filters.command('shortlink') & filters.private)
async def save_shortlink(c, m):
    if len(m.command) < 3:
        await m.reply_text(
            "**❌ Please provide both the Shortener URL and API key along with the command.\n\nExample: `/shortlink example.com your_api_key`\n\n>❤️‍🔥 By: @TechifyBots**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close", callback_data="close")]]))
        return
    usr = m.from_user
    elg = await save_data(
        m.command[1].replace("/", "").replace("https:", "").replace("http:", ""),
        m.command[2],
        user_id=usr.id
    )
    if elg:
        await m.reply_text(
            f"**✅ Shortener has been set successfully!\n\nShortener URL - {await tb.get_value('shortner', user_id=usr.id)}\nShortener API - {await tb.get_value('api', user_id=usr.id)}\n\n>❤️‍🔥 By: @TechifyBots**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close", callback_data="close")]]))
    else:       
        await m.reply_text("**⚠️ Error:\n\nYour Shortlink API or URL is invalid, please check again!**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close", callback_data="close")]]))

@Client.on_message(filters.command('info') & filters.private)
async def showinfo(c, m):
    usr = m.from_user
    site = await tb.get_value('shortner', user_id=usr.id)
    api = await tb.get_value('api', user_id=usr.id)
    await m.reply_text(
        f"**Your Information\n\n👤 User: {usr.mention}\n🆔 User ID: `{usr.id}`\n\n🌐 Connected Site: `{site}`\n🔗 Connected API: `{api}`\n\n>❤️‍🔥 By: @TechifyBots**",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close", callback_data="close")]]))

@Client.on_message(filters.command("tiny") & filters.private)
async def tiny_handler(client, message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.reply_text("❗ Send a valid URL.\n\n◉ `/tiny https://youtube.com/@techifybots`", quote=True)
        return
    url = parts[1].strip()
    if not url.startswith(("http://", "https://")):
        await message.reply_text("❗ URL must start with http:// or https://", quote=True)
        return
    try:
        async with httpx.AsyncClient() as client_httpx:
            resp = await client_httpx.get(f"http://tinyurl.com/api-create.php?url={url}")
            short_url = resp.text.strip()
        if not short_url.startswith("http"):
            await message.reply_text("❌ TinyURL could not shorten this link. Try a different URL.", quote=True)
            return
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close", callback_data="close")]])
        sent = await message.reply_text(
            f"🔗 **ShortLink:**\n\n`{short_url}`",
            reply_markup=reply_markup
        )
        await asyncio.sleep(300)
        try:
            await sent.delete()
        except Exception:
            pass
    except Exception as e:
        await message.reply_text(f"❌ Failed to shorten using TinyURL: {e}", quote=True)

@Client.on_message(filters.text & filters.private & ~filters.command(["tiny", "stats", " broadcast "]))
async def shorten_link(_, m):
    txt = m.text
    if txt.startswith("/"): return
    if not ("http://" in txt or "https://" in txt):
        await m.reply_text("Please send a valid link to shorten.")
        return
    usr = m.from_user
    try:
        short = await short_link(link=txt, user_id=usr.id)
        msg = f"**✨ 𝐘𝐨𝐮𝐫 𝐒𝐡𝐨𝐫𝐭 𝐋𝐢𝐧𝐤 𝐢𝐬 𝐑𝐞𝐚𝐝𝐲!\n\n🔗 𝗟𝗶𝗻𝗸: <code>{short}</code>\n\n>❤️‍🔥 By: @TechifyBots**"
        await m.reply_text(msg, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("❌ Close", callback_data="close")]]))
    except Exception as e:
        await m.reply_text(f"Error shortening link: {e}")
