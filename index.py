#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: José Rodolfo (JRIC2002)

#Modules
import asyncio
from bs4 import BeautifulSoup
import json
import os
import platform
import re
import requests
import sys
import telethon
from telethon.tl.functions.users import GetFullUserRequest
#from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl import functions, types
import time
from urllib import parse, request
#import datetime

from modules.colors import color

config_file = open("modules/config.json", "r")
config = config_file.read()
config = json.loads(config)
api_id = config["api_id"]
api_hash = config["api_hash"]
config_file.close()
client = telethon.TelegramClient("anon", api_id, api_hash)

class App:
    def __init__(self, app, app_version):
        self.app = app
        self.app_version = app_version
    def help(self):
        print("{}{}{}".format(color.bold, color.white, self.app))
        print("Uso: python index.py [opciones]")
        print("Opciones:")
        print("\t-h, --help\t\t\t\tMuestra el menú de ayuda.")
        print("\t-v, --version\t\t\t\tMuestra la versión.")
        print("\t-u <user>, --user <user>\t\tIniciar sesión como <user>.{}".format(color.reset))
    def version(self):
        print("{}{}{} {}{}".format(color.bold, color.white, self.app, self.app_version, color.reset))
#Instancia de la clase Telegram
telegram = App("Telegram", "v1.1.0")

