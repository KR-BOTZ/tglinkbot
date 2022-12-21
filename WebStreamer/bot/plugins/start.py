import urllib.parse
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant



db = Database(Var.DATABASE_URL, Var.SESSION_NAME)

########################## BUTTO TXT ########################## 

START_TEXT = """
**⍟ Hᴇʟʟᴏ Mʏ Fʀɪᴇɴᴅ {} ⍟ \n \n ⍟ Mʏ Nᴀᴍᴇ Iꜱ [『Fɪʟᴇs 2 Lɪɴᴋ Bᴏᴛ』](https://t.me/KR_File2link_Bot)
✌︎ I Aᴍ PᴏᴡᴇʀFᴜʟ 🧛‍♂️ Fɪʟᴇs 2 Lɪɴᴋ Bᴏᴛ  
 🚀 Sᴇᴇ Mʏ Pᴏᴡᴇʀ ⚡.....!!
⚜️ Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us 💖......!!!
**
"""
HELP_TEXT = """
🎆 𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐅𝐈𝐋𝐄𝐒 𝟐 𝐋𝐈𝐍𝐊 𝐁𝐎𝐓
**🔘 Sᴇɴᴅ Mᴇ Aɴʏ Fɪʟᴇ (Oʀ) Mᴇᴅɪᴀ Fʀᴏᴍ Tᴇʟᴇɢʀᴀᴍ....
🔘 Tʜɪs Bᴏᴛ Wɪʟʟ Sᴇɴᴅ Yᴏᴜ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ
🔘 Tʜɪs Lɪɴᴋ Cᴀɴ Bᴇ Usᴇᴅ Tᴏ Dᴏᴡɴʟᴏᴀᴅ Oʀ Sᴛʀᴇᴀᴍ Fɪʟᴇs[Usɪɴɢ Exᴛᴇʀɴᴀʟ Vɪᴅᴇᴏ Pʟᴀʏᴇʀ] Tʜʀᴏᴜɢʜ Mʏ Sᴇʀᴠᴇʀ
🔘 Fᴏʀ Sᴛʀᴇᴀᴍɪɴɢ Jᴜsᴛ Cᴏᴘʏ Tʜᴇ Mᴏɴᴏ Lɪɴᴋ Aɴᴅ Pᴀsᴛᴇ Iᴛ Iɴ Yᴏᴜʀ Vɪᴅᴇᴏ Pʟᴀʏᴇʀ Tᴏ Sᴛᴀʀᴛ Sᴛʀᴇᴀᴍɪɴɢ
🔘 Tʜɪs Bᴏᴛ Sʜᴀʀᴇs Tʜᴇ Pᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ Tᴏ Yᴏᴜ.
🔘 Tʜɪs Bᴏᴛ Is Aʟsᴏ Sᴜᴘᴘᴏʀᴛᴇᴅ Iɴ Cʜᴀɴɴᴇʟs. Aᴅᴅ Mᴇ Tᴏ Cʜᴀɴɴᴇʟ As Aᴅᴍɪɴ Tᴏ Mᴀᴋᴇ Mᴇ Wᴏʀᴋᴀʙʟᴇ...!
🔘 Fᴏʀ Mᴏʀᴇ IɴFᴏʀᴍᴀᴛɪᴏɴ : @KR_Join

🔹𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸
🔞 𝐏𝐨𝐫𝐧 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐋𝐞𝐚𝐝𝐬 𝐘𝐨𝐮 𝐓𝐨 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐁𝐚𝐧 𝐅𝐫𝐨𝐦 𝐀𝐥𝐥 𝐁𝐨𝐭𝐬
️ 
⚜️ Bᴏᴛ Aɴʏ Issᴜᴇs Cᴏɴᴛᴀᴄᴛ Mᴇ
@MrTamil_KiD **
"""

