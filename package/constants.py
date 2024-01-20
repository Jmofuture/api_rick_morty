import os
from dotenv import load_dotenv
from datetime import date as d

load_dotenv()
#Listado de canales de los cuales queremos la información, en este caso el ID
CHANNELS = ['Programando con Bel','midulive', 'Goncy', 'MoureDev by Brais Moure', 'hdeleon.net','s4vitar','freeCodeCamp Español','freeCodeCamp.org','Alex The Analyst', 'TodoCode', 'Maxi Programa', 'Guinxu']

#Datos para conectarse a la API
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
KEY = os.getenv('API_KEY') # Se obtiene de una variable de entorno
PART = "snippet,statistics"

NAME_DF = f"info_channels_{d.today()}.csv" #Nombre del archivo CSV

#Configuracion de Supabase

TABLE = 'youtube_channels'

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

SUPABASE_EMAIL = os.getenv("SUPABASE_EMAIL")
SUPABASE_PASSWORD = os.getenv("SUPABASE_PASSWORD")