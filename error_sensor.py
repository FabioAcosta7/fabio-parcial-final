contador = 0
contador_errores = 0
lecturas = int(input("Cuantas lecturas tienes:"))
while contador < lecturas:
  contador += 1
  temperatura = int(input("Inserta la temperatura:"))
  if temperatura < 5:
    contador_errores += 1
  elif temperatura > 40:
    contador_errores += 1
  porcentaje = (contador_errores/contador)*100

print("El sensor se equivoco", contador_errores, "veces")
print("El porcentaje de error del sensor es de", porcentaje, "%")
