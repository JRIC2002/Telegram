#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import platform

async def serverinfo(client, chat_id, telegram, username):
    try:
        campo_1 = "👤 **Usuario:**\t{}".format(username)
        campo_2 = "💾 **Módulos:** 16"
        campo_3 = "📱 **Telethon:**\tv1.21.1"
        campo_4 = "🐍 **Python:**\tv{}".format(platform.python_version())
        campo_5 = "📡 **{}:**\t{}".format(telegram.app, telegram.app_version)
        reply = "\n{}\n{}\n{}\n{}\n{}".format(campo_1, campo_2,campo_3, campo_4, campo_5)
        await client.send_message(chat_id, reply)
    except Exception as error:
        await client.send_message(chat_id, "Ha ocurrido un problema.")