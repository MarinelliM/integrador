from datetime import datetime
class Cama:
    __idCama = None
    __habitacion = ""
    __estado = None
    __nya = ""
    __diagnostico = None
    __fechai = ""
    __fechaa = ""

    def __init__(self, hab = None, est: bool = False, NyA = None, diag = None, fI = None, fA = None):
        self.__habitacion = hab
        self.__estado = est
        self.__nya = NyA
        self.__diagnostico = diag
        self.__fechai = fI
        self.__fechaa = fA

    def getHabitacion(self):
        return self.__habitacion

    def getEstado(self):
        return self.__estado

    def getNyA(self):
        return self.__nya

    def getDiagnostico(self):
        return self.__diagnostico

    def getI(self):
        return self.__fechai

    def ModificarFechA(self):
        self.__fechaa = datetime.today()

    def getA(self):
        return self.__fechaa
