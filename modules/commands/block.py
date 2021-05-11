#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
from telethon.tl import functions

async def block(client, chat_id, username):
    try:
        await client(functions.contacts.BlockRequest(id = username))
        await client.send_message(chat_id, "Se ha bloqueado al usuario **{}**.".format(username))
    except Exception as error:
        await client.send_message(chat_id, "Ocurrió un problema, no se puede bloquear al usuario **{}**.".format(username))