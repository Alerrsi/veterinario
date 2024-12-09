import requests as rq

class Medicamento():
    def __init__(self, nombre, tipo, dosis, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.dosis = dosis
        self.cantidad = cantidad
        


    def save(self):
        URL = url = "http://127.0.0.1:8000/medicamentos/"
        data = {
            "nombre" : self.nombre,
            "tipo" : self.tipo,
            "dosis" : self.dosis,
            "cantidad" : self.cantidad,
        }

        response = rq.post(URL, data=  data)

        print("Medicamento ingresado")



class MedicamentoModify():

    def verificarID(self, id: int):
        URL = f"http://127.0.0.1:8000/medicamentos/{id}/"
        response = rq.get(URL)
        if response.status_code == 200:
            return True
        
        return False

    def getAll(self):
        URL = f"http://127.0.0.1:8000/medicamentos/"
        response = rq.get(URL)
        if not  response.json() == []:
            return response.json()
        else: 
            return "No hay Existensias de Medicamentos"
    
    def get(self, id: int):
        URL = f"http://127.0.0.1:8000/medicamentos/{id}/"
        response = rq.get(URL)
        return response.json()

    def delete(self, id: int):
        URL = f"http://127.0.0.1:8000/medicamentos/{id}/"
        response = rq.delete(URL)
        if response.status_code == 404:
            print("Id no Existente")
        else: 
            print("Medicamento Eliminado Correctamente")
        

        

    def update(self, id: int, datos: dict):
        URL = f"http://127.0.0.1:8000/medicamentos/{id}/"
        response = rq.put(URL, datos)

        print(response.status_code)
        print(URL)



class AdminMedicamento():

    def addMedicamento(self):
        nombre = input("Ingrese el nombre: \n")
        tipo = input("Ingrese el tipo: \n")
        dosis = input("Ingrese la dosis: \n")
        while True: 
                try: 
                    cantidad = int(input("Ingrese la cantidad: \n"))
                    if self.clean_cantidad(cantidad):
                        break
                    else: 
                        print("la cantidad debe ser mayor a 0")
                except ValueError as e:
                    print("Debe ingresar un entero")
        medicamento = Medicamento(nombre= nombre, tipo=tipo,dosis=dosis, cantidad=cantidad)
        medicamento.save()



    def UpMedicamento(self, id: int):
        modify = MedicamentoModify()
        if not modify.verificarID(id) :
            print("id no valido")
        else:
            nombre = input("Ingrese el nombre: \n")
            tipo = input("Ingrese el tipo: \n")
            dosis = input("Ingrese la dosis: \n")
            while True: 
                try: 
                    cantidad = int(input("Ingrese la cantidad: \n"))
                    if self.clean_cantidad(cantidad):
                        break
                    else: 
                        print("la cantidad debe ser mayor a 0")
                except ValueError as e:
                    print("Debe ingresar un entero")

            action = MedicamentoModify()

            action.update(id, {
                "nombre": nombre,
                "tipo": tipo,
                "dosis": dosis,
                "cantidad": cantidad,
                
            })

    def clean_cantidad(self, cantidad: int) -> bool:

        if cantidad > 0:
            return True
        
        return False
        




