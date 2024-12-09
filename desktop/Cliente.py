import requests as rq

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

        print(response.status_code)



class ClienteModify():

    def getAll(self):
        URL = f"http://127.0.0.1:8000/clientes/"
        response = rq.get(URL)
        return response.json()
    
    def get(self, id: int):
        URL = f"http://127.0.0.1:8000/clientes/{id}/"
        response = rq.get(URL)
        return response.json()

    def delete(self, id: int):
        URL = f"http://127.0.0.1:8000/clientes/{id}/"
        rq.delete(URL)

        

    def update(self, id: int, datos: dict):
        URL = f"http://127.0.0.1:8000/clientes/{id}/"
        response = rq.put(URL, datos)

        print(response.status_code)
        print(URL)



class AdminCliente():

    def addVeterinario(self):
        nombre = input("Ingrese el nombre: \n")
        telefono = input("Ingrese la telefono: \n")
        correo = input("Ingrese la Correo: \n")
        direccion = input("Ingrese los direccion: \n")
        while True:

            tipo = input("Ingrese el estado: [premium, regular]")

            if tipo.lower() in ["premium", "regular"] and tipo:
                break
            else: print("Opcion No valida, Ingrese: [premium, regular]")

        cliente = Cliente(nombre= nombre, telefono=telefono, correo=correo, direccion=direccion, tipo=tipo)
        cliente.save()


    def UpVeterinario(self, id: int):
        nombre = input("Ingrese el nombre: \n")
        telefono = input("Ingrese la telefono: \n")
        correo = input("Ingrese la Correo: \n")
        direccion = input("Ingrese los direccion: \n")
        while True:

            tipo = input("Ingrese el estado: [premium, regular]")

            if tipo.lower() in ["premium", "regular"] and tipo:
                break
            else: print("Opcion No valida, Ingrese: [premium, regular]")

        action = ClienteModify()

        action.update(id, {
            "nombre": nombre,
            "especialidad": telefono,
            "correo": correo,
            "direccion": direccion,
            "tipo": tipo,
        })
        




