import requests
import pandas as pd
import json



def request_api_base(url):
    results = []
    page = 1

    while True:
        try:

            paginated_url = f"{url}?page=0{page}"
            response = requests.get(paginated_url)
            response.raise_for_status()  # Asegura que se manejen respuestas HTTP no exitosas

            data = response.json()

            results.extend(data['results']) 

            if 'next' in data['info'] and data['info']['next']: #Busca el campo next para hacer pa paginacion
                print(page)
                page += 1
            else:
                break
        except requests.RequestException as e:
            print(f"Error en la solicitud HTTP: {e}")
            break
        except ValueError:
            print("Error: La respuesta no es un JSON válido")
            break
        except TypeError as e:
            print(f"Error de tipo: {e}")
            break

    return results



def json_to_dataframe(json):
    try:
        df = pd.json_normalize(json)
        return df
    except Exception as e:
        print(e)
    finally:
        df.to_csv("rick.csv", index = False)


def replace_keys(df):
    # Reemplaza puntos en los nombres de las columnas por guiones bajos
    df.columns = df.columns.str.replace('.', '_', regex=False)
    return df
