#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import time

async def pseudohack(client, chat_id, message_id):
    try:
        # [12345]
        # [.....] 0%
        # [c....] 20%
        # [-c...] 40%
        # [--c..] 60%
        # [---c.] 80%
        # [----c] 100%
        size = 20
        progress = 0
        dino = ""
        cola = ""
        size_cola = 0
        comida = ""
        cantidad_comida = size
        reply = ""
        additional_msg = ""
        i = 0
        while (i <= size):
            if i == 0:
                comida = "o"
            if i == 1:
                dino = "C"
            if i == 2:
                cola = "="
            if i == size:
                dino = cola
            progress = int(i * (100/size))
            reply = "[" + (cola * (i - 1)) + dino + (comida * cantidad_comida) + "] " + str(progress) + "%"
            cantidad_comida = cantidad_comida - 1
            if progress == 0:
                additional_msg = "Buscando...\n"
            if progress == 25:
                additional_msg = "Obteniendo credenciales...\n"
            if progress == 50:
                additional_msg = "Descargando...\n"
            if progress == 75:
                additional_msg = "Guardando...\n"
            if progress == 100:
                additional_msg = ""
                reply = "**Ya tengo tus nudes...xD**"
            await client.edit_message(chat_id, message_id, additional_msg + reply)
            i += 1
            time.sleep(0.5)
    except Exception as error:
        await client.send_message(chat_id, "Ha ocurrido un problema, intente de nuevo.")
        print(error)
