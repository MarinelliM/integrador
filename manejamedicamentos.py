import csv
from medicamentos import medicamento

class manejador:
  __maneja = None
  
  def cargamed(self):
    archivo = open("medicamento.csv")
    reader = csv.reader(archivo, delimiter ';')
    medi = []
    bandera = True
    for fila in reader:
      if bandera:
        bandera = not bandera
      else:
        idcama = int(fila[0])
        idmed = int(fila[1])
        nombrec = str(fila[2])
        monod = str(fila[3])
        presentacion = str(fila[4])
        cantidada = int(fila[5])
        preciot = int(fila[6])
        m = medicamento(idcama, idmed, nombrec, monod, presentacion, cantidada, preciot)
        medi.append(m)
    self.__maneja = medi     
   
  def buscamed(self, idcama):
    cant = 0
     print("Medicamento/Monodroga        Presentacion          Cantidad               Precio")
    for i in range(len(self.__medi))
      if self.__maneja[i].getidcama() = idcama
        cant += self.__medi[i].getcant()
                j = i
                print("{}/{}           {}                {}                  {}".format(self.__Medicamento[i].getNomC(), self.__Medicamento[i].getMono(), self.__Medicamento[i].getPres(), self.__Medicamento[i].getCantApl(), self.__Medicamento[i].getPrecT()*self.__Medicamento[i].getCantApl()))
     print("Total Adeudado: {} ".format(cant * self.__medi[j].getpreciot()))
      
        
