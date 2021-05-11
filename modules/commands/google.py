#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
from bs4 import BeautifulSoup
import requests

async def google(client, chat_id, string):
    try:
        url = "https://www.google.com/search?"
        query_string = {
            "q": "+".join(string)
        }
        headers = {"Charset":"UTF-8","User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        html_content = requests.get(url, params = query_string, headers = headers)
        soup = BeautifulSoup(html_content.content, "html.parser")
        #print(soup.prettify())
        tag_h3 = soup.find_all("h3")
        titles = []
        for h3 in tag_h3:
            if "<h3 class=\"LC20lb DKV0Md" in str(h3):
                titles.append(str(h3.string))
        tag_span = soup.find_all("span")
        descriptions = []
        for span in tag_span:
            if "<span class=\"aCOpRe\"" in str(span):
                temp_string = ""
                for des in span.find_all("span"):
                    temp_string += str(des.text)
                descriptions.append(temp_string)
        tag_div = soup.find_all("div")
        temp = []
        for div in tag_div:
            if "<div class=\"yuRUbf\"" in str(div):
                if "<a data-ved=\"2ah" in str(div.a):
                    temp.append(str(div.a.get("href")))
        temp = list(dict.fromkeys(temp))
        links = []
        for url in temp:
            links.append(str(url))
        reply = ""
        num_of_results = 5
        for i in range(num_of_results):
            reply = reply + "[{}]({})\n{}".format(titles[i], links[i], descriptions[i])
            if i != (num_of_results - 1):
                reply += "\n\n"
            else:
                reply += "\n"
        await client.send_message(chat_id, "Google - Resultados de **{}**\n\n{}".format(" ".join(string), reply))
    except Exception as error:
        await client.send_message(chat_id, "Ha ocurrido un problema.")