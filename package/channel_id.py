import os
import requests as r
import pandas as pd
from googleapiclient.discovery import build
import googleapiclient.errors 


#Obtengo los ids de los canaloes

def get_channel_id(channel_name, api_key):
    try:
        url = f'https://www.googleapis.com/youtube/v3/search?part=id&type=channel&q={channel_name}&key={api_key}'
        response = r.get(url)
        data = response.json()

        if 'items' in data and len(data['items']) > 0:
            print(data)
            return data['items'][0]['id']['channelId']
    except Exception as e:
        print(e)

#con los ids generamos el listado pra luego pasarlo como parametro dentro de la llamda a la api
def get_channel_ids_list(channels, api_key):
    try:
        channel_ids = []
        for channel in channels:
            channel_id = get_channel_id(channel, api_key)
            channel_ids.append(channel_id)
            print(f'ID del Canal "{channel}": {channel_id}')
        return channel_ids
    except Exception as e:
        print(e)


def auth(name, version, key, part, id):
    try:
        youtube = build(name, version, developerKey=key)
        request = youtube.channels().list(part=part,id=','.join(id))
        response = request.execute()
        return response
    except Exception as e:
        print(e)
        



def data(res):
    all_data = []
    for item in res['items']:
        data = {
        'channel_id': item['id'],
        'creation_date': item['snippet']['publishedAt'],
        'channel_name': item['snippet']['title'],
        'description': item['snippet']['description'],
        'country': item['snippet']['country'],
        'subscribers': item['statistics']['subscriberCount'],
        'videos': item['statistics']['videoCount'],
        'views': item['statistics']['viewCount']
    }
    all_data.append(data)
    return all_data

# Crear un DataFrame con los datos

