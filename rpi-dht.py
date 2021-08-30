# -*- coding: utf-8 -*-

"""
rpi-dth.py

The script gets temperature and humidity from a DTH11 o DTH22 sersor.

Then these parameters can be viewed in the Terminal.

Usage:
1- Clone the repository. 

2- Update config.auth with your token and user Telegram ID.

3- Install libraries from requisites.txt

4- Run rpi-dth.py in your RPi.
"""

# Importo las librerias
import time, Adafruit_DHT, requests

# Importo la configuración del fichero
from config.auth import *

# Envía un mensaje a través de Telegram
def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + userTelegramID + '&parse_mode=Markdown&text=' + bot_message
    requests.post(send_text)

def main():  
    # Obtengo
    sensor = Adafruit_DHT.DHT11                                     # Cambiar 11 por 22 al usar un sensor DHT22
    pin = 4                                                         # Asignar el valor del pin que se use
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Se muestra en el Terminal los valores leidos
    if humidity is not None and temperature is not None:
        print('Temperatura = {0:0.1f} ºC  Humedad = {1:0.1f} %'.format(temperature, humidity))
    else:
        print('Fallo en la medida')
    # Se enviará la información mediante un mensaje a través un bot
    # telegram_bot_sendtext('La temperatura es %f ºC y la humedad es %f %', temperature, humidity)

if __name__ == "__main__":
	main()
