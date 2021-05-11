#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
#import asyncio

async def help(client, chat_id, prefix):
    try:
        field_1 = "**Comandos generales**"
        field_2 = "📓 Los siguientes comandos solo los puede usar el usuario:"
        field_3 = "* `{}help` : Mostrar el menú de ayuda.".format(prefix)
        field_4 = "* `{}serverinfo` : Mostrar información del servidor.".format(prefix)
        field_5 = "* `{}getinfo` : Conseguir información de un usuario, grupo o canal.".format(prefix)
        field_6 = "* `{}youtube` o `{}yt` : Busca un video en YouTube y mostrar el primer resultado.".format(prefix, prefix)
        field_7 = "* `{}wikipedia` o `{}wiki` : Buscar información en wikipedia.".format(prefix, prefix)
        field_8 = "* `{}google` : Buscar en Google.".format(prefix)
        field_9 = "* `{}translate` : Traducir texto a otro idioma.".format(prefix)
        field_10 = "* `{}weather` : Conseguir datos del clima de una ciudad.".format(prefix)
        field_11 = "* `{}alternative` : Buscar alternativas a ciertos programas en https://alternativeto.net/".format(prefix)
        field_12 = "* `{}myfavoriteos` o `{}mfos` : Ver, agregar y eliminar mis sistemas operativos favoritos.".format(prefix, prefix)
        field_13 = "* `{}block` : Bloquear a un usuario.".format(prefix)
        field_14 = "* `{}unblock` : Desbloquear a un usuario.".format(prefix)
        field_15 = "* `{}security` : Activar o desactivar medidas de seguridad.".format(prefix)
        field_16 = "* `{}setprefix` : Establece un nuevo prefijo para los comandos.".format(prefix)
        field_17 = "* `{}setlanguage` : Establecer un nuevo idioma.".format(prefix)
        #last_field = "Escribe `{}help <comando>` para ver más detalles acerca del comando.".format(prefix)
        part_1 = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(field_1, field_2, field_3, field_4, field_5, field_6, field_7, field_8, field_9, field_10)
        part_2 = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(field_11, field_12, field_13, field_14, field_15, field_16, field_17)
        await client.send_message(chat_id, "{}\n{}".format(part_1, part_2), link_preview = False)
    except Exception as error:
        await client.send_message(chat_id, "Ha ocurrido un problema.")