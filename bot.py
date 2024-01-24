import pywhatkit
from datetime import datetime
import time

numero_tel = "+34xxxxxxxxx"
mensaje = "Como estás?"

# Obtener la hora actual + 60 segundos
seconds = time.time() + 60
date = datetime.fromtimestamp(seconds)

# Enviar mensaje con pywhatkit
pywhatkit.sendwhatmsg(numero_tel, mensaje, date.hour, date.minute)
	
