#Creamos 1 diccionarioo y una lista
#El primero va a contener peliculas con sus respectivos precios
#La segunda va a tener la reserva hecha por el usuario

reservas=[]
# Diccionario original con películas y sus precios
peliculas = {
    "Inception": 50,
    "Titanic": 40,
    "Avatar": 60,
    "The Matrix": 45,
    "Interstellar": 55,
    "Avengers": 50,
    "Coco": 30,
    "Toy Story": 35,
    "Joker": 40,
    "The Godfather": 45
}

funcion = {
    "matutina": ["Inception", "Coco", "Toy Story"],
    "vespertina": ["Avatar", "Interstellar", "Titanic"],
    "nocturna": ["The Matrix", "Avengers", "Joker", "The Godfather"]
}

# Si se desea ver también el precio de cada película en cada función
funcion_con_precios = {
    clave: [(pelicula, peliculas[pelicula]) for pelicula in lista if pelicula in peliculas]
    for clave, lista in funcion.items()
}

def mostrar_funciones():
    print("Funciones con películas:")
    for f, pelis in funcion_con_precios.items():
        print(f"{f}: {pelis}")


def agregar_reserva(nombre, pelicula, cantidad):
    encontrado=False
    if any(r["nombre"] == nombre and r["pelicula"] == pelicula for r in reservas):
        encontrado=True
    if not encontrado:
        precio = next((p for m, p in peliculas.items() if pelicula in m), 0)
        reservas.append({
            "nombre": nombre,
            "pelicula": pelicula,
            "cantidad": cantidad,
            "total": cantidad*precio
        })
    else:
            print("Ya ha realizado una reserva con esta película")
def mostrar_reservas(reservas):
     if reservas:
          print("Reservas: ")
          for r in reservas:
               for i, (clave, valor)in enumerate(r.items()):
                    print(f"{clave}: {valor}")
     else:
          print("No existen reservas")

#Uso de las funciones
mostrar_funciones()
agregar_reserva("Juan", "Titanic", 2)
agregar_reserva("María", "Inception", 1)
agregar_reserva("Luis", "Coco", 3)
agregar_reserva("Ana", "Avatar", 1)
agregar_reserva("Juan", "Titanic", 1)
mostrar_reservas(reservas)