class User:
    def __init__(self, username, api_id, api_hash, prefix, language, security):
        self.username = username
        self.api_id = api_id
        self.api_hash = api_hash
        self.prefix = prefix
        self.language = language
        self.security = security
    def start(self):
        client.start()
        print("{}{} conectado...{}".format(color.yellow, self.username, color.reset))
    def msg(self):
        @client.on(telethon.events.NewMessage)
        async def message(event):
            sender = await event.get_sender()
            chat = await event.get_chat()
            sender_username = sender.username
            if bool(sender_username) == False:
                sender_username = "None"
            #sender_username = sender_username.lower()
            sender_id = sender.id
            chat_id = chat.id
            message_id = event.message.id
            #username = self.username
            #username = username.lower()
            me = await client.get_me()
            my_id = me.id
            #print(sender.stringify())
            if sender_id == my_id:
                msg = event.raw_text.split(" ")
                command = msg.pop(0)
                arg = msg
                """
                now = datetime.datetime.now()
                year = now.year
                month = now.month
                day = now.day
                hour = now.hour
                min = now.minute
                sec = now.second
                time = now.strftime("[%I:%M:%S %p | %Y-%m-%d]")
                with open("events.log", "a+") as logs:
                    logs.seek(0)
                    cont = 0
                    for linea in logs:
                        cont += 1
                    if cont < 3:
                        logs.write("{} {}: {}\n".format(time, sender_username, event.raw_text))
                    if cont >= 3:
                        logs.truncate(0)
                        logs.write("{} {}: {}\n".format(time, sender_username, event.raw_text))
                """
                async def deleteMsg():
                    time.sleep(1)
                    await client.delete_messages(chat_id, message_id)
                if command == self.prefix + "help" and len(arg) == 0:
                    await deleteMsg()
                    try:
                        field_1 = "**Comandos generales**"
                        field_2 = "📓 Los siguientes comandos solo los puede usar el usuario:"
                        field_3 = "* `{}help` : Mostrar el menú de ayuda.".format(self.prefix)
                        field_4 = "* `{}serverinfo` : Mostrar información del servidor.".format(self.prefix)
                        field_5 = "* `{}getinfo` : Conseguir información de un usuario, grupo o canal.".format(self.prefix)
                        field_6 = "* `{}youtube` o `{}yt` : Busca un video en YouTube y lanza el primer resultado.".format(self.prefix, self.prefix)
                        field_7 = "* `{}wikipedia` o `{}wiki` : Buscar información en wikipedia.".format(self.prefix, self.prefix)
                        field_8 = "* `{}google` : Buscar en Google.".format(self.prefix)
                        field_9 = "* `{}translate` : Traducir texto a otro idioma.".format(self.prefix)
                        field_10 = "* `{}weather` : Conseguir datos del clima de una ciudad.".format(self.prefix)
                        field_11 = "* `{}alternative` : Buscar alternativas a ciertos programas en https://alternativeto.net/".format(self.prefix)
                        field_12 = "* `{}myfavoriteos` o `{}mfos` : Ver, agregar y eliminar mis sistemas operativos favoritos.".format(self.prefix, self.prefix)
                        field_13 = "* `{}block` : Bloquear a un usuario.".format(self.prefix)
                        field_14 = "* `{}unblock` : Desbloquear a un usuario.".format(self.prefix)
                        field_15 = "* `{}security` : Activar o desactivar medidas de seguridad.".format(self.prefix)
                        field_16 = "* `{}setprefix` : Establece un nuevo prefijo para los comandos.".format(self.prefix)
                        field_17 = "* `{}setlanguage` : Establecer un nuevo idioma.".format(self.prefix)
                        #last_field = "Escribe `{}help <comando>` para ver más detalles acerca del comando.".format(self.prefix)
                        part_1 = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(field_1, field_2, field_3, field_4, field_5, field_6, field_7, field_8, field_9, field_10)
                        part_2 = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(field_11, field_12, field_13, field_14, field_15, field_16, field_17)
                        await client.send_message(chat_id, "{}\n{}".format(part_1, part_2), link_preview = False)
                    except Exception as error:
                        await client.send_message(chat_id, "Ha ocurrido un problema.")
                if command == self.prefix + "serverinfo" and len(arg) == 0:
                    await deleteMsg()
                    try:
                        reply = "\n👤 **Usuario:**\t{}\n📱 **Telethon:**\tv1.21.1\n🐍 **Python:**\tv{}\n📡 **{}:**\t{}".format(self.username, platform.python_version(), telegram.app, telegram.app_version)
                        await client.send_message(chat_id, reply)
                    except Exception as error:
                        await client.send_message(chat_id, "Ha ocurrido un problema.")
                if command == self.prefix + "getinfo" and len(arg) == 2:
                    if arg[0] == "-u" or str(arg[0]) == "--user":
                        try:
                            await deleteMsg()
                            user_data = await client(GetFullUserRequest(arg[1]))
                            user = user_data.user
                            profile_picture = await client.download_profile_photo(user.id, file = "modules/temp/")
                            user_profile = {
                                "first_name": "**Nombre:** {}".format(user.first_name),
                                "last_name": "**Apellido:** {}".format(user.last_name),
                                "username": "**Nombre de usuario:** {}".format(user.username),
                                "user_id": "**ID:** {}".format(user.id),
                                "user_bot": "**Bot:** {}".format(user.bot),
                                "biography": "**Biografía:** {}".format(user_data.about)
                            }
                            reply = "{}\n{}\n{}\n{}\n{}\n{}".format(user_profile["first_name"], user_profile["last_name"], user_profile["username"], user_profile["user_id"], user_profile["user_bot"], user_profile["biography"])
                            await client.send_message(chat_id, reply, file = profile_picture)
                            os.remove(profile_picture)
                        except Exception as error:
                            await client.send_message(chat_id, "Ha ocurrido un problema, es posible que el usuario **{}** no existe.".format(arg[1]))
                    if arg[0] == "-t":
                        if arg[1] == ".":
                            arg[1] = chat_id
                        try:
                            await deleteMsg()
                            chat_data = await client(GetFullChannelRequest(arg[1]))
                            full_chat = chat_data.full_chat
                            chats = chat_data.chats[0]
                            profile_picture = await client.download_profile_photo(full_chat.id, file = "modules/temp/")
                            chat_profile = {
                                "group_name": "**Nombre del grupo o canal:** {}".format(chats.title),
                                "username": "**Nombre de usuario:** {}".format(chats.username),
                                "group_id": "**ID:** {}".format(full_chat.id),
                                "description": "**Descripción:** {}".format(full_chat.about)
                            }
                            reply = "{}\n{}\n{}\n{}".format(chat_profile["group_name"], chat_profile["username"], chat_profile["group_id"], chat_profile["description"])
                            await client.send_message(chat_id, reply, file = profile_picture, link_preview = False)
                            os.remove(profile_picture)
                        except Exception as error:
                            print(error)
                            await client.send_message(chat_id, "Ha ocurrido un problema, es posible que el grupo o canal **{}** no existe.".format(arg[1]))
                if (command == self.prefix + "youtube" or command == self.prefix + "yt") and len(arg) >= 1:
                    try:
                        await deleteMsg()
                        url = "https://www.youtube.com/results?"
                        query_string = parse.urlencode({
                            "search_query": " ".join(arg)
                        })
                        html_content = request.urlopen(url + query_string)
                        result = html_content.read().decode()
                        video_id = re.findall("\/watch\?v=(.{11})", result)
                        video = "https://www.youtube.com/watch?v=" + video_id[0]
                        await client.send_message(chat_id, video)
                    except Exception as error:
                        await client.send_message(chat_id, "Ocurrió un problema.")
                if (command == self.prefix + "wikipedia" or command == self.prefix + "wiki") and len(arg) >= 1:
                    await deleteMsg()
                    session = requests.session()
                    url = "https://{}.wikipedia.org/w/api.php".format(self.language)
                    limit = 1
                    query_string = {
                        "action": "opensearch",
                        "namespace": "0",
                        "search": " ".join(arg),
                        "limit": str(limit),
                        "format": "json"
                    }
                    result = session.get(url = url, params = query_string)
                    data = result.json()
                    reply = ""
                    for i in range(limit):
                        reply = reply + data[1][i] + ": " + data[3][i] + "\n"
                    await client.send_message(chat_id, reply)
                if command == self.prefix + "google" and len(arg) >= 1:
                    await deleteMsg()
                    try:
                        url = "https://www.google.com/search?"
                        query_string = {
                            "q": "+".join(arg)
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
                        await client.send_message(chat_id, "Google - Resultados de **{}**\n\n{}".format(" ".join(arg), reply))
                    except Exception as error:
                        print(error)
                        await client.send_message(chat_id, "Ha ocurrido un problema.")
                if command == self.prefix + "translate" and len(arg) >= 2:
                    await deleteMsg()
                    try:
                        query_string = {
                            "sl": "auto",
                            "tl": arg[0],
                            "text": "".join(arg[1:])
                        }
                        headers = {"Charset":"UTF-8","User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
                        url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
                        response = requests.post(url, data=query_string, headers=headers)
                        if response.status_code == 200:
                            response = response.json()
                            text = response["sentences"][0]["trans"]
                            await client.send_message(chat_id, "Traducido a **{}**:\n{}".format(arg[0], text))
                        else:
                            await client.send_message(chat_id, "Ocurrió un problema.")
                    except Exception as error:
                        await client.send_message(chat_id, "Ocurrió un problema.")
                if command == self.prefix + "weather" and len(arg) >= 1:
                    await deleteMsg()
                    try:
                        #Project code https://github.com/chubin/wttr.in
                        #Download image
                        image = requests.get("http://wttr.in/{}.png?lang={}".format("+".join(arg), self.language)).content
                        image_temp = open("modules/temp/image_temp.png", "wb")
                        image_temp.write(image)
                        image_temp.close()
                        os.remove("modules/temp/image_temp.png")
                        #Weather data
                        url = "http://wttr.in/{}?lang={}&format=j1".format("+".join(arg), self.language)
                        response = requests.get(url)
                        response = response.json()
                        condition = response["current_condition"][0]["weatherDesc"][0]["value"]
                        if self.language != "en":
                            condition = response["current_condition"][0]["lang_{}".format(self.language)][0]["value"]
                        weather = {
                            "city": "**🏙 Ciudad:** {}".format(response["nearest_area"][0]["areaName"][0]["value"]),
                            "region": "**🏞 Región:** {}".format(response["nearest_area"][0]["region"][0]["value"]),
                            "country": "**🌇 País:** {}".format(response["nearest_area"][0]["country"][0]["value"]),
                            "latitude": "**🌎 Latitud:** {}".format(response["nearest_area"][0]["latitude"]),
                            "longitude": "**🌎 Longitud:** {}".format(response["nearest_area"][0]["longitude"]),
                            "condition": "**🌄 Estado:** {}".format(condition),
                            "temp_c": "**🌡 Temperatura:** {}°C".format(response["current_condition"][0]["temp_C"]),
                            "precip": "**🌦 Precipitación:** {}mm".format(response["current_condition"][0]["precipMM"]),
                            "humidity": "**🌫 Humedad:** {}%".format(response["current_condition"][0]["humidity"]),
                            "wind_speed": "**🌪 Velocidad del viento:** {}km/h".format(response["current_condition"][0]["windspeedKmph"])
                        }
                        reply = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(weather["city"], weather["region"], weather["country"], weather["latitude"], weather["longitude"], weather["condition"], weather["temp_c"], weather["precip"], weather["humidity"], weather["wind_speed"])
                        await client.send_message(chat_id, reply, file = image)
                    except Exception as error:
                        await client.send_message(chat_id, "Ocurrió un problema.")
                if command == self.prefix + "alternative" and len(arg) >= 1:
                    await deleteMsg()
                    try:
                        base_url = "https://alternativeto.net"
                        search_url = "https://alternativeto.net/browse/search?q={}".format("+".join(arg))
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
                            await client.send_message(chat_id, "Alternativa a **{}**:\n\n{}\nMás alternativas en: {}".format(" ".join(arg), alternatives, search_url))
                        else:
                            await client.send_message(chat_id, "No se encontraron resultados.\nPuede intentar buscar en: {}".format(base_url))
                    except Exception as error:
                        await client.send_message(chat_id, "Ha ocurrido un problema.")
                if (command == self.prefix + "myfavoriteos" or command == self.prefix  + "mfos") and len(arg) >= 1:
                    await deleteMsg()
                    if (arg[0] == "-s" or arg[0] == "--show") and len(arg) == 1:
                        try:
                            reply = ""
                            with open("modules/data.json", "r") as data_file:
                                data = data_file.read()
                                data = json.loads(data)
                                my_favorite_os = data["my_favorite_os"]
                                if len(my_favorite_os) != 0:
                                    n = 0
                                    while n < len(my_favorite_os):
                                        if n == len(my_favorite_os) - 1:
                                            reply = reply + "└─ {}".format(my_favorite_os[n])
                                        else:
                                            reply = reply + "├─ {}\n".format(my_favorite_os[n])
                                        n += 1
                                    await client.send_message(chat_id, "Mis OS favoritos\n{}".format(reply))
                                else:
                                    await client.send_message(chat_id, "No tienes OS favoritas en la lista.")
                        except Exception as error:
                            await client.send_message(chat_id, "Ha ocurrido un problema.")
                    if (arg[0] == "-a" or arg[0] == "--add") and len(arg) >= 2:
                        try:
                            with open("modules/data.json", "r+") as data_file:
                                #config_file.seek(0)
                                data = data_file.read()
                                data = json.loads(data)
                                my_favorite_os = data["my_favorite_os"]
                                add_os = True
                                os_name = " ".join(arg[1:])
                                for fav_os in my_favorite_os:
                                    if fav_os == os_name:
                                        add_os = False
                                        await client.send_message(chat_id, "**{}** ya esta en la lista.".format(os_name))
                                        break
                                if add_os:
                                    data["my_favorite_os"].append(os_name)
                                    data_file.seek(0)
                                    data_file.write(json.dumps(data))
                                    await client.send_message(chat_id, "**{}** ha sido agregado a la lista.".format(os_name))
                        except Exception as error:
                            await client.send_message(chat_id, "Ha ocurrido un problema.")
                    if (arg[0] == "-d" or arg[0] == "--delete") and len(arg) >= 2:
                        try:
                            data = ""
                            my_favorite_os = ""
                            os_name = ""
                            error_msg = True
                            with open("modules/data.json", "r") as data_file:
                                data = data_file.read()
                                data = json.loads(data)
                                my_favorite_os = data["my_favorite_os"]
                                os_name = " ".join(arg[1:])
                            with open("modules/data.json", "w") as data_file:
                                for fav_os in my_favorite_os:
                                    if fav_os == os_name:
                                        index = my_favorite_os.index(os_name)
                                        data["my_favorite_os"].pop(index)
                                        data_file.seek(0)
                                        #data_file.truncate()
                                        data_file.write(json.dumps(data))
                                        error_msg = False
                                        await client.send_message(chat_id, "**{}** ha sido eliminado de la lista.".format(os_name))
                                        break
                                if error_msg:
                                    await client.send_message(chat_id, "No se puede eliminar algo que no existe.")
                        except Exception as error:
                            await client.send_message(chat_id, "Ha ocurrido un problema.")
                if command == self.prefix + "block" and len(arg) == 1:
                    await deleteMsg()
                    try:
                        await client(functions.contacts.BlockRequest(id = arg[0]))
                        await client.send_message(chat_id, "Se ha bloqueado al usuario **{}**.".format(arg[0]))
                    except Exception as error:
                        await client.send_message(chat_id, "Ocurrió un problema, no se puede bloquear al usuario **{}**.".format(arg[0]))
                if command == self.prefix + "unblock" and len(arg) == 1:
                    await deleteMsg()
                    try:
                        await client(functions.contacts.UnblockRequest(id = arg[0]))
                        await client.send_message(chat_id, "Se ha desbloqueado al usuario **{}**.".format(arg[0]))
                    except Exception as error:
                        await client.send_message(chat_id, "Ocurrió un problema, no se puede desbloquear al usuario **{}**.".format(arg[0]))
                if command == self.prefix + "security" and len(arg) == 1:
                    await deleteMsg()
                    try:
                        if arg[0] == "-a" or arg[0] == "--activate":
                            self.security = True
                            await client.send_message(chat_id, "Se activo el modo **seguro**.")
                        if arg[0] == "-d" or arg[0] == "--desactivate":
                            self.security = False
                            await client.send_message(chat_id, "Se desactivo el modo **seguro**.")
                    except Exception as error:
                        await client.send_message(chat_id, "Ha ocurrido un problema.")
                if command == self.prefix + "setprefix" and len(arg) == 1:
                    await deleteMsg()
                    try:
                        self.prefix = arg[0]
                        await client.send_message(chat_id, "El nuevo prefijo de los comandos es `{}`".format(self.prefix))
                    except Exception as error:
                        await client.send_message(chat_id, "No se pudó cambiar el prefijo de los comandos.")
                if command == self.prefix + "setlanguage" and len(arg) == 1:
                    await deleteMsg()
                    try:
                        self.language = arg[0]
                        await client.send_message(chat_id, "Se cambió el idioma a `{}`".format(self.language))
                    except Exception as error:
                        await client.send_message(chat_id, "Ocurrió un problema, no se puede cambiar el idioma.")
            if sender_id == chat_id and event.is_private and sender_id != my_id and self.security:
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
    def finish(self):
        client.run_until_disconnected()
        print("{}Desconectado...{}".format(color.yellow, color.reset))

#Start
if len(sys.argv) == 1:
    telegram.help()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        telegram.help()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        telegram.version()
    else:
       telegram.help()
elif len(sys.argv) == 3:
    if sys.argv[1] == "-u" or sys.argv[1] == "--user":
        user = User(str(sys.argv[2]), api_id, api_hash, ".", "es", True)
        user.msg()
        user.start()
        user.finish()
    else:
        telegram.help()
else:
    telegram.help()