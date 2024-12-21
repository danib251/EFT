import requests
from datetime import datetime, timedelta

# Configuración
API_KEY = "tu_clave_api"  # Reemplaza con tu clave API
BASE_URL = "https://newsapi.org/v2/everything"

# Función para obtener noticias
def obtener_noticias_economia():
    # Fechas
    hoy = datetime.now()
    ayer = hoy - timedelta(days=1)

    # Dominios especializados en economía, bolsa y ETFs
    dominios = ",".join([
        "bloomberg.com", "ft.com", "reuters.com", "cnbc.com", "morningstar.com",
        "expansion.com", "cincodias.elpais.com", "eleconomista.es"
    ])

    # Parámetros refinados
    params = {
        "q": '"S&P 500" OR "bolsa" OR "ETFs" OR "mercados financieros"',  # Búsqueda exacta con términos clave
        "from": ayer.strftime("%Y-%m-%d"),  # Noticias desde ayer
        "to": hoy.strftime("%Y-%m-%d"),  # Hasta hoy
        "language": "es",  # Español (puedes eliminar para resultados globales)
        "domains": dominios,  # Filtrar por dominios seleccionados
        "sortBy": "relevancy",  # Ordenar por relevancia
        "apiKey": API_KEY,
    }

    # Solicitud a la API
    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        print("Error al obtener noticias:", response.status_code, response.json())
        return []

    # Procesar respuesta
    datos = response.json()
    if "articles" not in datos or not datos["articles"]:
        print("No se encontraron noticias. Respuesta completa:", datos)
        return []

    # Filtrar resultados
    noticias_filtradas = [
        {
            "titulo": articulo["title"],
            "descripcion": articulo["description"],
            "url": articulo["url"],
        }
        for articulo in datos["articles"]
    ]

    return noticias_filtradas

# Ejecutar y mostrar resultados
noticias = obtener_noticias_economia()
if noticias:
    print("Noticias relevantes:")
    for i, noticia in enumerate(noticias, 1):
        print(f"{i}. {noticia['titulo']}")
        print(f"   {noticia['descripcion']}")
        print(f"   URL: {noticia['url']}")
else:
    print("No se encontraron noticias relevantes.")
