from manejadorcama import ManejaCama
from manejamedicamentos import manejador

class Menu:
    __opcion = None

    def __init__(self, op):
        self.__opcion = op

    def menu(self):
        if self.__opcion == 1:
            c = Manejacama()
            c.Carga()
            pos = c.ListaPacienteAlta()
            if pos < 30:
                c = manejador()
                c.Cargamed()
                c.buscamed(pos+1)

        elif self.__opcion == 2:
            c = ManejadorCama()
            c.Carga()
            c.ListaPacienteInt()

        else:
            print("No exite esa opcion")
