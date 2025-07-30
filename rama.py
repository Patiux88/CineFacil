def cancelar_reserva(nombre, pelicula):
    if reservas:
        encontrado=False
        for i, r in enumerate(list(reservas)):
            if nombre == r["nombre"] and pelicula == r["pelicula"]:
                reserva_eliminar=i
                encontrado=True
                break
        if encontrado:
            reservas.pop(indice)
            print("Reserva eliminada con éxito")
        else:
            print("No se encontró reserva con ese nombre y película")
def cambiar_precio_pelicula(pelicula, precio):
    if pelicula in peliculas:
        peliculas[pelicula]=precio
    else:
        print("No se encotró esa película en la cartelera")

