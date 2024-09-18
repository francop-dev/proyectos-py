import requests
import tkinter as tk
from bs4 import BeautifulSoup
import os
from tkinter import messagebox



entrada_inicial = 'Simbolo del Stock'

#funcion para borrar el placeholder del entry
def on_entry_click(event):
    if visor.get() == entrada_inicial:
        visor.delete(0,'end')
        visor.config(fg='#000000')

    #funcion para extraer datos
def obtener_info():
    sigla = visor.get()
    url = 'https://es.finance.yahoo.com/quote/' + sigla
    if sigla == entrada_inicial or not sigla:
        messagebox.showwarning('advertencia','Por favor ingresa una sigla de stock correcta')
        return
    
    #detalle pedido
    encabezados={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0'}
    
    try:
    
        html = requests.get(url, headers=encabezados)



        #crear sopa
        sopa = BeautifulSoup(html.content,'lxml')


        #extraer titulo y precio actual
        info_encabezado = sopa.find_all('div',id='quote-header-info')[0]
        titulo = info_encabezado.find("h1").get_text()
        precio = info_encabezado.find('fin-streamer', class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").get_text()
        
        #limpiar el frame anterior
        for widget in frame_interior.winfo_children():
            widget.destroy()
        
        #mostrar encabezado
        encabezado = f'{titulo} - {precio}$'
        encabezado_etiqueta = tk.Label(frame_interior, text=encabezado, font=('Helvetica', 16, 'bold'))
        encabezado_etiqueta.grid(row=0, column=0, columnspan=4, pady=10, sticky='n')
        
        #extraer tablas
        filas = sopa.find('div', id='quote-summary').find_all('tr')  # Encuentra todas las filas
        
        for indice_tr,tr in enumerate(filas):
                titulo = tr.find_all('td')[0].get_text()  # Primer columna
                precio = tr.find_all('td')[1].get_text()   # Segunda columna
                fila = (indice_tr // 2) 
                columna = indice_tr % 2
                agregar_a_filas(titulo,precio,fila,columna)

    except requests.exceptions.RequestException as e:
        messagebox.showerror('Error', f'No se pudo obtener la informacion: {e}')
    
#funcion para agregar los registros a la tabla
def agregar_a_filas(titulo,precio,fila,columna):
    #etiqueta 
    etiqueta_widget = tk.Label(frame_interior,text=titulo +':',font=('helvetica',10),anchor='w',name=f'etiqueta_{fila}_{columna}')
    etiqueta_widget.grid(row=fila, column=columna * 2, sticky='w', padx=10, pady=2)
    
    #valor
    valor_widget = tk.Label(frame_interior,text=precio +':' ,font=('helvetica',10),anchor='w',name=f'etiqueta_{fila}_{columna}')
    valor_widget.grid(row=fila, column=columna *2 + 1, padx=10, pady=2)
    
#ventana
ventana = tk.Tk()
#tamaño ventana
ventana.geometry('900x400')
#ruta actual
current_path = os.path.dirname(os.path.abspath(__file__))


#titulo ventana
ventana.title('InfoFinanzas')
#ruta e icono
icon_path = os.path.join(current_path,'calculo.png')
ventana.iconphoto(False, tk.PhotoImage(file=icon_path))

#visor
visor = tk.Entry(ventana,
                 width = 20,
                 font=('Helvetica', 16,'bold'),
                 fg='grey',
                 bg='#eef0f2',
                 )

visor.insert(0, entrada_inicial)
visor.bind('<FocusIn>',on_entry_click)
visor.pack(pady=20)


#boton para buscar
boton_buscar = 'Obtener informacion'
boton =tk.Button(ventana,
          text=boton_buscar,
          font=('Helvetica',20,'bold'),
          bg='#0d21a1',
          fg='#eef0f2',
          command=obtener_info
          )
boton.pack(pady=20)

#frame (cuadro) para el area de resultados
frame_interior = tk.Frame(ventana)
frame_interior.pack(fill='both',padx=10,pady=10,expand=True)

frame_interior.grid_columnconfigure(0,weight=1)
frame_interior.grid_columnconfigure(1,weight=1)
frame_interior.grid_columnconfigure(2,weight=1)
frame_interior.grid_columnconfigure(3,weight=1)





ventana.mainloop()

