import requests
import tkinter as tk
from bs4 import BeautifulSoup
import os
from tkinter import messagebox
import tkinter.ttk as ttk




entrada_inicial = 'Simbolo del Stock'

modo_noche = False

colores_modo_dia={'ventana_bg':'#E3F2FD',
                  'frame_bg':'#F9FAFB',
                  'boton_bg':'#007BFF',
                  'boton_fg':'white',
                  'texto_etiquetas_fg':'#333333',
                  'etiqueta_bg':'#DDEAF6',
                  'valor_bg':'#FFFFFF',
                  'valor_fg':'#333333'}

colores_modo_noche={'ventana_bg':'#1C1C1E',
                  'frame_bg':'#2C2C2E',
                  'boton_bg':'#0A84FF',
                  'boton_fg':'white',
                  'texto_etiquetas_fg':'#F5F5F5',
                  'etiqueta_bg':'#4D4D4D',
                  'valor_bg':'#000000',
                  'valor_fg':'#FFFFFF'}

#ALTERNAR DIA/NOCHE
def aplicar_paleta(paleta):
    ventana.config(bg=paleta['ventana_bg'])
    frame_interior.config(bg=paleta['frame_bg'])
    boton.config(bg=paleta['boton_bg'], fg=paleta['boton_fg'])
    visor.config(bg=paleta['valor_bg'], fg=paleta['valor_fg'])

    # Actualizar los widgets dentro del frame
    for widget in frame_interior.winfo_children():
        if isinstance(widget, tk.Label):
            if 'valor' in widget.winfo_name():
                widget.config(bg=paleta['valor_bg'], fg=paleta['valor_fg'])
            else:
                widget.config(bg=paleta['etiqueta_bg'], fg=paleta['texto_etiquetas_fg'])


#funcion para borrar el placeholder del entry
def on_entry_click(event):
    color_incio = colores_modo_dia['boton_fg'] if not modo_noche else colores_modo_noche['boton_fg']
    if visor.get() == entrada_inicial:
        visor.delete(0,'end')
        visor.config(fg=color_incio)

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
        encabezado_etiqueta = tk.Label(frame_interior, text=encabezado, font=('Helvetica', 16,'bold' ),relief="raised",borderwidth=3)
        encabezado_etiqueta.grid(row=0, column=0, columnspan=4, pady=5, sticky='n')
        
        #extraer tablas
        filas = sopa.find('div', id='quote-summary').find_all('tr')  # Encuentra todas las filas
        
        for indice_tr,tr in enumerate(filas):
                titulo = tr.find_all('td')[0].get_text()  # Primer columna
                precio = tr.find_all('td')[1].get_text()   # Segunda columna
                fila = (indice_tr // 2)
                columna = (indice_tr % 2) 
                agregar_a_filas(titulo,precio,fila,columna)

    except requests.exceptions.RequestException as e:
        messagebox.showerror('Error', f'No se pudo obtener la informacion: {e}')
    
#funcion para agregar los registros a la tabla
def agregar_a_filas(titulo, precio, fila, columna):
    global etiqueta_widget,valor_widget
    # Colocar las primeras 8 filas en la primera tabla y las siguientes 8 en la segunda
    if fila >= 8:  # Si supera la fila 8, comenzamos la segunda tabla
        fila -= 8
        columna += 2  # Desplazamos a la derecha para la segunda tabla
    
    
    color_incio = colores_modo_dia['frame_bg'] if not modo_noche else colores_modo_noche['frame_bg']
    # Crear la etiqueta con el nombre
    etiqueta_widget = tk.Label(frame_interior, text=titulo + ':', font=('Helvetica', 10,'bold'), anchor='w',relief="ridge",borderwidth=1, bg=color_incio)
    etiqueta_widget.grid(row=fila+1, column=columna * 2, sticky='w', padx=10, pady=1)
    
    # Crear la etiqueta con el valor
    valor_widget = tk.Label(frame_interior, text=precio,fg='black', font=('Helvetica', 10,'bold'), anchor='w',relief="ridge",borderwidth=1, bg=color_incio)
    valor_widget.grid(row=fila+1, column=columna * 2 + 1,sticky='w', padx=10, pady=1)
    





    
def apariencia():
    global modo_noche
    if var.get() == 1:
        modo_noche = True
        aplicar_paleta(colores_modo_noche)
    else:
        modo_noche = False
        aplicar_paleta(colores_modo_dia)
    
  
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


#checkbutton cambio de apariencia
var = tk.IntVar()

casilla = tk.Checkbutton(
  ventana, 
  text="Darkmode", 
  onvalue=1, 
  offvalue=0,
  variable=var,
  command=apariencia,
  
  font=('Helvetica', 13,'bold')
)

casilla.pack(anchor='e',pady=2,padx=20)


#visor
visor = tk.Entry(ventana,
                 width = 20,
                 font=('Helvetica', 16,'bold'),
                 fg='#eef0f2',
                 bg='#eef0f2',relief="ridge",borderwidth=2
                 )

visor.insert(0, entrada_inicial)
visor.bind('<FocusIn>',on_entry_click)
visor.pack(pady=1)


#boton para buscar
boton_buscar = 'Obtener informacion'
boton =tk.Button(ventana,
          text=boton_buscar,
          font=('Helvetica',20,'bold'), 
          command=obtener_info
          )
boton.pack(pady=8)

#frame (cuadro) para el area de resultados



frame_interior = tk.Frame(ventana)
frame_interior.pack(fill='both',padx=10,pady=10,expand=True)
frame_interior.grid_columnconfigure(0,weight=1)
frame_interior.grid_columnconfigure(1,weight=1)
frame_interior.grid_columnconfigure(2,weight=1)
frame_interior.grid_columnconfigure(3,weight=1)



#iniciar con paleta dia
aplicar_paleta(colores_modo_dia)

ventana.mainloop()