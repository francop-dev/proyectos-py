import requests
import tkinter as tk
from bs4 import BeautifulSoup


#detalle del pedido
url = 'https://es.finance.yahoo.com/quote/NVDA/'
encabezados={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0'}
html = requests.get(url, headers=encabezados)

#crear sopa
sopa = BeautifulSoup(html.content,'lxml')


#extraer titulo y precio actual
titulo_nvidia = sopa.find('h1', string='NVIDIA Corporation (NVDA)').get_text()
precio_nvidia = sopa.find('fin-streamer', {'data-symbol': 'NVDA'}).get_text()

#extraer tablas
tabla1_nvidia = sopa.find('div',{'data-test':'left-summary-table'})
tabla2_nvidia = sopa.find('div',{'data-test':'right-summary-table'})

for tabla in (tabla1_nvidia, tabla2_nvidia):
    filas = tabla.find_all('tr')  # Encuentra todas las filas
    for fila in filas:  # Itera sobre cada fila
        nombre = fila.find_all('td')[0].get_text()  # Primer columna
        valor = fila.find_all('td')[1].get_text()   # Segunda columna
        print(nombre + ' - ' + valor)

#print(titulo_nvidia)
#print(precio_nvidia)



