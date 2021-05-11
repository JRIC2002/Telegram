#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import json

async def setlanguage(client, chat_id, new_language):
    try:
        with open("modules/config.json", "r") as config_file:
            config = config_file.read()
            config = json.loads(config)
        with open("modules/config.json", "w") as config_file:
            config_file.seek(0)
            config["language"] = new_language
            config_file.write(json.dumps(config))
        await client.send_message(chat_id, "Se cambió el idioma a `{}`".format(new_language))
    except Exception as error:
        await client.send_message(chat_id, "Ha ocurrido un problema, no se puede cambiar el idioma.")