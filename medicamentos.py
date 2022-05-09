class Medicamento:
    __idCama = None
    __idMedicamento = None
    __nombreC = None
    __monodroga = None
    __presentacion = None
    __cantidadA = None
    __precioT = None

    def __init__(self ,idcama ,idmedicamento, nombre, mono, presentacion, cantidad, precio):
        self.__idCama = idcama
        self.__idMedicamento = idmedicamento
        self.__nombreC = nombre
        self.__monodroga = mono
        self.__presentacion = presentacion
        self.__cantidadA = cantidad
        self.__precioT = precio

    def getcama(self):
        return self.__idCama

    def getmedi(self):
        return self.__idMedicamento

    def getn(self):
        return self.__nombreC

    def getm(self):
        return self.__monodroga

    def getp(self):
        return self.__presentacion

    def getc(self):
        return self.__cantidadA

    def getprecio(self):
        return self.__precioT
