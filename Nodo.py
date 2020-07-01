import numpy as np
import random

class Nodo:
    def __init__(self, identificador, modelo,movimiento,argMovimiento,paso,x,y):
        #Atributos propios del nodo
        self.identificador = identificador
        self.x_actual = x
        self.y_actual = y
        self.participando = False

        #Atributos de la maquina
        self.modelo=modelo

        if(modelo=='IPHONE-11'):
            self.fabricante='APPLE'
            self.RAM_GB=4
            self.MEMORIA_GB= np.zeros((1,256))
            self.procesador='A13'
            self.velocidad=2.66
            self.OS='IOS-13'
            self.porc_part=0.6
            self.participarEnRed()

        elif(modelo=='IPHONE-X'):
            self.fabricante='APPLE'
            self.RAM_GB=3
            self.MEMORIA_GB=np.zeros((1,256))
            self.procesador='A11'
            self.velocidad=2.39
            self.OS='IOS-11'
            self.porc_part=0.5
            self.participarEnRed()

        elif(modelo=='IPHONE-8'):
            self.fabricante='APPLE'
            self.RAM_GB=3
            self.MEMORIA_GB=np.zeros((1,256))
            self.procesador='A11'
            self.velocidad=2.39
            self.OS='IOS-11'
            self.porc_part=0.4
            self.participarEnRed()

        elif(modelo=='IPHONE-7'):
            self.fabricante='APPLE'
            self.RAM_GB=2
            self.MEMORIA_GB=np.zeros((1,256))
            self.procesador='A10'
            self.velocidad=2.34
            self.OS='IOS-10'
            self.porc_part=0.3
            self.participarEnRed()

        elif(modelo=='GALAXY-A-Q'):
            self.fabricante='SAMSUNG'
            self.RAM_GB=8
            self.MEMORIA_GB=np.zeros((1,128))
            self.procesador='CORTEX-A77'
            self.velocidad=2.2
            self.OS='ANDROID-10'
            self.porc_part=0.6
            self.participarEnRed()

        elif(modelo=='GALAXY-A11'):
            self.fabricante='SAMSUNG'
            self.RAM_GB=3
            self.MEMORIA_GB=np.zeros((1,32))
            self.procesador='OCTACORE'
            self.velocidad=1.8
            self.OS='ANDROID-10'
            self.porc_part=0.35
            self.participarEnRed()

        elif(modelo=='GALAXY-A21'):
            self.fabricante='SAMSUNG'
            self.RAM_GB=3
            self.MEMORIA_GB=np.zeros((1,32))
            self.procesador='OCTACORE'
            self.velocidad=1.8
            self.OS='ANDROID-10'
            self.porc_part=0.40
            self.participarEnRed()

        elif(modelo=='GALAXY-Z'):
            self.fabricante='SAMSUNG'
            self.RAM_GB=8
            self.MEMORIA_GB=np.zeros((1,256))
            self.procesador='KYRO'
            self.velocidad=2.95
            self.OS='ANDROID-10'
            self.porc_part=0.65
            self.participarEnRed()

        elif(modelo=='P40'):
            self.fabricante='HUAWEI'
            self.RAM_GB=8
            self.MEMORIA_GB=np.zeros((1,128))
            self.procesador='KIRIN'
            self.velocidad=2.86
            self.OS='ANDROID-10'
            self.porc_part=0.65
            self.participarEnRed()

        elif(modelo=='Y5P'):
            self.fabricante='HUAWEI'
            self.RAM_GB=2
            self.MEMORIA_GB=np.zeros((1,32))
            self.procesador='CORTEX-A53'
            self.velocidad=2.0
            self.OS='ANDROID-10'
            self.porc_part=0.30
            self.participarEnRed()

        elif(modelo=='P30'):
            self.fabricante='HUAWEI'
            self.RAM_GB=6
            self.MEMORIA_GB=np.zeros((1,128))
            self.procesador='CORTEX-A76'
            self.velocidad=2.6
            self.OS='ANDROID-9'
            self.porc_part=0.55
            self.participarEnRed()

        elif(modelo=='P20'):
            self.fabricante='HUAWEI'
            self.RAM_GB=4
            self.MEMORIA_GB=np.zeros((1,128))
            self.procesador='CORTEX-A73'
            self.velocidad=2.4
            self.OS='ANDROID-8'
            self.porc_part=0.5
            self.participarEnRed()

        elif(modelo=='ENVY-13'):#HP ENVY-13
            self.fabricante='HP'
            self.RAM_GB=8
            self.MEMORIA_GB=np.zeros((1,256))
            self.procesador='RYZEN-5'
            self.velocidad=3.7
            self.OS='WINDOWS-10'
            self.porc_part=0.8
            self.participarEnRed()

        elif(modelo=='X-PRO-2020'):#HUAWEI-MATEBOOK
            self.fabricante='HUAWEI-MATEBOOK'
            self.RAM_GB=16
            self.MEMORIA_GB=np.zeros((1,1000))
            self.procesador='I7-10510'
            self.velocidad=4.9
            self.OS='WINDOWS-10'
            self.porc_part=0.9
            self.participarEnRed()

        elif(modelo=='XPS-13'):#DELL
            self.fabricante='DELL'
            self.RAM_GB=8
            self.MEMORIA_GB=np.zeros((1,256))
            self.procesador='I5-8250'
            self.velocidad=3.4
            self.OS='WINDOWS-10'
            self.porc_part=0.85
            self.participarEnRed()

        elif(modelo=='SWIFT-5'):#ACER
            self.fabricante='ACER'
            self.RAM_GB=8
            self.MEMORIA_GB=np.zeros((1,256))
            self.procesador='I5-8265'
            self.velocidad=4.2
            self.OS='WINDOWS-10'
            self.porc_part=0.75
            self.participarEnRed()

        elif(modelo=='S13'):#ASUS-ZENBOOK
            self.fabricante='ASUS-ZENBOOK'
            self.RAM_GB=16
            self.MEMORIA_GB=np.zeros((1,512))
            self.procesador='I5-8565'
            self.velocidad=3.2
            self.OS='WINDOWS-10'
            self.porc_part=0.8
            self.participarEnRed()

        elif(modelo=='YOGA-C740'):#LENOVO YOGA-C740
            self.fabricante='LENOVO'
            self.RAM_GB=8
            self.MEMORIA_GB=np.zeros((1,512))
            self.procesador='I7-10510'
            self.velocidad=4.9
            self.OS='WINDOWS-10'
            self.porc_part=0.65
            self.participarEnRed()

        else:
            print("Modelo no encontrado. Se asignaran caracteristicas de la maquina por defecto:\n"
                  "\tRAM(GB): 2\n"
                  "\tMEMORIA(GB): 128\n"
                  "\tVELOCIDAD(GHz): 2.0\n")
            self.fabricante='DESCONOCIDO'
            self.RAM_GB=2
            self.MEMORIA_GB=np.zeros((1,128))
            self.procesador='DESCONOCIDO'
            self.velocidad=2.0
            self.OS='DESCONOCIDO'
            self.porc_part=0.35
            self.participarEnRed()

        #Atributos del movimiento
        self.movimiento = movimiento
        self.arg_movimiento = argMovimiento
        self.paso= paso
        self.lista_puntos_x = []
        self.lista_puntos_y = []
        self.punto_actual_lista=0

        #Se concatena el punto inicial
        self.lista_puntos_x.append(x)
        self.lista_puntos_y.append(y)

        if(movimiento=='CIRCULAR'):

            #for de posiciones izquierda-derecha
            for i in range(1,argMovimiento+1):
                self.lista_puntos_x.append(x+(i*paso))
                self.lista_puntos_y.append(y)

            #for de posiciones arriba-abajo
            for i in range(1,argMovimiento+1):
                self.lista_puntos_x.append(x+(argMovimiento*paso))
                self.lista_puntos_y.append(y-(i*paso))

            #for de posiciones derecha-izquierda
            for i in range(argMovimiento-1,-1,-1):
                self.lista_puntos_x.append(x+(i*paso))
                self.lista_puntos_y.append(y-(argMovimiento*paso))

            #for de posiciones abajo-arriba
            for i in range(argMovimiento-1,0,-1):
                self.lista_puntos_x.append(x)
                self.lista_puntos_y.append(y-(i*paso))

        elif(movimiento=='IDAVUELTA-LINEAR'):

            # for de posiciones izquierda-derecha
            for i in range(1, argMovimiento + 1):
                self.lista_puntos_x.append(x + (i * paso))
                self.lista_puntos_y.append(y)

            # for de posiciones derecha-izquierda
            for i in range(argMovimiento - 1, 0, -1):
                self.lista_puntos_x.append(x + (i * paso))
                self.lista_puntos_y.append(y)

        elif(movimiento=='IDAVUELTA-DIAGONAL'):

            # for de posiciones izquierda-derecha
            for i in range(1, argMovimiento + 1):
                self.lista_puntos_x.append(x + (i * paso))
                self.lista_puntos_y.append(y + (i * paso))

            # for de posiciones derecha-izquierda
            for i in range(argMovimiento - 1, 0, -1):
                self.lista_puntos_x.append(x + (i * paso))
                self.lista_puntos_y.append(y + (i * paso))

        elif(movimiento=='ESTATICO'):
            print("ESTATICO: No hay puntos para agregar")
        else:
            print("Movimiento no conocido. El movimiento será estatico por defecto.")

    def participarEnRed(self):
        #Crea un aleatorio y revisa si es menor o igual al porcentaje de participacion
        aleatorio = random.random()
        if(aleatorio<=self.porc_part):
            self.participando = True
        else:
            self.participando = False

    def obtenerRecursos(self):
        recursosAdar = self.porc_part / 2;
        return (self.identificador, self.RAM_GB * recursosAdar, (self.MEMORIA_GB.size) * recursosAdar,
                self.velocidad * recursosAdar)  # (RAM,MEMORIA,VELOCIDAD)

    def mover(self):

        #Se revisa si se llego al final de la lista para reiniciarla
        if (self.punto_actual_lista + 1==len(self.lista_puntos_x)):
            self.punto_actual_lista = 0
        else:
            self.punto_actual_lista = self.punto_actual_lista + 1

        #Se asignan los puntos a donde se moverá el nodo
        self.x_actual=self.lista_puntos_x[self.punto_actual_lista]
        self.y_actual = self.lista_puntos_y[self.punto_actual_lista]

        #Se calcula si el nodo quiere participar en la red
        self.participarEnRed()

        #Se retorna una tupla con el punto a donde se movio el nodo
        return (self.x_actual,self.y_actual)

    def getInfo(self):
        return "{ID="+self.identificador+", MODELO: "+self.modelo+", MOVIMIENTO: "+self.movimiento+", COORDENADAS: ("+str(self.x_actual)+","+str(self.y_actual)+")}"