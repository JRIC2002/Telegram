#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author: José Rodolfo (JRIC2002)

#Modules
#import asyncio
#from bs4 import BeautifulSoup
import json
from modules.colors import color
from modules.commands import help, serverinfo, getinfo, youtube, wikipedia, google, translate, weather, alternative, myfavoriteos, block, unblock, security, setprefix, setlanguage
#import os
#import platform
#import re
#import requests
import sys
import telethon
#from telethon.tl.functions.users import GetFullUserRequest
#from telethon.tl.functions.messages import GetFullChatRequest
#from telethon.tl.functions.channels import GetFullChannelRequest
#from telethon.tl import functions
import time
#from urllib import parse, request
#import datetime

config_file = open("modules/config.json", "r")
config = config_file.read()
config = json.loads(config)
api_id = config["api_id"]
api_hash = config["api_hash"]
#prefix = config["prefix"]
#language = config["language"]
#security = config["security"]
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
    def __init__(self, username, api_id, api_hash):
        self.username = username
        self.api_id = api_id
        self.api_hash = api_hash
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
            prefix = "."
            language = "es"
            security_status = False
            try:
                with open("modules/config.json", "r") as config_file:
                    config = config_file.read()
                    config = json.loads(config)
                    prefix = config["prefix"]
                    language = config["language"]
                    security_status = bool(config["security"])
            except Exception as error:
                await client.send_message(chat_id, "Ha ocurrido un problema.")
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
            if command == prefix + "help" and len(arg) == 0 and sender_id == my_id:
                await deleteMsg()
                await help.help(client, chat_id, prefix)
            if command == prefix + "serverinfo" and len(arg) == 0 and sender_id == my_id:
                await deleteMsg()
                await serverinfo.serverinfo(client, chat_id, telegram, self.username)
            if command == prefix + "getinfo" and len(arg) == 2 and sender_id == my_id:
                await deleteMsg()
                if arg[0] == "-u" or str(arg[0]) == "--user":
                    await getinfo.userinfo(client, chat_id, arg[1])
                if arg[0] == "-t":
                    await getinfo.gcinfo(client, chat_id, arg[1])
            if (command == prefix + "youtube" or command == prefix + "yt") and len(arg) >= 1 and sender_id == my_id:
                await deleteMsg()
                await youtube.youtube(client, chat_id, arg)
            if (command == prefix + "wikipedia" or command == prefix + "wiki") and len(arg) >= 1 and sender_id == my_id:
                await deleteMsg()
                await wikipedia.wikipedia(client, chat_id, language, arg)
            if command == prefix + "google" and len(arg) >= 1 and sender_id == my_id:
                await deleteMsg()
                await google.google(client, chat_id, arg)
            if command == prefix + "translate" and len(arg) >= 2 and sender_id == my_id:
                await deleteMsg()
                await translate.translate(client, chat_id, arg[0], arg[1:])
            if command == prefix + "weather" and len(arg) >= 1 and sender_id == my_id:
                await deleteMsg()
                await weather.weather(client, chat_id, language, arg)
            if command == prefix + "alternative" and len(arg) >= 1 and sender_id == my_id:
                await deleteMsg()
                await alternative.alternative(client, chat_id, arg)
            if (command == prefix + "myfavoriteos" or command == prefix  + "mfos") and len(arg) >= 1 and sender_id == my_id:
                await deleteMsg()
                if (arg[0] == "-s" or arg[0] == "--show") and len(arg) == 1:
                    await myfavoriteos.show(client, chat_id)
                if (arg[0] == "-a" or arg[0] == "--add") and len(arg) >= 2:
                    await myfavoriteos.add(client, chat_id, arg[1:])
                if (arg[0] == "-d" or arg[0] == "--delete") and len(arg) >= 2:
                    await myfavoriteos.delete(client, chat_id, arg[1:])
            if command == prefix + "block" and len(arg) == 1 and sender_id == my_id:
                await deleteMsg()
                await block.block(client, chat_id, arg[0])
            if command == prefix + "unblock" and len(arg) == 1 and sender_id == my_id:
                await deleteMsg()
                await unblock.unblock(client, chat_id, arg[0])
            if command == prefix + "security" and len(arg) == 1 and sender_id == my_id:
                await deleteMsg()
                try:
                    if arg[0] == "-a" or arg[0] == "--activate":
                        await security.activate(client, chat_id, security_status)
                    if arg[0] == "-d" or arg[0] == "--desactivate":
                        await security.desactivate(client, chat_id, security_status)
                except Exception as error:
                    await client.send_message(chat_id, "Ha ocurrido un problema.")
            if command == prefix + "setprefix" and len(arg) == 1 and sender_id == my_id:
                await deleteMsg()
                await setprefix.setprefix(client, chat_id, arg[0])
            if command == prefix + "setlanguage" and len(arg) == 1 and sender_id == my_id:
                await deleteMsg()
                await setlanguage.setlanguage(client, chat_id, arg[0])
            if sender_id == chat_id and event.is_private and sender_id != my_id and security_status:
                await security.security(client, chat_id, sender_id)
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
        user = User(str(sys.argv[2]), api_id, api_hash)
        user.msg()
        user.start()
        user.finish()
    else:
        telegram.help()
else:
    telegram.help()