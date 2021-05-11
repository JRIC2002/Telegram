#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
from bs4 import BeautifulSoup
import requests

async def alternative(client, chat_id, software):
    try:
        base_url = "https://alternativeto.net"
        search_url = "https://alternativeto.net/browse/search?q={}".format("+".join(software))
        headers = {"Charset":"UTF-8","User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        html_content = requests.get(search_url, headers = headers)
        if html_content.status_code == 200:
            html = html_content.content
            soup = BeautifulSoup(html, "html.parser")
            tags_a = soup.find_all("a")
            titles = []
            urls = []
            for a in tags_a:
                if "<a data-link-action" in str(a):
                    titles.append(str(a.string))
                    urls.append(base_url + str(a["href"]))
            tags_p = soup.find_all("p")
            descriptions = []
            values = []
            available_os = []
            for p in tags_p:
                if "<p class=\"text\"" in str(p):
                    descriptions.append(str(p.string))
                if "<p class=\"meta\"" in str(p):
                    if "<span class=\"label label-pricing\"" in str(p.span):
                        values.append(str(p.span.span.string))
                    temp = []
                    for span in p.descendants:
                        if "<span class=\"label label-platform" in str(span):
                            temp.append(str(span.string))
                    available_os.append(temp)
            alternatives = ""
            num_of_results = 10
            for n in range(num_of_results):
                alternatives = alternatives + "{}. [{}]({}) ({})\n{}\n**Disponible en:** {}".format(str(n + 1), titles[n], urls[n], values[n], descriptions[n], ", ".join(available_os[n]))
                if n != (num_of_results - 1):
                    alternatives = alternatives + "\n\n"
                else:
                    alternatives = alternatives + "\n"
            await client.send_message(chat_id, "Alternativa a **{}**:\n\n{}\nMás alternativas en: {}".format(" ".join(software), alternatives, search_url))
        else:
            await client.send_message(chat_id, "No se encontraron resultados.\nPuede intentar buscar en: {}".format(base_url))
    except Exception as error:
        await client.send_message(chat_id, "Ha ocurrido un problema.")