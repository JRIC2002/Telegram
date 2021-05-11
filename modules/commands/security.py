#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import json
from telethon.tl import functions

async def activate(client, chat_id, status):
    with open("modules/config.json", "r") as config_file:
        config = config_file.read()
        config = json.loads(config)
    with open("modules/config.json", "w") as config_file:
        config["security"] = 1
        config_file.write(json.dumps(config))
    await client.send_message(chat_id, "Se activo el modo **seguro**.")

async def desactivate(client, chat_id, status):
    with open("modules/config.json", "r") as config_file:
        config = config_file.read()
        config = json.loads(config)
    with open("modules/config.json", "w") as config_file:
        config_file.seek(0)
        config["security"] = 0
        config_file.write(json.dumps(config))
    await client.send_message(chat_id, "Se desactivo el modo **seguro**.")

async def security(client, chat_id, sender_id):
    messages = await client.get_messages(sender_id, limit = 3)
    if messages.total == 1:
        try:
            async with client.conversation(chat_id, total_timeout = 120) as conv:
                await conv.send_message("Hola 👋")
                while True:
                    await conv.send_message("¿Me conoces?\n1) Sí\n2) No")
                    response = await conv.get_response()
                    msg = response.message
                    msg = msg.lower()
                    if msg == "1" or msg == "si" or msg == "sí":
                        await conv.send_message("Uhmmm...genial, ¿En qué te puedo ayudar?")
                        break
                    if msg == "2" or msg == "no":
                        await conv.send_message("Uhmmm...sospechoso 👀. Bueno, ¿En qué te puedo ayudar?")
                        break
                response = await conv.get_response()
                await conv.send_message("Estarás bloqueado(a) por el momento 👻.\nSi tienes algun grupo en común conmigo, hablame por ahi, para poder desbloquearte.\nNota: Para poder desbloquearte no borres el historial del chat.")
                conv.cancel()
                await client(functions.contacts.BlockRequest(id = sender_id))
                #await client.delete_dialog(chat_id, revoke = False)
        except Exception as error:
            #await client.delete_dialog(chat_id, revoke = False)
            await client.send_message(chat_id, "Demasiado tiempo en responder, estas bloqueado(a) 👻.\nSi tienes algun grupo en común conmigo, hablame por ahi, para poder desbloquearte.\nNota: Para poder desbloquearte no borres el historial del chat.")
            await client(functions.contacts.BlockRequest(id = sender_id))