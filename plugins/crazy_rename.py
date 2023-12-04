from pyrogram import Client, filters
from asyncio import sleep
from pyrogram.errors import FloodWait
from database.users_chats_db import db
from pyrogram.enums import MessageMediaType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
import humanize
from info import ADMINS , FLOOD, LAZY_MODE, LAZY_RENAMERS
import random

@Client.on_message( filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    if (LAZY_MODE==True):
        if message.from_user.id in ADMINS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"""\n**__𝑊ℎ𝑎𝑡 𝑑𝑜 𝑦𝑜𝑢 𝑤𝑎𝑛𝑡 𝑚𝑒 𝑡𝑜 𝑑𝑜 𝑤𝑖𝑡ℎ 𝑡ℎ𝑖𝑠 𝑓𝑖𝑙𝑒...?__**\n**__𝑂𝑙𝑑 𝐹𝑖𝑙𝑒𝑁𝑎𝑚𝑒__** :- `{filename}`\n\n🗃️ 𝙁𝙞𝙡𝙚 𝙎𝙞𝙯𝙚 :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("✍️ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇ", callback_data="rename"),
                         InlineKeyboardButton("ᴄᴀɴᴄᴇʟ  ❌", callback_data="close_data") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))

        elif message.from_user.id in LAZY_RENAMERS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            try:
                text = f"""\n**__𝑊ℎ𝑎𝑡 𝑑𝑜 𝑦𝑜𝑢 𝑤𝑎𝑛𝑡 𝑚𝑒 𝑡𝑜 𝑑𝑜 𝑤𝑖𝑡ℎ 𝑡ℎ𝑖𝑠 𝑓𝑖𝑙𝑒...?__**\n**__𝑂𝑙𝑑 𝐹𝑖𝑙𝑒𝑁𝑎𝑚𝑒__** :- `{filename}`\n\n🗃️ 𝙁𝙞𝙡𝙚 𝙎𝙞𝙯𝙚 :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("✍️ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇ", callback_data="rename"),
                             InlineKeyboardButton("ᴄᴀɴᴄᴇʟ  ❌", callback_data="close_data") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
                await sleep(FLOOD)
            except FloodWait as e:
                await sleep(e.value)
                text = f"""\n**__𝑊ℎ𝑎𝑡 𝑑𝑜 𝑦𝑜𝑢 𝑤𝑎𝑛𝑡 𝑚𝑒 𝑡𝑜 𝑑𝑜 𝑤𝑖𝑡ℎ 𝑡ℎ𝑖𝑠 𝑓𝑖𝑙𝑒...?__**\n**__𝑂𝑙𝑑 𝐹𝑖𝑙𝑒𝑁𝑎𝑚𝑒__** :- `{filename}`\n\n🗃️ 𝙁𝙞𝙡𝙚 𝙎𝙞𝙯𝙚 :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("✍️ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇ", callback_data="rename") ],
                           [ InlineKeyboardButton("ᴄᴀɴᴄᴇʟ  ❌", callback_data="close_data") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
            except:
                pass
        else:
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"""\n**__𝑊ℎ𝑎𝑡 𝑑𝑜 𝑦𝑜𝑢 𝑤𝑎𝑛𝑡 𝑚𝑒 𝑡𝑜 𝑑𝑜 𝑤𝑖𝑡ℎ 𝑡ℎ𝑖𝑠 𝑓𝑖𝑙𝑒...?__**\n**__𝑂𝑙𝑑 𝐹𝑖𝑙𝑒𝑁𝑎𝑚𝑒__** :- `{filename}`\n\n🗃️ 𝙁𝙞𝙡𝙚 𝙎𝙞𝙯𝙚 :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("✍️ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇ", callback_data="rename")],
                        [InlineKeyboardButton("ᴄᴀɴᴄᴇʟ  ❌", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        return

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    if (message.reply_to_message.reply_markup) and isinstance(message.reply_to_message.reply_markup, ForceReply):
        new_name = message.text
        await message.delete()
        await message.delete()
        media = await client.get_messages(message.chat.id, message.reply_to_message.id)
        file = media.reply_to_message.document or media.reply_to_message.video or media.reply_to_message.audio
        filename = file.file_name
        types = file.mime_type.split("/")
        mime = types[0]
        mg_id = media.reply_to_message.id
        try:
            out = new_name.split(".")
            out[1]
            out_name = out[-1]
            out_filename = new_name
            await message.reply_to_message.delete()
            if mime == "video":
                markup = InlineKeyboardMarkup([[
                    InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="upload_document"),
                    InlineKeyboardButton("🎥 ᴠɪᴅᴇᴏ", callback_data="upload_video")]])
            elif mime == "audio":
                markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                    "📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="doc"), InlineKeyboardButton("🎵 ᴀᴜᴅɪᴏ", callback_data="upload_audio")]])
            else:
                markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="upload_document")]])
            # Lazy-WarninG -> Please Dont chnage anything after this Line 
            await message.reply_text(f"**__𝑆𝑒𝑙𝑒𝑐𝑡 𝑇ℎ𝑒 𝑂𝑢𝑡𝑝𝑢𝑡 𝐹𝑖𝑙𝑒 𝑇𝑦𝑝𝑒__**\n**__𝑁𝑒𝑤 𝐹𝑖𝑙𝑒𝑁𝑎𝑚𝑒__** `{out_filename}`", reply_to_message_id=mg_id, reply_markup=markup)

        except:
            try:
                out = filename.split(".")
                out_name = out[-1]
                out_filename = new_name + "." + out_name
            except:
                await message.reply_to_message.delete()
                await message.reply_text("**Error** :  No  Extension in File, Not Supporting", reply_to_message_id=mg_id)
                return
            await message.reply_to_message.delete()
            if mime == "video":
                markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                    "📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="upload_document"), InlineKeyboardButton("🎥 ᴠɪᴅᴇᴏ", callback_data="upload_video")]])
            elif mime == "audio":
                markup = InlineKeyboardMarkup([[InlineKeyboardButton(
                    "📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="upload_document"), InlineKeyboardButton("🎵 ᴀᴜᴅɪᴏ", callback_data="upload_audio")]])
            else:
                markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("📁 ᴅᴏᴄᴜᴍᴇɴᴛ", callback_data="upload_document")]])
            # Lazy-WarninG -> Please Dont chnage anything after this Line 
            await message.reply_text(f"**__𝑆𝑒𝑙𝑒𝑐𝑡 𝑇ℎ𝑒 𝑂𝑢𝑡𝑝𝑢𝑡 𝐹𝑖𝑙𝑒 𝑇𝑦𝑝𝑒__**\n**__𝑁𝑒𝑤 𝐹𝑖𝑙𝑒𝑁𝑎𝑚𝑒__** :- `{out_filename}`",
                                     reply_to_message_id=mg_id, reply_markup=markup)

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("**yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴy ᴄᴏꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ !!**") 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("**ᴄᴏꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy !!**")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    LazyDev = await message.reply_text("Please Wait ...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await LazyDev.edit("**ᴄᴏꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy !!**")

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**ɢɪᴠᴇ ᴍᴇ ᴀ ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ꜱᴇᴛ.\n\nᴇxᴀᴍᴘʟᴇ:- `/set_caption {filename}\n\n💾 Size: {filesize}\n\n⏰ Duration: {duration}`**")
    caption = message.text.split(" ", 1)[1]
    await db.set_caption(message.from_user.id, caption=caption)
    await message.reply_text("**yᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy ᴀᴅᴅᴇᴅ !!**")

    
@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if not caption:
       return await message.reply_text("**yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴy ᴄᴏꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ !!**")
    await db.set_caption(message.from_user.id, caption=None)
    await message.reply_text("**yᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟy ᴅᴇʟᴇᴛᴇᴅ !!**")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message):
    caption = await db.get_caption(message.from_user.id)  
    if caption:
       await message.reply_text(f"**ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ:-**\n\n`{caption}`")
    else:
       await message.reply_text("**yᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴy ᴄᴏꜱᴛᴏᴍ ᴄᴀᴩᴛɪᴏɴ !!**")