ABOUT_TEXT = """
<b>╔══❰ 𝗙𝗜𝗟𝗘𝗦 𝟮 𝗟𝗜𝗡𝗞 𝗕𝗢𝗧 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖 Mʏ Nᴀᴍᴇ : <a href='https://t.me/KR_File2link_Bot'>『Fɪʟᴇs 2 Lɪɴᴋ Bᴏᴛ』</a>
║┣⪼👦 Oᴡɴᴇʀ : <a href=https://t.me/MR_tamil_kid>Ꮋ ค ℘ ℘ ꪗ 👻 Ҝiᗪ</a>
║┣⪼👨‍💻 Dᴇᴠ : <a href=https://t.me/LastDrogz>Lᴀsᴛ 🐲 Dʀᴏɢᴢ</a>
║┣⪼📢 Uᴘᴅᴀᴛᴇ : <a href=https://t.me/kr_botz>𝗞𝗥 ⚠︎ 𝗕ᴏᴛᴢ</a>
║┣⪼❣️ Sᴜᴘᴘᴏʀᴛ : <a href=https://t.me/kr_join>𝗞𝗥 👽 𝗝ᴏɪɴ</a>
║┣⪼📡 Sᴇʀᴠᴇʀ : <a href=https://t.me/MRtamil_kid>𝗩𝗣𝗦</a>
║┣⪼🗣️ Lᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>Pʏᴛʜᴏɴ3</a>
║┣⪼📚 Lɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>Pʏʀᴏɢʀᴀᴍ</a>  
║┣⪼🗒️ Vᴇʀsɪᴏɴ : V 1.0.0 [ Bᴇᴛᴀ ]
║╰━━━━━━━━━━━━━━━➣
╚═════❰ @KR_Botz ❱═════❍ </b>
"""
DON_TXT = """
<b>💗 𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐬𝐡𝐨𝐰𝐢𝐧𝐠 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐢𝐧 𝐝𝐨𝐧𝐚𝐭𝐢𝐨𝐧
Dᴏɴᴀᴛᴇ Us Tᴏ Kᴇᴇᴘ Oᴜʀ Sᴇʀᴠɪᴄᴇs Cᴏɴᴛɪɴᴏᴜsʟʏ Aʟɪᴠᴇ 😢
Yᴏᴜ Cᴀɴ Sᴇɴᴅ Aɴʏ Aᴍᴏᴜɴᴛ 
Dᴏɴᴀᴛᴇ Oɴʟʏ Oɴᴇ Rᴜᴘᴇᴇ 🥲
Of 10₹, 20₹, 30₹, 50₹, 70₹, 100₹, 200₹ 😊
📨 Pᴀʏᴍᴇɴᴛ Mᴇᴛʜᴏᴅs:
 
GᴏᴏɢʟᴇPᴀʏ / Pᴀʏᴛᴏɴ / PʜᴏɴPᴀʏ / PᴀʏPᴀʟ
 
 Oʀ Dᴏɴᴀᴛᴇ: Mᴇssᴀɢᴇ Mᴇ @MR_Tamil_KiD </b>
"""

DEV_TXT = "Nothing 🤨"



########################## BUTTONS TXT ########################## 

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎', url=f'http://t.me/mr_tamil_kid')
        ],[
        InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://t.me/kr_botz'),
        InlineKeyboardButton('⚡ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/kr_join')
        ],[
        InlineKeyboardButton("👨‍💻 Mʏ Fᴀᴛʜᴇʀ", url="https://t.me/mrtamil_kid")
        ],[
        InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("💸 Dᴏɴᴀᴛᴇ", callback_data="don")
        ],[
        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="home"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
        ]]
    )

ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(' Dᴏɴᴀᴛᴇ 💸 Mᴇ ', callback_data='don')
        ],[
        InlineKeyboardButton("📢 Uᴘᴅᴀᴛᴇ", url= "https://t.me/KR_Botz"),
        InlineKeyboardButton("👨‍💻 Dᴇᴠs 🥷", callback_data = "dev")
        ],[
        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "home"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
        ]]
    )

DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Pᴀʏ 💰 Aᴍᴏᴜɴᴛ",
                                             url="https://t.me/mr_tamil_kid")
        ],[
        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="home"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
        ]]
    ) 

DEV_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton('๑۩ tค๓เl ۞ التاميل ۩๑', url='https://t.me/mr_tamil_kid'),
        ],[
        InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data = "about"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
        ]]
    ) 



@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS
        )
    elif update.data == "dev":
        await update.message.edit_text(
            text=DEV_TXT,
            reply_markup=DEV_BUTTONS
        )
    elif update.data == "don":
        await update.message.edit_text(
            text=DON_TXT,
            reply_markup=DONATE_BUTTONS
        )
    else:
        await update.message.delete()

def get_media_file_size(m):
    media = m.video or m.audio or m.document
    if media and media.file_size:
        return media.file_size
    else:
        return None


def get_media_file_name(m):
    media = m.video or m.document or m.audio
    if media and media.file_name:
        return urllib.parse.quote_plus(media.file_name)
    else:
        return None


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text=" **Sᴏʀʀʏ Sɪʀ, Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ Tᴏ Usᴇ Mᴇ. Cᴏɴᴛᴀᴄᴛ Mʏ [𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗥𝗢𝗨𝗣](https://t.me/kr_join).**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Jᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</i> <b><a href='http://t.me/Kr_Join'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_photo(
            photo="https://graph.org/file/c72af6f77c6d164b81dd2.jpg",
            caption=START_TEXT.format(m.from_user.first_name, m.from_user.id),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [[
                InlineKeyboardButton('♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎', url=f'http://t.me/mr_tamil_kid')
                ],[
                InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://t.me/kr_botz'),
                InlineKeyboardButton('⚡ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/kr_join')
                ],[
                InlineKeyboardButton("👨‍💻 Mʏ Fᴀᴛʜᴇʀ", url="https://t.me/mrtamil_kid")
                ],[
                InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
                InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
                ]]
            )
        )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**𝘚𝘰𝘳𝘳𝘺 𝘚𝘪𝘳, 𝘠𝘰𝘶 𝘈𝘳𝘦 𝘉𝘢𝘯𝘯𝘦𝘥 𝘛𝘰 𝘜𝘴𝘦 𝘔𝘦. 𝘊𝘰𝘯𝘵𝘢𝘤𝘵 𝘔𝘺 [𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽](https://t.me/kr_join).**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ**!\n\n**Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ**!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")],
                         [InlineKeyboardButton("🔄 Refresh / Try Again", url=f"https://t.me/{(await b.get_me()).username}?start=MrTamilKiD_{usr_cmd}")
                        
                        ]]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍʏ [𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽](https://t.me/kr_join).**",
                    parse_mode="markdown", 
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))
        file_name = get_media_file_name(get_msg)
        file_size = humanbytes(get_media_file_size(get_msg))

        stream_link = "{}/{}/{}".format(Var.DOMAIN,get_msg.message_id, file_name) if Var.ON_HEROKU or Var.NO_PORT else \
            "{}/{}/{}".format(Var.DOMAIN,
                                     get_msg.message_id,
                                     file_name)

        msg_text ="""
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <code>{}</code>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🚸 Nᴏᴛᴇ : Lɪɴᴋ ᴇxᴘɪʀᴇᴅ ɪɴ 24 ʜᴏᴜʀꜱ</b>\n
<b>🍃 Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : ©️ @KR_BOTZ</b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ 📥", url=stream_link)]])
        )



@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_photo(
        photo="https://graph.org/file/c72af6f77c6d164b81dd2.jpg",
        caption=ABOUT_TEXT.format(update.from_user.mention),
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ Mʏ [𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽](https://t.me/kr_join).**",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_photo(
        photo="https://graph.org/file/c72af6f77c6d164b81dd2.jpg",
        caption=HELP_TEXT,
        parse_mode="HTML",
        reply_markup=HELP_BUTTONS
        )

