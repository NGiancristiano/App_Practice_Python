from tkinter import *
import random
import datetime
from tkinter import filedialog,messagebox



#Funcion mostrar numeros calculadora en pantalla
operador=''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_button(num):
    global operador
    operador = operador + num
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)

#Funcion borrar
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

#Obtener resultado
def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador = ''


#Funcion revisar checks
def revisar_check():
    x=0
    for c in cuadro_comidas:
        if variable_comidas[x].get() == 1:
            cuadro_comidas[x].config(state=NORMAL)
            if cuadro_comidas[x].get() == '0':
                cuadro_comidas[x].delete(0,END)
            cuadro_comidas[x].focus()
        else:
            cuadro_comidas[x].config(state=DISABLED)
            texto_comidas[x].set('0')
        x += 1


    x=0
    for c in cuadro_bebidas:
        if variable_bebidas[x].get() == 1:
            cuadro_bebidas[x].config(state=NORMAL)
            if cuadro_bebidas[x].get() == '0':
                cuadro_bebidas[x].delete(0,END)
            cuadro_bebidas[x].focus()
        else:
            cuadro_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1


    x=0
    for c in cuadro_postres:
        if variable_postres[x].get() == 1:
            cuadro_postres[x].config(state=NORMAL)
            if cuadro_postres[x].get() == '0':
                cuadro_postres[x].delete(0,END)
            cuadro_postres[x].focus()
        else:
            cuadro_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


