#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import json
import requests

async def wikipedia(client, chat_id, language, string):
    try:
        session = requests.session()
        url = "https://{}.wikipedia.org/w/api.php".format(language)
        limit = 1
        query_string = {
            "action": "opensearch",
            "namespace": "0",
            "search": " ".join(string),
            "limit": str(limit),
            "format": "json"
        }
        result = session.get(url = url, params = query_string)
        data = result.json()
        reply = ""
        for i in range(limit):
            reply = reply + data[1][i] + ": " + data[3][i] + "\n"
        await client.send_message(chat_id, reply)
    except Exception as error:
        await client.send_message(chat_id, "Ha ocurrido un problema.")