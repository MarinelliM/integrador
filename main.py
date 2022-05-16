from Menu import Menu
if __name__ == '__main__':
    print("1:Listar datos del paciente de alta")
    print("2:Listar datos de pacientes internados")
    m = Menu(int(input("Ingrese una opcion:")))
    m.menu()
