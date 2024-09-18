import requests
import tkinter as tk
from bs4 import BeautifulSoup
import os

# URL base
url_base = "https://es.finance.yahoo.com/quote/"  # Aquí pones la parte fija de la URL

encabezados={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0'}

html = requests.get(url_base+siglas, headers=encabezados)

sopa = BeautifulSoup(html.content,'lxml')

titulo = sopa.find('h1',class_="D(ib) Fz(18px)").get_text()



siglas= ''

# Función que completa la URL y muestra los resultados
def buscar_compania():
    global siglas,url_completa
    siglas = visor_texto.get()  # Obtener el texto del visor
    if siglas:
        url_completa = url_base + siglas.upper()  # Completar la URL con las siglas en mayúsculas
        resultado.set(f"{titulo} el precio es {precio}")
        # Aquí puedes hacer alguna búsqueda real o simulada con la URL completa
    else:
        resultado.set("Por favor ingresa las siglas de la compañía.")


precio = sopa.find('fin-streamer', {'data-symbol': siglas}).get_text()



# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Búsqueda de Compañías")

# Variable para el texto ingresado en el visor
visor_texto = tk.StringVar()

# Crear un campo de entrada para las siglas de la compañía
visor = tk.Entry(ventana, textvariable=visor_texto, font=('Helvetica', 16), width=20)
visor.pack(pady=10)

# Crear un botón para realizar la búsqueda
boton = tk.Button(ventana, text="Buscar", command=buscar_compania, font=('Helvetica', 14))
boton.pack(pady=10)

# Variable para mostrar los resultados
resultado = tk.StringVar()

# Crear una etiqueta para mostrar los resultados
label_resultado = tk.Label(ventana, textvariable=resultado, font=('Helvetica', 14), fg="blue")
label_resultado.pack(pady=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()
