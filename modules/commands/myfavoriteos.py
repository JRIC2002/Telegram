#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import json

async def show(client, chat_id):
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

async def add(client, chat_id, opsys):
    try:
        with open("modules/data.json", "r+") as data_file:
            #config_file.seek(0)
            data = data_file.read()
            data = json.loads(data)
            my_favorite_os = data["my_favorite_os"]
            add_os = True
            os_name = " ".join(opsys)
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

async def delete(client, chat_id, opsys):
    try:
        data = ""
        my_favorite_os = ""
        os_name = ""
        error_msg = True
        with open("modules/data.json", "r") as data_file:
            data = data_file.read()
            data = json.loads(data)
            my_favorite_os = data["my_favorite_os"]
            os_name = " ".join(opsys)
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