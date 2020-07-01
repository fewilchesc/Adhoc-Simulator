class Distribuido:
    def __init__(self):
        self.nombres_participantes = []
        self.RAM_GB = []
        self.MEMORIA_GB = []
        self.VELOCIDAD = []

    def getRAM_GB(self):
        RAM_GB = 0
        for i in range(len(self.RAM_GB)):
            RAM_GB = RAM_GB + self.RAM_GB[i]

        return RAM_GB

    def getMEMORIA_GB(self):
        MEMORIA_GB = 0
        for i in range(len(self.MEMORIA_GB)):
            MEMORIA_GB = MEMORIA_GB + self.MEMORIA_GB[i]

        return MEMORIA_GB

    def getVELOCIDAD(self):
        VELOCIDAD = 0
        for i in range(len(self.VELOCIDAD)):
            VELOCIDAD = VELOCIDAD + self.VELOCIDAD[i]

        return VELOCIDAD

    def agregarRecursos(self,identificador,RAM_GB,MEMORIA_GB,VELOCIDAD):
        self.nombres_participantes.append(identificador)
        self.RAM_GB.append(RAM_GB)
        self.MEMORIA_GB.append(MEMORIA_GB)
        self.VELOCIDAD.append(VELOCIDAD)

