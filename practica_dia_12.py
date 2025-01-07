from tkinter import *


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
                      font=('Dosis',43), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0,column=0)


#Panel izquierdo
panel_izq = Frame(aplicacion,bd=1,relief=FLAT)
panel_izq.pack(side=LEFT)

#Panel de costos
panel_costos = Frame(panel_izq,bd=1,relief=FLAT)
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
                         font=('Dosis',10,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_comidas[contador])
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
                         font=('Dosis',10,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_bebidas[contador])
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
                         font=('Dosis',10,'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_postres[contador])
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


#Etiquetas de costo
etiqueta_costo_comida=Label(panel_costos,
                            text='Costo comida:',
                            font=('Dosis',12,'bold'),
                            bg='azure4',
                            fg='white')
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida= Entry(panel_costos,
                          font=('Dosis',12,'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_costo_comida)
texto_costo_comida.grid(row=0,column=1)

#Evitar cierre de pantalla
aplicacion.mainloop()