#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: José Rodolfo (JRIC2002)

#Modules
import json
import os
import re
import requests
import sys
import telethon
from telethon.tl.functions.users import GetFullUserRequest
#from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl import types
import time
from urllib import parse, request
#import datetime

from modules.colors import color

configFile = open("modules/config.json", "r")
config = configFile.read()
config = json.loads(config)
api_id = config["api_id"]
api_hash = config["api_hash"]
configFile.close()
client = telethon.TelegramClient("anon", api_id, api_hash)

class App:
    def __init__(self, app, app_version):
        self.app = app
        self.app_version = app_version
    def help(self):
        print("{}{}".format(color.bold, self.app))
        print("Uso: python index.py [opciones]")
        print("Opciones:")
        print("\t-h, --help\t\t\t\tMuestra el menú de ayuda.")
        print("\t-v, --version\t\t\t\tMuestra la versión.")
        print("\t-u <user>, --user <user>\t\tInicia sesión con <user>.{}".format(color.reset))
    def version(self):
        print("{}Telegram {}{}".format(color.bold, self.app_version, color.reset))
#Instancia de la clase Telegram
telegram = App("Telegram", "v1.0.0")

class User:
    def __init__(self, username, api_id, api_hash, prefix):
        self.username = username
        self.api_id = api_id
        self.api_hash = api_hash
        self.prefix = prefix
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
            sender_username = sender_username.lower()
            #sender_id = sender.id
            chat_id = chat.id
            message_id = event.message.id
            username = self.username
            username = username.lower()
            if sender_username == username:
                #me = await client.get_me()
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
                    first_field = "**Comandos generales**"
                    second_field = "Los siguientes comandos solo los puede usar el usuario:"
                    third_field = "• `{}help`: Muestra el menú de ayuda.".format(self.prefix)
                    fourth_field = "• `{}getinfo`: Consigue información de un usuario, grupo o canal.".format(self.prefix)
                    fifth_field = "• `{}yt` o `{}youtube`: Busca un video en YouTube y lanza el primer resultado.".format(self.prefix, self.prefix)
                    sixth_field = "• `{}wikipedia`: Busca un información en wikipedia.".format(self.prefix)
                    seventh_field = "• `{}setprefix`: Configura un nuevo prefijo para los comandos.".format(self.prefix)
                    last_field = "Escribe `{}help <comando>` para ver más detalles acerca del comando.".format(self.prefix)
                    #sixth_field
                    #seventh_field
                    #eighth_field
                    #ninth_field
                    #tenth_field
                    #eleventh_field
                    #twelfth_field
                    await client.send_message(chat_id, "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(first_field, second_field, third_field, fourth_field, fifth_field, sixth_field, seventh_field, last_field))
                if command == self.prefix + "getinfo" and len(arg) == 2:
                    if arg[0] == "-u" or str(arg[0]) == "--user":
                        try:
                            await deleteMsg()
                            user_data = await client(GetFullUserRequest(arg[1]))
                            user = user_data.user
                            profile_picture = await client.download_profile_photo(user.id)
                            user_profile = {
                                "first_name": "**First name:** {}".format(user.first_name),
                                "last_name": "**Last name:** {}".format(user.last_name),
                                "username": "**Username:** {}".format(user.username),
                                "user_id": "**ID:** {}".format(user.id),
                                "user_bot": "**Bot:** {}".format(user.bot),
                                "biography": "**Biography:** {}".format(user_data.about)
                            }
                            reply = "{}\n{}\n{}\n{}\n{}\n{}".format(user_profile["first_name"], user_profile["last_name"], user_profile["username"], user_profile["user_id"], user_profile["user_bot"], user_profile["biography"])
                            await client.send_message(chat_id, reply, file = profile_picture)
                            os.remove(profile_picture)
                        except Exception as error:
                            await client.send_message(chat_id, "El usuario **{}** no existe.".format(arg[1]))
                    if arg[0] == "-t":
                        if arg[1] == ".":
                            arg[1] = chat_id
                        try:
                            await deleteMsg()
                            chat_data = await client(GetFullChannelRequest(arg[1]))
                            full_chat = chat_data.full_chat
                            chats = chat_data.chats[0]
                            profile_picture = await client.download_profile_photo(full_chat.id)
                            chat_profile = {
                                "group_name": "**Group name:** {}".format(chats.title),
                                "username": "**Username:** {}".format(chats.username),
                                "group_id": "**ID:** {}".format(full_chat.id),
                                "description": "**Description:** {}".format(full_chat.about)
                            }
                            reply = "{}\n{}\n{}\n{}".format(chat_profile["group_name"], chat_profile["username"], chat_profile["group_id"], chat_profile["description"])
                            await client.send_message(chat_id, reply, file = profile_picture, link_preview = False)
                            os.remove(profile_picture)
                        except Exception as error:
                            print(error)
                            await client.send_message(chat_id, "El chat o canal **{}** no existe.".format(arg[1]))
                if command == self.prefix + "translate" and len(arg) >= 1:
                    await deleteMsg()
                    url = "https://translate.google.com/?"
                    query_string = parse.urlencode({
                        "sl": "auto",
                        "tl": "es",
                        "text": "hello world",
                        "op": "translate"
                    })
                    html_content = request.urlopen(url + query_string)
                    result = html_content.read().decode()
                    print(result)
                if (command == self.prefix + "yt" or command == self.prefix + "youtube") and len(arg) >= 1:
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
                        await client.send_message(chat_id, "No se puede obtener el resultado.")
                if command == self.prefix + "wikipedia" and len(arg) >= 1:
                    await deleteMsg()
                    session = requests.session()
                    url = "https://es.wikipedia.org/w/api.php"
                    query_string = {
                        "action": "opensearch",
                        "search": " ".join(arg),
                        "limit": "3",
                        "format": "json"
                    }
                    result = session.get(url = url, params = query_string)
                    data = result.json()
                    reply = data[3][0]
                    await client.send_message(chat_id, reply)
                if command == self.prefix + "setprefix" and len(arg) == 1:
                    await deleteMsg()
                    self.prefix = arg[0]
                    await client.send_message(chat_id, "El nuevo prefijo de los comandos es `{}`".format(self.prefix))
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
        user = User(str(sys.argv[2]), api_id, api_hash, ".")
        user.msg()
        user.start()
        user.finish()
    else:
        telegram.help()
else:
    telegram.help()