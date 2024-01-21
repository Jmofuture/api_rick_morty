# Rick and Morty Data Integration

Este proyecto consulta la API de Rick y Morty, realiza transformaciones de datos y los carga en Supabase para su almacenamiento y análisis.

## Descripción

Este repositorio contiene un conjunto de scripts en Python diseñados para interactuar con la [API de Rick y Morty](https://rickandmortyapi.com/documentation/#rest). Los scripts automatizan el proceso de extracción de datos de personajes, ubicaciones y episodios. Luego, realiza las transformaciones de datos necesarias y finalmente carga los datos en una base de datos Supabase.

## Características

- Extracción automática de datos paginados de la API de Rick y Morty.
- Transformación de datos JSON, incluyendo la normalización de estructuras anidadas y la corrección de nombres de claves.
- Carga eficiente de datos en Supabase, listos para ser utilizados en aplicaciones o para análisis de datos.

## Requisitos

- Python 3.6 o superior.
- Instalación de las bibliotecas `requests`, `pandas`, y `supabase-py`.
- Credenciales válidas de Supabase (URL de Supabase y Supabase Key).

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/rick-and-morty-supabase.git
    cd rick-and-morty-supabase
    ```

2. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

3. Configura tus credenciales de Supabase en un archivo `.env` en el directorio raíz del proyecto:

    ```
    SUPABASE_URL='tu_url_de_supabase'
    SUPABASE_KEY='tu_llave_de_api_supabase'
    ```

## Uso

Para ejecutar el script principal y cargar los datos en tu base de datos Supabase:

    ```bash
    python main.py
    ```

## Contribución

Las contribuciones son lo que hacen que la comunidad de código abierto sea un lugar maravilloso para aprender, inspirarse y crear. Cualquier contribución que hagas será **enormemente apreciada**.

1. Haz un Fork del proyecto.
2. Crea tu rama para la nueva característica (`git checkout -b feature/AmazingFeature`).
3. Realiza tus cambios y haz commit (`git commit -m 'Add some AmazingFeature'`).
4. Sube tus cambios a la rama (`git push origin feature/AmazingFeature`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo `LICENSE` para detalles.

## Contacto

[@Jmofuture](https://twitter.com/Jmofuture) - email@example.com

Link del Proyecto: [https://github.com/tu-usuario/rick-and-morty-supabase](https://github.com/tu-usuario/rick-and-morty-supabase)
