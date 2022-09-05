"""
Proyecto de prueba sobre WebScrapping con BeautifulSoup y Pandas.
Obtención de datos de precios de combustible de la web de Petropar.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Obtenemos la respuesta de la página a ser scrappeada
response = requests.get('https://www.petropar.gov.py/?page_id=4460')

# Creamos el objeto BeautifulSoup para parsear el HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Obtenemos el elemento que contiene la tabla
tbody = soup.find('tbody')
# Obtenemos los elementos que contienen las filas de la tabla
all_tr = tbody.find_all('tr')

data = []
# Iteramos sobre las filas de la tabla
# Omitimos los primeros 3 elementos de la lista por que son cabeceras
for elem in all_tr[3:]:
    row = []
    # Por cada tr, iteramos sobre los td, para evitar el salto de linea entre los td 
    for td in elem.find_all('td'):
        # agregamos el texto de cada td a la fila(row)
        row.append(td.text)
    # Agregamos la fila a la lista data
    data.append(row)

# Creamos el DataFrame
df = pd.DataFrame(data)
print(df)