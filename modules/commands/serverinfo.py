#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import platform

async def serverinfo(client, chat_id, telegram, username):
    try:
        reply = "\n👤 **Usuario:**\t{}\n📱 **Telethon:**\tv1.21.1\n🐍 **Python:**\tv{}\n📡 **{}:**\t{}".format(username, platform.python_version(), telegram.app, telegram.app_version)
        await client.send_message(chat_id, reply)
    except Exception as error:
        await client.send_message(chat_id, "Ha ocurrido un problema.")