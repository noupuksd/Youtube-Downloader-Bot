from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>,𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 @TSutubebot,\n𝐓𝐡𝐞 𝐌𝐨𝐬𝐭 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐮𝐭𝐮𝐛𝐞 𝐕𝐢𝐝𝐞𝐨 𝐚𝐧𝐝 𝐀𝐮𝐝𝐢𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐞𝐫 𝐢𝐧 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦.𝐏𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐚𝐧𝐲 𝐮𝐭𝐮𝐛𝐞 𝐯𝐢𝐝𝐞𝐨 𝐥𝐢𝐧𝐤 𝐨𝐫 𝐬𝐞𝐚𝐫𝐜𝐡 𝐮𝐬𝐢𝐧𝐠 @vid 𝐢𝐧𝐥𝐢𝐧𝐞 𝐦𝐨𝐝𝐞."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
