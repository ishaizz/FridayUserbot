import asyncio
import os
import time
from datetime import datetime
from userbot.uniborgConfig import Config
from userbot.utils import friday_on_cmd, sudo_cmd
from MediaInfo import MediaInfo
from telegraph import Telegraph, exceptions, upload_file

@friday.on(friday_on_cmd(pattern="mediainfo (.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if reply_message is None:
        await event.edit(
            "Reply To a Media."
        )
    file_path = await borg.download_media(reply_message, Config.TMP_DOWNLOAD_DIRECTORY)
    info = Mediainfo(filename = file_path, cmd = '/app/vendor/ffmpeg/ffprobe')
    infoData = info.getInfo()
    media_info = f"<b> MediaInfo </b> \n"
    media_info += f"<code>{infoData}</code>"
    title_of_page = "MediaInfo By Friday."
    response = telegraph.create_page(title_of_page, html_content=media_info)
    km = response["path"]
    await event.edit(f"**MediaInfo** [Here]({km})")
