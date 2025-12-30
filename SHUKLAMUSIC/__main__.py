# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# -----------------------------------------------
import asyncio
import importlib
import os
from threading import Thread
from flask import Flask  # Flask import kiya

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
import config
from SHUKLAMUSIC import LOGGER, app, userbot
from SHUKLAMUSIC.core.call import SHUKLA
from SHUKLAMUSIC.misc import sudo
from SHUKLAMUSIC.plugins import ALL_MODULES
from SHUKLAMUSIC.utils.database import get_banned_users, get_gbanned

# --- FLASK SERVER SETUP (UPTIME KE LIYE) ---
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Stranger Music Bot Is Alive & Running! 🎵"

def run_web():
    # Render ka PORT uthayega ya default 8080 use karega
    port = int(os.environ.get("PORT", 8080))
    web_app.run(host="0.0.0.0", port=port)

def start_web_server():
    # Alag thread me server start karo taaki bot block na ho
    t = Thread(target=run_web)
    t.daemon = True
    t.start()
# -------------------------------------------

async def init():
    # Sabse pehle Web Server start karo
    start_web_server()
    LOGGER("SHUKLAMUSIC").info("Fʟᴀsᴋ Sᴇʀᴠᴇʀ Sᴛᴀʀᴛᴇᴅ Fᴏʀ Uᴘᴛɪᴍᴇ ⚡")

    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SHUKLAMUSIC.plugins" + all_module)
    LOGGER("SHUKLAMUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await SHUKLA.start()
    try:
        await SHUKLA.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("SHUKLAMUSIC").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\n𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass
    await SHUKLA.decorators()
    LOGGER("SHUKLAMUSIC").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥 𝗦𝗛𝗜𝗩𝗔𝗡𝗦𝗛\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SHUKLAMUSIC").info("𝗦𝗧𝗢𝗣 𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    
