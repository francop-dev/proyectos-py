import tkinter as tk


#crear la ventana principal
ventana = tk.Tk()
ventana.title('Mi calculadora')

# Cambiar icono de la app
ruta_icono = "C:/Users/franco/Desktop/proyectos-python/calculadora/calculadora.ico"
ventana.iconbitmap(ruta_icono)

#variable para almacenar la expresion matematica
expresion = ''

#variable para almacenar el estado del visor
resultado_mostrado = False

#funcion para actualizar la expresion en el cuadro de texto
def pulsar_tecla(tecla):
    global expresion, resultado_mostrado
    
    #evaluar si en la pantalla hay un resultado
    if resultado_mostrado:
        #evaluar si se presiono un numero o el ".", reiniciar el visor
        if tecla.isdigit() or tecla == '.':
            expresion = str(tecla)
        else:
            expresion = str(expresion) + str(tecla)
        resultado_mostrado = False
    else:
        expresion += str(tecla)
        
    visor_texto.set(expresion)

#funcion de limpiar la entrada
def limpiar():
    global expresion, resultado_mostrado
    
    expresion = ""
    visor_texto.set(expresion)
    resultado_mostrado = False

#funcion para evaluar la expresion y mostrar el resultado
def evaluar():
    global expresion, resultado_mostrado
    
    try: 
        resultado = eval(expresion)
        #verificar si el resultado es un numero entero
        if resultado == int(resultado):
            resultado = int(resultado)

        visor_texto.set(str(resultado))
        expresion = resultado
        resultado_mostrado = True
    
    except:
        visor_texto.set('Error')
        expresion = ''
        resultado_mostrado = False
    

#configurar el tamaño dinamico de las columnas y filas

for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)

for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)
    
#cuadro de texto para mostrar las expresiones y resultado

visor_texto = tk.StringVar()
visor = tk.Entry(ventana,
                 textvariable = visor_texto,
                 font=('Helvetica', 32,'bold'),
                 bd=10,
                 bg='#A8DADC',
                 insertwidth=4,
                 width=14,
                 borderwidth=2,
                 justify='right',
                 relief='sunken',)

visor.grid(row=0,
           column=0,
           columnspan=6,
           sticky='nsew')


#botones
botones_numeros = [
    ('7',1,0),('8',1,1),('9',1,2),
    ('4',2,0),('5',2,1),('6',2,2),
    ('1',3,0),('2',3,1),('3',3,2),
    ('0',4,0)
]

botones_operaciones = [
    ('/',1,3),('*',2,3),('-',3,3),('+',4,3),
    ('C',4,2),('.',4,1)
]

#ubicacion de botones
for (numero,fila,columna) in botones_numeros:
    if numero == 'C':
        comando = limpiar
    
    else:
        comando = lambda x=numero: pulsar_tecla(x)
        
    tk.Button(ventana,
              text=numero,
              padx=20,
              pady=20,
              font=('Helvetica',20),
              bg='#0094C6',
              relief = 'raised',
              command=comando
              ).grid(row=fila,
                     column=columna,
                     sticky='nsew')

#botones operadores
for (numero,fila,columna) in botones_operaciones:
    if numero == 'C':
        comando = limpiar
    
    else:
        comando = lambda x=numero: pulsar_tecla(x)
        
    tk.Button(ventana,
              text=numero,
              padx=20,
              pady=20,
              font=('Helvetica',20),
              bg='#001242',
              fg='#005E7C',
              command=comando
              ).grid(row=fila,
                     column=columna,
                     sticky='nsew')

#boton '='

tk.Button(ventana,
          text='=',
          padx=20,
          pady=20,
          font=('Helvetica',40,'bold'),
          bg='#0C7C59',
          fg='#005E7C',
          command=evaluar).grid(row=5,
                                      column=0,
                                      columnspan=4,
                                      sticky='nsew')

#ejecutar aplicacion
ventana.mainloop()

