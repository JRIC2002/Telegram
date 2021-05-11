#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Modules
import json
import os
import requests

async def weather(client, chat_id, language, city):
    try:
        #Project code https://github.com/chubin/wttr.in
        #Download image
        image = requests.get("http://wttr.in/{}.png?lang={}".format("+".join(city), language)).content
        image_temp = open("modules/temp/image_temp.png", "wb")
        image_temp.write(image)
        image_temp.close()
        os.remove("modules/temp/image_temp.png")
        #Weather data
        url = "http://wttr.in/{}?lang={}&format=j1".format("+".join(city), language)
        response = requests.get(url)
        response = response.json()
        condition = response["current_condition"][0]["weatherDesc"][0]["value"]
        if language != "en":
            condition = response["current_condition"][0]["lang_{}".format(language)][0]["value"]
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
        await client.send_message(chat_id, "Ha ocurrido un problema.")