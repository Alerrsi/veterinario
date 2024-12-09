import requests as rq
from email_validator import validate_email, EmailNotValidError

class Cliente():
    def __init__(self, nombre, telefono, correo, direccion, tipo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.tipo = tipo


    def save(self):
        URL = url = "http://127.0.0.1:8000/clientes/"
        data = {
            "nombre" : self.nombre,
            "telefono" : self.telefono,
            "correo" : self.correo,
            "direccion" : self.direccion,
            "tipo" : self.tipo,
        }

        response = rq.post(URL, data=  data)

        print("Cliente ingresado")



class ClienteModify():


    def verificarID(self, id: int):
        URL = f"http://127.0.0.1:8000/clientes/{id}/"
        response = rq.get(URL)
        if response.status_code == 200:
            return True
        
        return False

    def getAll(self):
        URL = f"http://127.0.0.1:8000/clientes/"
        response = rq.get(URL)
        if not  response.json() == []:
            return response.json()
        else: 
            return "No hay Existensias de Clientes"

    
    def get(self, id: int):
        URL = f"http://127.0.0.1:8000/clientes/{id}/"
        response = rq.get(URL)
        if response.status_code == 200:
            return response.json()
        else: 
            return "Id no Existente"
    

    def delete(self, id: int):
        URL = f"http://127.0.0.1:8000/clientes/{id}/"
        response = rq.delete(URL)
        if response.status_code == 404:
            print("Id no Existente")
        else: 
            print("cliente Eliminado Correctamente")

        

    def update(self, id: int, datos: dict):
        URL = f"http://127.0.0.1:8000/clientes/{id}/"
        response = rq.put(URL, datos)

        print(response.status_code)
        



class AdminCliente():

    def addCliente(self):
        nombre = input("Ingrese el nombre: \n")
        while True: 
            telefono = input("Ingrese la telefono: \n")
            if self.clean_telefono(telefono):
                break
            else: 
                print("numero no valido, debe ser: [9]87654321")
        while True:
            correo = input("Ingrese el correo: \n")

            if self.clean_correo(correo):
                break
        direccion = input("Ingrese los direccion: \n")
        while True:

            tipo = input("Ingrese el estado: [premium, regular]")

            if tipo.lower() in ["premium", "regular"] and tipo:
                break
            else: print("Opcion No valida, Ingrese: [premium, regular]")

        cliente = Cliente(nombre= nombre, telefono=telefono, correo=correo, direccion=direccion, tipo=tipo)
        cliente.save()


    def upCliente(self, id: int):
        modify = ClienteModify()
        if not modify.verificarID(id) :
            print("id no valido")
        else:
            nombre = input("Ingrese el nombre: \n")
            while True: 
                telefono = input("Ingrese la telefono: \n")
                if self.clean_telefono(telefono):
                    break
                else: 
                    print("numero no valido, debe ser: [9]87654321")
            while True:
                correo = input("Ingrese el correo: \n")

                if self.clean_correo(correo):
                    break
                else: 
                    print("correo no valido")

            direccion = input("Ingrese los direccion: \n")
            while True:
                tipo = input("Ingrese el estado: [premium, regular]")
                if self.clean_tipo(tipo):
                    break
                else: 
                    print("tipo no valido, debe ser : ['regular', 'premium']")
                

            action = ClienteModify()

            action.update(id, {
                "nombre": nombre,
                "telefono": telefono,
                "correo": correo,
                "direccion": direccion,
                "tipo": tipo,
            })

            print("Cliente actualizado")


    def clean_correo(self, correo: str) -> bool:
            try: 
                res = validate_email(correo)
            except EmailNotValidError as e:
                print(e)
                return False
            else: 
                return True
            

    def clean_telefono(self, telefono: str) -> bool:

        if len(telefono) == 9 and telefono[0] == "9" and telefono.isnumeric():
            return True

        return False
    
    def clean_tipo(self, tipo: str) -> bool:

        if tipo.lower() in ["premium", "regular"] and tipo:
            return True
        else: 
            return False
        




