import ply.yacc as yacc
import os
import codecs
import re
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
from tkinter import ttk, messagebox
from tkinter.ttk import *
from tkinter import Menu
from Nodo import Nodo
from Distribuido import Distribuido
import copy
import statistics
from analizadorSintactico import *
from analizadorLexico import tokens


class Simulacion:
    def __init__(self):

        # Se define el archivo que tiene los comandos para la creacion de nodos
        self.commands = open("commands.txt", "r")

        # Se define el diccionario que tiene instanciados los nodos
        self.nodos = {}
        self.procesarArchivo()

        # Se define el computador distribuido y se agregan los recursos
        self.superPC = Distribuido()

        self.extraerRecursos()

        #Se define la ventana y su titulo
        self.ventana = tk.Tk()
        self.ventana.title("Simulador Ad hoc ")
        self.ventana.resizable(0, 0)
        self.ventana.protocol('WM_DELETE_WINDOW', self.estadisticas)

        #Se define el menu y se asocia a la ventana
        self.menu = Menu(self.ventana)

        #Se definen los items del menu y se asocian al menu
        self.itemMenuAbrir = Menu(self.menu)
        self.itemMenuVer = Menu(self.menu)

        self.itemMenuAbrir.add_command(label='Procesador de Lenguaje', command=self.openProcesador)
        self.itemMenuVer.add_command(label="Nodos", command=self.openVerNodos)
        self.itemMenuVer.add_command(label="Computador distribuido", command=self.openSuperPC)

        self.menu.add_cascade(label='Abrir', menu=self.itemMenuAbrir)
        self.menu.add_cascade(label='Ver', menu=self.itemMenuVer)
        self.ventana.config(menu=self.menu)

        #Se definen los atributos para las estadísticas
        self.registro_RAM=[]
        self.registro_MEMORIA=[]
        self.registro_VELOCIDAD=[]
        self.registro_participacion = []

        #Se definen los nodos participantes en la red y los que no
        #Tambien se definen las coordenadas de los participantes y los no participantes
        self.x_participantes = []
        self.y_participantes = []

        self.x_no_participantes = []
        self.y_no_participantes = []

        self.ids_participantes = []
        self.ids_no_participantes = []
        self.actualizarParticipantes()

        #Se definen los diccionarios para volverlos dataframe
        self.posiciones_participantes = {'x': [],
                          'y': []
                          }
        self.posiciones_no_participantes = {'x': [],
                         'y': []
                         }

        #Se definen los dataframes
        self.posicionesDATAFRAME_participantes = DataFrame([], columns=['x', 'y'])
        self.posicionesDATAFRAME_no_participantes = DataFrame([], columns=['x', 'y'])

        # Se inicializa la figura
        self.figura = plt.Figure(figsize=(4, 4), dpi=100)
        self.ejes = self.figura.add_subplot(111)

        self.graficoDispersion = FigureCanvasTkAgg(self.figura, self.ventana)

        self.actualizarDataFrames()

        # Se agregan los botones para manejar la simulación
        tk.Button(self.ventana, text="Siguiente", bg="#36FF33", command=self.simular).grid(row=1, column=0, columnspan=2)

        #Se agregan los elementos para enviar mensajes
        '''self.labelEnviar = Label(self.ventana, text="Enviar Mensaje de: ").grid(row=2, column=0, pady=15, padx=0)
        self.comboboxEmisor = ttk.Combobox(self.ventana,
                                      values=[]).grid(row=2, column=1, pady=15)
        self.labelA = Label(self.ventana, text="A nodo:").grid(row=3, column=0, pady=15)
        self.comboboxReceptor = ttk.Combobox(self.ventana,
                                        values=[]).grid(row=3, column=1, pady=15)
        tk.Button(self.ventana, text="Enviar", bg="#FFE033", command=self.enviar).grid(row=4, column=0, pady=15, columnspan=2)

        self.actualizarComboBox()'''

    # Metodo que abre la ventana del procesador de lenguaje (Se utiliza al abrir el menu -> Procesador de Lenguaje)
    def openProcesador(self):
        ventanaProcesador = tk.Toplevel(self.ventana)
        ventanaProcesador.geometry("400x400")
        ventanaProcesador.title("Procesador de lenguaje")
        labelExample = tk.Label(ventanaProcesador, text="Ingrese el texto a procesar...").grid(row=0, column=0)
        textArea = tk.Text(ventanaProcesador, height=20, width=50)
        textArea.grid(row=1, column=0)
        botonInicioProcesamiento = tk.Button(ventanaProcesador, text="Procesar", bg="green",
                                             command=lambda: self.procesar(textArea)).grid(row=2, column=0)

    def openVerNodos(self):
        ventanaVerNodos = tk.Toplevel(self.ventana)
        ventanaVerNodos.geometry("220x500")
        ventanaVerNodos.title("Ver Nodos")
        label = tk.Label(ventanaVerNodos, text="Seleccione el nodo que quiera ver").grid(row=0, column=0)
        ids_nodos = []
        for clave,valor in self.nodos.items():
                ids_nodos.append(valor.identificador)
        comboboxNodos = ttk.Combobox(ventanaVerNodos, values=ids_nodos)
        comboboxNodos.grid(row=1, column=0)

        botonVer = tk.Button(ventanaVerNodos, text="Ver", bg="yellow",command=lambda: self.verNodo(comboboxNodos.get(),ventanaVerNodos)).grid(row=2, column=0,pady=5)

    def openSuperPC(self):
        ventanaSuperPC = tk.Toplevel(self.ventana)

        frame = tk.Frame(ventanaSuperPC)
        frame.grid(row=20, column=1)
        ventanaSuperPC.geometry("290x500")
        ventanaSuperPC.title("Ver Computador Distribuido")

        label_CPU = tk.Label(frame, text="Computador Distribuido", fg="red", font=("Helvetica", 13)).grid(row=1, column=0, pady=5)
        label_totalRAM = tk.Label(frame, text="TOTAL RAM (GB): "+str("{0:.2f}".format(self.superPC.getRAM_GB())), font=("Helvetica", 11)).grid(row=2, column=0, pady=5)
        label_totalMEMORIA = tk.Label(frame, text="TOTAL MEMORIA (GB): "+str("{0:.2f}".format(self.superPC.getMEMORIA_GB())), font=("Helvetica", 11)).grid(row=3, column=0, pady=5)
        label_totalVELOCIDAD = tk.Label(frame, text="TOTAL PROCESAMIENTO (GHz): "+str("{0:.2f}".format(self.superPC.getVELOCIDAD())), font=("Helvetica", 11)).grid(row=4, column=0, pady=5)

        print("Computador Distribuido")
        print("\tTOTAL RAM (GB): "+str("{0:.2f}".format(self.superPC.getRAM_GB())))
        print("\tTOTAL MEMORIA (GB): "+str("{0:.2f}".format(self.superPC.getMEMORIA_GB())))
        print("\tTOTAL PROCESAMIENTO (GHz): "+str("{0:.2f}".format(self.superPC.getVELOCIDAD())))
        print("______________________________________________________________________")
        label_separador = tk.Label(frame, text="___________________________________", font=("Helvetica", 11)).grid(row=5, column=0, pady=5)

        cantidadParti=0
        for clave, valor in self.nodos.items():
            if (valor.participando):
                cantidadParti = cantidadParti+1

        label_participantes = tk.Label(frame, text="Participantes ("+str(cantidadParti)+")", fg="red", font=("Helvetica", 13)).grid(row=6, column=0, pady=5)

        row_counter=8
        for clave, valor in self.nodos.items():
            if(valor.participando):
                tk.Label(frame, text="ID: "+str(valor.identificador), font=("Helvetica", 8)).grid(row=row_counter, column=0)
                print("ID: "+str(valor.identificador))
                row_counter=row_counter+1
                tk.Label(frame, text="Modelo:"+str(valor.fabricante)+" "+str(valor.modelo), font=("Helvetica", 8)).grid(row=row_counter, column=0)
                print("\tModelo:"+str(valor.fabricante)+" "+str(valor.modelo))
                row_counter=row_counter+1

                id, ram, memoria, velocidad = valor.obtenerRecursos()
                tk.Label(frame, text="RAM cedida (GB): " + str("{0:.2f}".format(ram)),font=("Helvetica", 8)).grid(row=row_counter, column=0)
                print("\tRAM cedida (GB): " + str("{0:.2f}".format(ram)))
                row_counter = row_counter + 1
                tk.Label(frame, text="Memoria cedida (GB): " + str("{0:.2f}".format(memoria)),font=("Helvetica", 8)).grid(row=row_counter, column=0)
                print("\tMemoria cedida (GB): " + str("{0:.2f}".format(memoria)))
                row_counter = row_counter + 1
                tk.Label(frame, text="Procesamiento cedido (GHz): " + str("{0:.2f}".format(velocidad)),font=("Helvetica", 8)).grid(row=row_counter, column=0)
                print("\tProcesamiento cedido (GHz): " + str("{0:.2f}".format(velocidad)))
                row_counter = row_counter + 1
                tk.Label(frame, text="___________________________________", font=("Helvetica", 8)).grid(row=row_counter,column=0,pady=5)
                print("______________________________________________________________________")
                row_counter = row_counter + 1

    # Metodo que verifica si lo que hay en el textArea es valido para el procesador de lenguaje
    def valido(self,TextArea):
        texto = TextArea.get("1.0","end-1c")
        parser = yacc.yacc()
        result = parser.parse(texto) 
        
        f = open("datos.txt", "r")
        Lines = f.readlines() 
        f = open ("datos.txt", "w")
        f.write("")
        f.close()
        for i in Lines:
            if i == 'Sintax error\n':
                return False
        return True

    # Metodo que ejecuta el procesador de lenguaje
    def procesar(self,TextArea):
        if (self.valido(TextArea)):
            messagebox.showinfo('Procesador de lenguaje', 'El texto es valido')
        else:
            messagebox.showinfo('Procesador de lenguaje', 'El texto NO es valido')

    #Metodo que lee el archivo de texto y se crean los nodos
    def procesarArchivo(self):

        for linea in self.commands.readlines():
            lista_tokens = linea.split("\t")
            movimiento_args = lista_tokens[4].split(",")
            coordenadas = lista_tokens[5].split(",")

            nodoAux = Nodo(lista_tokens[1], lista_tokens[2],lista_tokens[3],int(movimiento_args[0]),int(movimiento_args[1]), int(coordenadas[0]),int(coordenadas[1]))

            self.nodos[nodoAux.identificador]=copy.copy(nodoAux)

    #Metodo que actualiza la lista de participantes segun si atributo 'participando'
    def actualizarParticipantes(self):

        #Se reinician las listas de participantes
        self.x_participantes = []
        self.y_participantes = []

        self.x_no_participantes = []
        self.y_no_participantes = []

        self.ids_participantes = []
        self.ids_no_participantes = []

        for clave,valor in self.nodos.items():
            if(valor.participando):
                self.x_participantes.append(valor.x_actual)
                self.y_participantes.append(valor.y_actual)
                self.ids_participantes.append(valor.identificador)
            else:
                self.x_no_participantes.append(valor.x_actual)
                self.y_no_participantes.append(valor.y_actual)
                self.ids_no_participantes.append(valor.identificador)

    def actualizarDataFrames(self):
        #Se reinician los atributos

        self.posiciones_participantes = {'x': self.x_participantes,
                                         'y': self.y_participantes
                                         }
        self.posiciones_no_participantes = {'x': self.x_no_participantes,
                                            'y': self.y_no_participantes
                                            }

        self.posicionesDATAFRAME_participantes = DataFrame(self.posiciones_participantes, columns=['x', 'y'])
        self.posicionesDATAFRAME_no_participantes = DataFrame(self.posiciones_no_participantes, columns=['x', 'y'])

        self.figura = plt.Figure(figsize=(5, 4), dpi=100)
        self.ejes = self.figura.add_subplot(111)

        self.ejes.scatter(self.posicionesDATAFRAME_participantes['x'], self.posicionesDATAFRAME_participantes['y'],
                          color='green')
        self.ejes.scatter(self.posicionesDATAFRAME_no_participantes['x'],
                          self.posicionesDATAFRAME_no_participantes['y'], color='red')

        self.ejes.set_xlim([-1, 15])
        self.ejes.set_ylim([-5, 15])

        #Se pintan las anotaciones
        for i in range(0,len(self.ids_participantes)):
            self.ejes.annotate(self.ids_participantes[i], xy=(self.x_participantes[i], self.y_participantes[i]))

        for i in range(0,len(self.ids_no_participantes)):
            self.ejes.annotate(self.ids_no_participantes[i], xy=(self.x_no_participantes[i], self.y_no_participantes[i]))


        self.graficoDispersion = FigureCanvasTkAgg(self.figura, self.ventana)


        self.graficoDispersion.get_tk_widget().grid(row=0, column=0, columnspan=2)

    def moverNodos(self):
        for clave,valor in self.nodos.items():
            valor.mover()

    def actualizarComboBox(self):
        self.comboboxEmisor = ttk.Combobox(self.ventana,
                                           values=self.ids_participantes).grid(row=2, column=1, pady=15)
        self.comboboxReceptor = ttk.Combobox(self.ventana,
                                             values=self.ids_participantes).grid(row=3, column=1, pady=15)

    def verNodo(self,identificador,ventana):
        nodoaux = self.nodos[identificador]
        label_ID = tk.Label(ventana, text="ID: "+str(nodoaux.identificador),font=("Helvetica", 11)).grid(row=3, column=0,pady=5)

        label_CPU = tk.Label(ventana, text="CPU",fg="red",font=("Helvetica", 13)).grid(row=4, column=0,pady=5)
        label_MODELO = tk.Label(ventana, text="Modelo:"+str(nodoaux.fabricante)+" "+str(nodoaux.modelo),font=("Helvetica", 11)).grid(row=5, column=0)
        label_RAM = tk.Label(ventana, text="RAM (GB): "+str(nodoaux.RAM_GB),font=("Helvetica", 11)).grid(row=6, column=0)
        label_MEMORIA = tk.Label(ventana, text="Memoria (GB): "+str(len(nodoaux.MEMORIA_GB)),font=("Helvetica", 11)).grid(row=7, column=0)
        label_PROCESADOR = tk.Label(ventana, text="Procesador: "+str(nodoaux.procesador)+"  ["+str(nodoaux.velocidad)+" Ghz]",font=("Helvetica", 11)).grid(row=8, column=0)

        label_ADHOC = tk.Label(ventana, text="AD-HOC",fg="red",font=("Helvetica", 13)).grid(row=9, column=0,pady=5)
        label_porc_parti = tk.Label(ventana, text="Participacion (%): "+str(nodoaux.porc_part),font=("Helvetica", 11)).grid(row=10, column=0)
        label_participando = tk.Label(ventana, text="Participando actualmente: "+str(nodoaux.participando),font=("Helvetica", 11)).grid(row=11, column=0)

        rowCounter=12
        if(nodoaux.participando):
            id,ram,memoria,velocidad = nodoaux.obtenerRecursos()
            label_RAM_CEDIDA = tk.Label(ventana, text="RAM cedida (GB): "+str("{0:.3f}".format(ram)),font=("Helvetica", 11)).grid(row=rowCounter, column=0)
            rowCounter=rowCounter+1

            label_RAM_CEDIDA = tk.Label(ventana, text="Memoria cedida (GB): "+str("{0:.3f}".format(memoria)),font=("Helvetica", 11)).grid(row=rowCounter, column=0)
            rowCounter=rowCounter+1

            label_RAM_CEDIDA = tk.Label(ventana, text="Procesamiento cedido (GHz): "+str("{0:.3f}".format(velocidad)),font=("Helvetica", 11)).grid(row=rowCounter, column=0)
            rowCounter=rowCounter+1

        label_ADHOC = tk.Label(ventana, text="MOVIMIENTO", fg="red", font=("Helvetica", 13)).grid(row=rowCounter, column=0, pady=5)
        rowCounter = rowCounter + 1
        label_coordenadas = tk.Label(ventana, text="Coordenadas: ( " + str(nodoaux.x_actual)+" , "+str(nodoaux.y_actual)+" )",font=("Helvetica", 11)).grid(row=rowCounter, column=0)
        rowCounter = rowCounter + 1
        label_movimiento = tk.Label(ventana, text="Movimiento: "+str(nodoaux.movimiento)+" ["+str(nodoaux.arg_movimiento)+";"+str(nodoaux.paso)+"]",font=("Helvetica", 11)).grid(row=rowCounter, column=0)


    def extraerRecursos(self):
        self.superPC.nombres_participantes = []
        self.superPC.RAM_GB = []
        self.superPC.MEMORIA_GB = []
        self.superPC.VELOCIDAD = []

        for clave, valor in self.nodos.items():
            if (valor.participando):
                identificador,RAM,MEMORIA,VELOCIDAD = valor.obtenerRecursos()
                self.superPC.agregarRecursos(identificador,RAM,MEMORIA,VELOCIDAD)

    def actualizarEstadisticas(self):
        self.registro_RAM.append(float(self.superPC.getRAM_GB()))
        self.registro_MEMORIA.append(float(self.superPC.getMEMORIA_GB()))
        self.registro_VELOCIDAD.append(float(self.superPC.getVELOCIDAD()))
        self.registro_participacion.append(float((len(self.ids_participantes))/(len(self.nodos))))

    # Método que inicia la simulacion
    def simular(self):
        self.actualizarEstadisticas()
        self.moverNodos()
        self.actualizarParticipantes()
        self.extraerRecursos()
        self.actualizarDataFrames()
        #self.actualizarComboBox()


    def enviar(self):
        print("Enviando mensaje")

    def estadisticas(self):

        ventanaestadisticas = tk.Toplevel(self.ventana)
        ventanaestadisticas.protocol('WM_DELETE_WINDOW', self.cerrarTodo)

        ventanaestadisticas.geometry("350x200")
        ventanaestadisticas.title("Estadisticas")

        promedio_RAM = 0
        promedio_MEMORIA = 0
        promedio_VELOCIDAD = 0
        promedio_Participacion = 0

        if(self.registro_RAM!=[]):
            promedio_RAM = statistics.mean(self.registro_RAM)

        if (self.registro_MEMORIA != []):
            promedio_MEMORIA = statistics.mean(self.registro_MEMORIA)

        if (self.registro_VELOCIDAD != []):
            promedio_VELOCIDAD = statistics.mean(self.registro_VELOCIDAD)

        if (self.registro_participacion != []):
            promedio_Participacion = statistics.mean(self.registro_participacion)

        tk.Label(ventanaestadisticas, text="ESTADISTICAS - Computador Distribuido", fg="red", font=("Helvetica", 13)).grid(row=0, column=0, pady=5)
        tk.Label(ventanaestadisticas, text="Promedio RAM cedida (GB): "+str("{0:.3f}".format(promedio_RAM)),  font=("Helvetica", 11)).grid(row=1,column=0,pady=5)
        tk.Label(ventanaestadisticas, text="Promedio MEMORIA cedida (GB): "+str("{0:.3f}".format(promedio_MEMORIA)),  font=("Helvetica", 11)).grid(row=2,column=0,pady=5)
        tk.Label(ventanaestadisticas, text="Promedio Procesamiento cedido (GHz): "+str("{0:.3f}".format(promedio_VELOCIDAD)),  font=("Helvetica", 11)).grid(row=3,column=0,pady=5)
        tk.Label(ventanaestadisticas, text="Promedio participacion de nodos (%): "+str("{0:.3f}".format(promedio_Participacion)),  font=("Helvetica", 11)).grid(row=4,column=0,pady=5)

    def cerrarTodo(self):
        self.ventana.destroy()

    def mostrar(self):
        self.ventana.mainloop()

simulacion = Simulacion()
simulacion.mostrar()