#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import json
import requests

async def translate(client, chat_id, tl, text):
    try:
        query_string = {
            "sl": "auto",
            "tl": tl,
            "text": "".join(text)
        }
        headers = {"Charset":"UTF-8","User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
        response = requests.post(url, data=query_string, headers=headers)
        if response.status_code == 200:
            response = response.json()
            trans_text = response["sentences"][0]["trans"]
            await client.send_message(chat_id, "Traducido a **{}**:\n{}".format(tl, trans_text))
        else:
            await client.send_message(chat_id, "Ha ocurrido un problema.")
    except Exception as error:
        await client.send_message(chat_id, "Ha ocurrido un problema.")