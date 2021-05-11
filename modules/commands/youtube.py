#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
from urllib import parse, request
import re

async def youtube(client, chat_id, string):
    try:
        url = "https://www.youtube.com/results?"
        query_string = parse.urlencode({
            "search_query": " ".join(string)
        })
        html_content = request.urlopen(url + query_string)
        result = html_content.read().decode()
        video_id = re.findall("\/watch\?v=(.{11})", result)
        video = "https://www.youtube.com/watch?v=" + video_id[0]
        await client.send_message(chat_id, video)
    except Exception as error:
        await client.send_message(chat_id, "Ocurrió un problema.")