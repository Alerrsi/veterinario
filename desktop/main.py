from Cliente import ClienteModify, AdminCliente
from Medicamento import MedicamentoModify, AdminMedicamento
import os


# clases a USAR

adminCliente = AdminCliente()
modifyCliente = ClienteModify()

modifyMedicamento  = MedicamentoModify()
adminMedicamento = AdminMedicamento()

def cleanDisplay():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")


def pedirID():
    while True:
        try:
            id = int(input("Ingrese el Id"))
            break
        except ValueError as e:
            print("ingrese un numero")

    return id 



def menu() :
    print("___Menu de Opciones___")
    print("1) Menu de Medicamentos")
    print("2) Menu de Clientes")

def menuOpcion(tipo: str):
    print(f"__MENU {tipo}__")
    print(f"1) ver un {tipo}[s]")
    print(f"2) ver todos{tipo}[s]")
    print(f"3) agregar un {tipo}[s]")
    print(f"4) eliminar un {tipo}[s]")
    print(f"5) editar un {tipo}[s]")
    print(f"6) salir")


def opcionAPICliente():

    while True:
        try: 
            menuOpcion("Cliente")
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                id = pedirID()
                cleanDisplay()
                print(modifyCliente.get(id))
                input("continuar: [ENTER]")
            elif opcion == 2:
                print(modifyCliente.getAll())
                input("continuar: [ENTER]")
            elif opcion == 3:
                adminCliente.addCliente()
                input("continuar: [ENTER]")
            elif opcion == 4:
                print(modifyCliente.getAll())
                id = pedirID()
                modifyCliente.delete(id)
                input("continuar: [ENTER]")
            elif opcion == 5:
                print(modifyCliente.getAll())
                id = pedirID()
                adminCliente.upCliente(id)
                input("continuar: [ENTER]")
            elif opcion == 6:
                cleanDisplay()
                break
            else: 
                print("opcion no valida")
            
            cleanDisplay()
        except ValueError as e:
            print("opcion no valida, ingrese: [1, 2,3,4,5,6] ")



def opcionAPIMedicamento():

    while True:
        try: 
            menuOpcion("Medicamento")
            opcion = int(input("Ingrese la opcion: "))
            if opcion == 1:
                id = pedirID()
                cleanDisplay()
                print(modifyMedicamento.get(id))
                input("continuar: [ENTER]")
            elif opcion == 2:
                print(modifyMedicamento.getAll())
                input("continuar: [ENTER]")
            elif opcion == 3:
                adminMedicamento.addMedicamento()
                input("continuar: [ENTER]")
            elif opcion == 4:
                print(modifyMedicamento.getAll())
                id = pedirID()
                modifyMedicamento.delete(id)
                input("continuar: [ENTER]")
            elif opcion == 5:
                print(modifyMedicamento.getAll())
                id = pedirID()
                adminMedicamento.UpMedicamento(id)
                input("continuar: [ENTER]")
            elif opcion == 6:
                cleanDisplay()
                break
            else: 
                print("opcion no valida, ingrese: [1, 2,3,4,5,6] ")
            
            cleanDisplay()
        except ValueError as e:
            print("debe ingresar un numero: [1, 2,3,4,5,6]")

    
 


    


def opciones():
    while True:
        try: 
            opcion = int(input("Ingrese la opcion: "))
            if opcion in [1, 2]:
                cleanDisplay()
                break
            else: 
                os.system("clear")
                print("opcion no valida")
            
        except ValueError as e:
            print("debe ingresar un numero: [1, 2]")

    return opcion


def algo(opcion: int): 
    if opcion == 1:
        
        opcionAPIMedicamento()

    elif opcion == 2:
        
        opcionAPICliente()



def main():

    
    while True:
        menu()
        opcion = opciones()
        algo(opcion)
        







main()






