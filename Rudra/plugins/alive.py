from .. import *

@app.on_message(commandx(["alive"]))
async def alive_check(client, message):
    await message.reply_text("**🥀 I Aᴍ Aʟɪᴠᴇ Mʏ Dᴇᴀʀ Rᴜᴅʀᴀ Mᴀsᴛᴇʀ ✨ ...**")



__NAME__ = "Alive"
__MENU__ = f"""
**🥀 Check Userbot Working
Or Not ..**

**Example:** `.alive`
"""
