import requests as rq


try: 
    id = int(input("ingrese Id del Producto: "))



    response = rq.get(f"https://fakestoreapi.com/products/{id}")




    if response.status_code == 200:
        for data in response.json().items():
            print(f"{data[0]}: {data[1]}")


except ValueError as e:
    print("Ingrese Ids numericos")

