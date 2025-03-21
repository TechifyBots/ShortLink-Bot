import os

API_ID = int(os.environ.get("API_ID", "123456"))  # Default to a valid integer
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
BASE_URL = os.environ.get("BASE_URL", "")
DATABASE_URL = os.environ.get("DATABASE_URL", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))  # Default to 0 if not set
ADMINS = int(os.environ.get("ADMINS", "0"))  # Default to 0 if not set
IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"

# Convert AUTH_CHANNEL to a list of integers
AUTH_CHANNELS = os.environ.get("AUTH_CHANNEL", "")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split() if channel_id.strip()]




START_TXT = '''<b>{},

๏ I ᴄᴀɴ Cᴏɴᴠᴇʀᴛ ʏᴏᴜʀ ʟɪɴᴋs ᴛᴏ Sʜᴏʀᴛ ʟɪɴᴋs ᴜsɪɴɢ ʏᴏᴜʀ ᴀᴩɪ.

๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ Hᴇʟᴩ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.

๏ By - @TechifyBots</b>'''

LOG_TEXT = '''<b>#NewUser
    
ID - <code>{}</code>

Name - {}</b>'''

HELP_TXT = '''Send Shortener URL & API along with the command.

Ex: <code>/shortlink example.com api</code>

Now send me any link I will convet that link into your connected Shortener

If you want to remove your Shortener then use <code>/remove</code> command.'''

FORCE_SUBSCRIBE_TEXT = '''<b>{}, Tᴏ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ. Tʜᴇ ʙᴏᴛ ᴡɪʟʟ ɴᴏᴛ ᴘʀᴏᴄᴇss ᴀɴʏ ʀᴇǫᴜᴇsᴛs ᴡɪᴛʜᴏᴜᴛ ᴊᴏɪɴɪɴɢ.

बॉट का उपयोग करने के लिए आपको पहले हमारे चैनल में Join होना होगा। बॉट बिना शामिल हुए किसी भी Request को Process नहीं करेगा।</b>'''

ABOUT_TXT = '''<b>╔════❰ ShortLink Bot ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ Mʏ ɴᴀᴍᴇ -> {}
║ ┣ Mʏ Oᴡɴᴇʀ -> @CallOwnerBot
║ ┣ Uᴘᴅᴀᴛᴇꜱ -> @TechifyBots
║ ┣ 𝖲ᴜᴘᴘᴏʀᴛ -> @TechifySupport
║ ┣ ๏ Cʜᴇᴄᴋ ʜᴇʟᴘ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ.
║ ┗━━━━━━━━━❥
╚═════❰ @ ❱═════❍</b>'''
