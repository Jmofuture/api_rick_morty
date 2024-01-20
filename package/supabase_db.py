import supabase as s


def create_client(url, key):
    try:
        client = s.create_client(url, key)
        print(f"Cliente exitoso {client}")
        return client
    except Exception as e:
        print(e)



def insert_data(url, key, df, table_name):
    client = create_client(url, key)
    if client is None:
        print("No se pudo crear el cliente de Supabase.")
        return

    data_to_insert = df.to_dict(orient='records')

    try:
        response = client.table(table_name).insert(data_to_insert).execute()
        if response.error:
            print(f"Error al insertar datos: {response.error}")
        else:
            print(f"Datos insertados exitosamente. {len(data_to_insert)} filas añadidas.")
    except Exception as e:
        print(f"Excepción al insertar datos: {e}")





