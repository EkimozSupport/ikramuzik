from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>โจ **Merhaba {message.from_user.first_name}** \n
๐ญ **[{BOT_NAME}](https://t.me/Hatiralaramusicbot) Ben telegram Sesli sohbetlerinde ลarkฤฑ dinletebilen Elly & Carl Mรผzik botuyum !**

๐ก **komut listemi รถฤrenmek iรงin Komut butonuna tฤฑklayฤฑnฤฑz ยป ๐ ๐๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฏ๐๐๐๐ผ๐ป !**

โ **๐๐ผ๐ฟ ๐ถ๐ป๐ณ๐ผ๐ฟ๐บ๐ฎ๐๐ถ๐ผ๐ป ๐ฎ๐ฏ๐ผ๐๐ ๐ฎ๐น๐น ๐ณ๐ฒ๐ฎ๐๐๐ฟ๐ฒ ๐ผ๐ณ ๐๐ต๐ถ๐ ๐ฏ๐ผ๐, ๐ท๐๐๐ ๐๐๐ฝ๐ฒ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "โ Add me to your Group โ", url=f"https://t.me/HatiralaraMusicBot?startgroup=true")
                ],[
                    InlineKeyboardButton(
                         "๐ Commands", url="https://t.me/kizilsancakbilgi"
                    ),
                    InlineKeyboardButton(
                        "๐ BOT YAPTIRMAK ฤฐรฤฐN", url=f"https://t.me/kizilsancaksahibi")
                ],[
                    InlineKeyboardButton(
                        "๐ฅ Resmi Grubum", url=f"https://t.me/Smailesi"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ รCRETLฤฐ BOTLAR ", url=f"https://t.me/ucretliBotlar")
                ],[
                    InlineKeyboardButton(
                        "๐ Mango Botlarฤฑ ", url="https://t.me/Kizilsancakbilgi")
                ],[
                    InlineKeyboardButton(
                        "๐ PREMฤฐUM ๐", url="https://t.me/ucretlibotlar"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""โ **bot is running**\n<b>๐? **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โจ Group", url=f"https://t.me/Mangodestek"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ Channel", url=f"https://t.me/Ucretlibotlar"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>๐๐ป **Hello** {message.from_user.mention()}, **please tap the button below to see the help message you can read for using this bot**</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="โ HOW TO USE ME", url=f"https://t.me/HatiralaraMusicBot?start=help"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.mention()}, welcome to help menu โจ
\n๐ HOW TO USE ME ?
\n1. first add me to your group.
2. promote me as admin and give all permission.
3. then, add @{ASSISTANT_NAME} to your group or type /userbotjoin.
3. make sure you turn on the voice chat first before start playing music.
\n๐๐ปโโ๏ธ **commands for all user:**
\n/play (song name) - play song from youtube
/ytp (song name) - play song from youtube directly
/stream (reply to audio) - play song using audio file
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name)ย?- search video from youtube detailed
/vsong (video name)ย?- download video from youtube detailed
/lyric - (song name) lyrics scrapper
/vk (song name) - download song from inline mode
\n๐ท๐ปโโ๏ธ **commands for admins:**
\n/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/reload - for refresh the admin list
/cache - for cleared admin cache
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/silent - mute the music player on voice chat
/unsilent - unmute the music player on voice chat
/musicplayer (on / off) - disable / enable music player in your group
\n๐ง channel streaming commands:
\n/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/admincache - refresh the admin cache
\n๐งโโ๏ธ command for sudo users:
\n/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic
\n๐จ๐ปโโ๏ธ owner only:
\n/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot
\n๐ **commands for fun:**
\n/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself
\n๐ก version 0.6.5 (latest)
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โจ GROUP", url=f"https://t.me/MangoDestek"
                    ),
                    InlineKeyboardButton(
                        "๐ฃ CHANNEL", url=f"https://t.me/ucretlibotlar"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Kendi Botunuz ฤฐรงin ", url=f"https://t.me/Kizilsancaksahibi"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "๐ `PONG!!`\n"
        f"โก๏ธ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "๐ค bot status:\n"
        f"โข **uptime:** `{uptime}`\n"
        f"โข **start time:** `{START_TIME_ISO}`"
    )
