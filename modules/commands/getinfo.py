#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import os
from telethon.tl.functions.users import GetFullUserRequest
#from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.channels import GetFullChannelRequest

async def userinfo(client, chat_id, username):
    try:
        user_data = await client(GetFullUserRequest(username))
        user = user_data.user
        profile_picture = await client.download_profile_photo(user.id, file = "modules/temp/")
        user_profile = {
            "first_name": "**Nombre:** {}".format(user.first_name),
            "last_name": "**Apellido:** {}".format(user.last_name),
            "username": "**Nombre de usuario:** {}".format(user.username),
            "user_id": "**ID:** {}".format(user.id),
            "user_bot": "**Bot:** {}".format(user.bot),
            "biography": "**Biografía:** {}".format(user_data.about)
        }
        reply = "{}\n{}\n{}\n{}\n{}\n{}".format(user_profile["first_name"], user_profile["last_name"], user_profile["username"], user_profile["user_id"], user_profile["user_bot"], user_profile["biography"])
        await client.send_message(chat_id, reply, file = profile_picture)
        os.remove(profile_picture)
    except Exception as error:
        await client.send_message(chat_id, "Ha ocurrido un problema, es posible que el usuario **{}** no existe.".format(username))

async def gcinfo(client, chat_id, name):
    try:
        if name == ".":
            name = chat_id
        chat_data = await client(GetFullChannelRequest(name))
        full_chat = chat_data.full_chat
        chats = chat_data.chats[0]
        profile_picture = await client.download_profile_photo(full_chat.id, file = "modules/temp/")
        chat_profile = {
            "group_name": "**Nombre del grupo o canal:** {}".format(chats.title),
            "username": "**Nombre de usuario:** {}".format(chats.username),
            "group_id": "**ID:** {}".format(full_chat.id),
            "description": "**Descripción:** {}".format(full_chat.about)
        }
        reply = "{}\n{}\n{}\n{}".format(chat_profile["group_name"], chat_profile["username"], chat_profile["group_id"], chat_profile["description"])
        await client.send_message(chat_id, reply, file = profile_picture, link_preview = False)
        os.remove(profile_picture)
    except Exception as error:
        print(error)
        await client.send_message(chat_id, "Ha ocurrido un problema, es posible que el grupo o canal **{}** no existe.".format(name))