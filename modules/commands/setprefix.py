#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import json

async def setprefix(client, chat_id, new_prefix):
    try:
        config = ""
        with open("modules/config.json", "r") as config_file:
            config = config_file.read()
            config = json.loads(config)
        with open("modules/config.json", "w") as config_file:
            config_file.seek(0)
            config["prefix"] = new_prefix
            config_file.write(json.dumps(config))
        await client.send_message(chat_id, "El nuevo prefijo de los comandos es `{}`".format(new_prefix))
    except Exception as error:
        print(error)
        await client.send_message(chat_id, "No se pudo cambiar el prefijo de los comandos.")