#Funcion para calcular el total
def total():
    sub_total_comida = 0
    p=0
    for cant in texto_comidas:
        sub_total_comida = sub_total_comida + (float(cant.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p=0
    for cant in texto_bebidas:
        sub_total_bebida = sub_total_bebida + (float(cant.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p=0
    for cant in texto_postres:
        sub_total_postres = sub_total_postres + (float(cant.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'${round(sub_total_comida,2)}')
    var_costo_bebida.set(f'${round(sub_total_bebida,2)}')
    var_costo_postre.set(f'${round(sub_total_postres,2)}')
    var_subtotal.set(f'${round(sub_total,2)}')
    var_impuesto.set(f'${round(impuestos,2)}')
    var_total.set(f'${round(total,2)}')


#Funcion para rellenar el recibo
def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END,f'Datos:{num_recibo}\t{fecha_recibo}\n')
    texto_recibo.insert(END,f'*'*42+'\n')
    texto_recibo.insert(END,f'Items\t\tCant\tCosto\n')
    texto_recibo.insert(END,f'-'*51+'\n')

    x=0
    for comida in texto_comidas:
        if comida.get() != '0':
            texto_recibo.insert(END,f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                    f'${int(comida.get())*precios_comida[x]}\n')
        x += 1


    x=0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END,f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                    f'${int(bebida.get())*precios_bebida[x]}\n')
        x += 1


    x=0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END,f'{lista_postres[x]}\t\t{postres.get()}\t'
                                    f'${int(postres.get())*precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 51 + '\n')
    texto_recibo.insert(END,f'Costo comida:\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END,f'Costo bebida:\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END,f'Costo postre:\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 51 + '\n')
    texto_recibo.insert(END,f'Sub-Total:\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END,f'Impuestos:\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END,f'Total:\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 42 + '\n')


#Funcion para guardar el recibo en un archivo
def guardar():
    info_recibo = texto_recibo.get(1.0,END)
    archivo = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion','Su recibo ha sido guardado')


#Funcion para resetear toda la pantalla
def resetear():
    texto_recibo.delete(0.1,END)

    for text in texto_comidas:
        text.set('0')
    for text in texto_bebidas:
        text.set('0')
    for text in texto_postres:
        text.set('0')

    for cuadro in cuadro_comidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postres:
        cuadro.config(state=DISABLED)

    for var in variable_comidas:
        var.set(0)
    for var in variable_bebidas:
        var.set(0)
    for var in variable_postres:
        var.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')


#Iniciar TkInter
aplicacion = Tk()

#Tamano de la ventana
aplicacion.geometry("800x600+0+0")

#Titulo
aplicacion.title('Restaurante')

#Evitar minimizar
aplicacion.resizable(0,0)

#Cambiar color fondo
aplicacion.config(bg='burlywood4')

#Panel superior
panel_superior = Frame(aplicacion,bd=1,relief=FLAT)
panel_superior.pack(side=TOP)

#Etiqueta titulo
etiqueta_titulo=Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                      font=('Dosis',47,'bold'), bg='burlywood', width=20, height=2)
etiqueta_titulo.grid(row=0,column=0)


#Panel izquierdo
panel_izq = Frame(aplicacion,bd=1,relief=FLAT)
panel_izq.pack(side=LEFT)

#Panel de costos
panel_costos = Frame(panel_izq,bd=1,relief=FLAT,bg='azure4')
panel_costos.pack(side=BOTTOM)

#Panel comidas
panel_comidas = LabelFrame(panel_izq, text='Comidas', font=('Dosis',15,'bold'), bd=1,
                           relief=FLAT,fg='azure4')
panel_comidas.pack(side=LEFT)


#Panel bebidas
panel_bebidas = LabelFrame(panel_izq, text='Bebidas', font=('Dosis',15,'bold'), bd=1,
                           relief=FLAT,fg='azure4')
panel_bebidas.pack(side=LEFT)

#Panel postres
panel_postres = LabelFrame(panel_izq, text='Postres', font=('Dosis',15,'bold'), bd=1,
                           relief=FLAT,fg='azure4')
panel_postres.pack(side=LEFT)


#Panel derecha
panel_derecha = Frame(aplicacion,bd=1,relief=FLAT)
panel_derecha.pack(side=RIGHT)

#Panel calculadora
panel_calculadora = Frame(panel_derecha,bd=1,relief=FLAT)
panel_calculadora.pack()

#Panel recibo
panel_recibo = Frame(panel_derecha,bd=1,relief=FLAT)
panel_recibo.pack()

#Panel botones
panel_botones = Frame(panel_derecha,bd=1,relief=FLAT)
panel_botones.pack()


#Lista de productos
lista_comidas=['pollo','carne','pastas','kebab','pizza1','pizza2','matambre','canelones']
lista_bebidas = ['agua','soda','jugo','coca','vino1','vino2','cerveza1','cerveza2']
lista_postres = ['helado','flan','torta','tiramisu','brownie','lemon pie','fruta','panqueque']


#Generar lista comidas
variable_comidas=[]
cuadro_comidas = []
texto_comidas = []
contador = 0


for comida in lista_comidas:
    #Crear checkbuttons
    variable_comidas.append('')
    variable_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis',15,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_comidas[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    #Crear cuadros de entrada
    cuadro_comidas.append('')
    texto_comidas.append('')
    texto_comidas[contador]=StringVar()
    texto_comidas[contador].set('0')
    cuadro_comidas[contador] = Entry(panel_comidas,
                                     font=('Dosis',10),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comidas[contador])
    cuadro_comidas[contador].grid(row=contador,
                                  column=1)

    contador += 1


#Generar lista bebidas
variable_bebidas=[]
cuadro_bebidas = []
texto_bebidas = []
contador = 0

for bebida in lista_bebidas:

    # Crear checkbuttons
    variable_bebidas.append('')
    variable_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis',15,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_bebidas[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    #Crear cuadros de entrada
    cuadro_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador]=StringVar()
    texto_bebidas[contador].set('0')
    cuadro_bebidas[contador] = Entry(panel_bebidas,
                                     font=('Dosis',10),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebidas[contador])
    cuadro_bebidas[contador].grid(row=contador,
                                  column=1)

    contador += 1


#Generar lista postres
variable_postres=[]
cuadro_postres = []
texto_postres = []
contador = 0

for postre in lista_postres:

    # Crear checkbuttons
    variable_postres.append('')
    variable_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis',15,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_postres[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)

    #Crear cuadros de entrada
    cuadro_postres.append('')
    texto_postres.append('')
    texto_postres[contador]=StringVar()
    texto_postres[contador].set('0')
    cuadro_postres[contador] = Entry(panel_postres,
                                     font=('Dosis',10),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadro_postres[contador].grid(row=contador,
                                  column=1)

    contador += 1


#Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()


#Etiquetas de costo comida
etiqueta_costo_comida=Label(panel_costos,
                            text='Costo comida:',
                            font=('Dosis',15,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_comida.grid(row=0,column=0,padx=15)

texto_costo_comida= Entry(panel_costos,
                          font=('Dosis',10,'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1,padx=15)

#Etiquetas de costo bebida
etiqueta_costo_bebida=Label(panel_costos,
                            text='Costo bebida:',
                            font=('Dosis',15,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_bebida.grid(row=1,column=0,padx=15)

texto_costo_bebida= Entry(panel_costos,
                          font=('Dosis',10,'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1,column=1,padx=15)


#Etiquetas de costo postre
etiqueta_costo_postre=Label(panel_costos,
                            text='Costo postre:',
                            font=('Dosis',15,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_postre.grid(row=2,column=0,padx=15)

texto_costo_postre= Entry(panel_costos,
                          font=('Dosis',10,'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_costo_postre)
texto_costo_postre.grid(row=2,column=1,padx=15)

#Etiquetas de subtotal
etiqueta_subtotal=Label(panel_costos,
                            text='Subtotal:',
                            font=('Dosis',15,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_subtotal.grid(row=0,column=2,padx=15)

texto_subtotal= Entry(panel_costos,
                          font=('Dosis',10,'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_subtotal)
texto_subtotal.grid(row=0,column=3,padx=15)


#Etiquetas de impuesto
etiqueta_impuesto=Label(panel_costos,
                            text='Impuesto:',
                            font=('Dosis',15,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_impuesto.grid(row=1,column=2,padx=15)

texto_impuesto= Entry(panel_costos,
                          font=('Dosis',10,'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_impuesto)
texto_impuesto.grid(row=1,column=3,padx=15)


#Etiquetas de total
etiqueta_total=Label(panel_costos,
                            text='Total:',
                            font=('Dosis',15,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_total.grid(row=2,column=2,padx=15)

texto_total= Entry(panel_costos,
                          font=('Dosis',10,'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_total)
texto_total.grid(row=2,column=3,padx=15)


#Botones
botones = ['Total','Recibo','Guardar','Resetear']
columnas = 0
botones_creados = []
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis',10,'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=7)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

#Recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis',11,'bold'),
                    bd=1,
                    width=32,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)


#Calculadora

visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis',11,'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)


#Botones calculadora
botones_calculadora=['7','8','9','+','4','5','6','-','1','2','3','x','R','B','0','/']
botones_guardados=[]

fila=1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis',11,'bold'),
                   bd=1,
                   fg='white',
                   bg='azure4',
                   width=6)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1

    columna += 1
    if columna == 4:
        columna = 0


botones_guardados[0].config(command=lambda : click_button('7'))
botones_guardados[1].config(command=lambda : click_button('8'))
botones_guardados[2].config(command=lambda : click_button('9'))
botones_guardados[3].config(command=lambda : click_button('+'))
botones_guardados[4].config(command=lambda : click_button('4'))
botones_guardados[5].config(command=lambda : click_button('5'))
botones_guardados[6].config(command=lambda : click_button('6'))
botones_guardados[7].config(command=lambda : click_button('-'))
botones_guardados[8].config(command=lambda : click_button('1'))
botones_guardados[9].config(command=lambda : click_button('2'))
botones_guardados[10].config(command=lambda : click_button('3'))
botones_guardados[11].config(command=lambda : click_button('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_button('0'))
botones_guardados[15].config(command=lambda : click_button('/'))




#Evitar cierre de pantalla
aplicacion.mainloop()