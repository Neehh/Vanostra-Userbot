import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from neehproject import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from neehproject.helpers.misc import create_botlog, heroku
from neehproject.modules import ALL_MODULES

MSG_ON = """
🔥 **Neehh-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"neehproject.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("validc0de")
            await bot.join_chat("hiroosupport")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("neehproject").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("neehproject").info(f"Neeh-Userbot v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    if bot1 and str(BOTLOG_CHATID).startswith("-100"):
        bot1.me = await bot1.get_me()
        chat = await bot1.get_chat(BOTLOG_CHATID)
        desc = "Group Log untuk Neeh-UserBot.\n\nHARAP JANGAN KELUAR DARI GROUP INI.\n\n✨ Powered By ~ @hiroosupport ✨"
        lolo = f"LOGS | FOR {bot1.me.first_name}"
        if chat.description != desc:
            await bot1.set_chat_description(BOTLOG_CHATID, desc)
        if chat.title != lolo:
            await bot1.set_chat_title(BOTLOG_CHATID, lolo)
        await bot1.set_chat_photo(BOTLOG_CHATID, photo="neehproject/resources/asoyy.jpg")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("neehproject").info("Starting Neeh-UserBot")
    install()
    heroku()
    LOOP.run_until_complete(main())
