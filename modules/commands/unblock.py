#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
from telethon.tl import functions

async def unblock(client, chat_id, username):
    try:
        await client(functions.contacts.UnblockRequest(id = username))
        await client.send_message(chat_id, "Se ha desbloqueado al usuario **{}**.".format(username))
    except Exception as error:
        await client.send_message(chat_id, "Ocurrió un problema, no se puede desbloquear al usuario **{}**.".format(username))