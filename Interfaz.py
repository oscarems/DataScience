from matplotlib.widgets import Button
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from datetime import datetime
import tkinter
from tkinter import ttk
from tkinter import *


# archivo
archivo = 'F:\Personal\Python\Data Science\owid-covid-data_3.csv'
data_covid = pd.read_csv(archivo)

Paises = data_covid['location']
Paises = Paises.drop_duplicates()
Paises = Paises.values.tolist()

Variables = data_covid.columns
Variables = Variables.values.tolist()

Lista_Fechas = data_covid['date']
Lista_Fechas = Lista_Fechas.drop_duplicates()
Lista_Fechas = Lista_Fechas.values.tolist()


del Variables[-1:3]


# Funciones
def graficar():

    pais = lista_paises.get()
    Variable_interes = lista_Variables.get()
    interes = data_covid.loc[data_covid['location'] == pais]

    a = interes.index[interes['date'] == Fechas0.get()].tolist()
    a = a[0]
    b = interes.index[interes['date'] == Fechas1.get()].tolist()
    b = b[0]
    interes = interes.loc[a:b, :]

    ax.clear()
    ax.set_xlabel('Date')
    ax.set_ylabel(Variable_interes)
    ax.grid(True)
    ax.plot(interes['date'], interes[Variable_interes])
    titulo = 'Country: ' + pais + ', Variable: '+Variable_interes
    ax.set_title(titulo)
    canvas.draw()

    pais = []
    Variable_interes = []
    interes = []
    a = []
    b = []


# Ventana
ventana = tkinter.Tk()
ventana.title("Interfaz CoronaVirus")
ventana.geometry('1500x1000')


# Frame Opciones
Opciones = LabelFrame(ventana, text="Variables")
Opciones.pack(fill="both", expand="yes", side='left')


# Lista de Paises
Pai = Label(Opciones, width=40, text='Choose a country')
Pai.place(x=50, y=100)
lista_paises = ttk.Combobox(Opciones, width=40, state='readonly')
lista_paises.place(x=300, y=100)
lista_paises['values'] = Paises


# Lista de Variables

Vari = Label(Opciones, width=40, text='Choose variable')
Vari.place(x=50, y=200)
lista_Variables = ttk.Combobox(Opciones, width=40, state='readonly')
lista_Variables.place(x=300, y=200)
lista_Variables['values'] = Variables

# Fechas


Fecha0 = Label(Opciones, width=40, text='First date')
Fecha0.place(x=50, y=300)
Fechas0 = ttk.Combobox(Opciones, width=40, state='readonly')
Fechas0.place(x=300, y=300)
Fechas0['values'] = Lista_Fechas


Fecha1 = Label(Opciones, width=40, text='Final date')
Fecha1.place(x=50, y=400)
Fechas1 = ttk.Combobox(Opciones, width=40, state='readonly')
Fechas1.place(x=300, y=400)
Fechas1['values'] = Lista_Fechas

# Boton para Graficar
Button(Opciones, text='Plot', command=graficar).place(x=500, y=700)


# Frame Opciones
Graficos = LabelFrame(ventana, text='Plots')
Graficos.pack(fill="both", expand="yes", side='right')

# Figura

fig = plt.figure()
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, Graficos)
canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, Graficos)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()
