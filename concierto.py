contador_b = 0
cliente = str(input("hay algun cliente?:"))
if cliente == "si":
  contador_b += 1
while cliente == "si":
  nombre = str(input("como se llama el cliente?:"))
  zona = input("Elige la zona para el concierto (1/2/3):")
  if zona == "1":
    print("serian $2000")
    dia = input("Que dia es?:")
    if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves":
      print("Los cupones son validos")
      cupon = input("desea utilizar un cupon?:")
      if cupon == "si":
        tipo_cupon = input("Que cupon desea utilizar?:")
        if tipo_cupon == "platino":
          print("El boleto de", nombre, "cuesta $1500")
        elif tipo_cupon == "oro":
          print("El boleto de", nombre, "cuesta $1700")
        elif tipo_cupon == "plata":
          print("El boleto de", nombre, "cuesta $1800")
      elif cupon == "no":
        print("el boleto de", nombre, "cuesta $2000")
    elif dia == "viernes" or dia == "sabado" or dia == "domingo":
      print("cupon no valido")
      print("el boleto de", nombre, "cuesta $2000")
  if zona == "2":
    print("serian $1000")
    dia = input("Que dia es?:")
    if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves":
      print("Los cupones son validos")
      cupon = input("desea utilizar un cupon?:")
      if cupon == "si":
        tipo_cupon = input("Que cupon desea utilizar?:")
        if tipo_cupon == "platino":
          print("El boleto de", nombre, "cuesta $500")
        elif tipo_cupon == "oro":
          print("El boleto de", nombre, "cuesta $700")
        elif tipo_cupon == "plata":
          print("El boleto de", nombre, "cuesta $800")
      elif cupon == "no":
        print("el boleto de", nombre, "cuesta 1000")
    elif dia == "viernes" or dia == "sabado" or dia == "domingo":
      print("cupon no valido")
      print("el boleto de", nombre, "cuesta $1000")
  if zona == "3":
    print("serian $700")
    dia = input("Que dia es?:")
    if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves":
      print("Los cupones son validos")
      cupon = input("desea utilizar un cupon?:")
      if cupon == "si":
        tipo_cupon = input("Que cupon desea utilizar?:")
        if tipo_cupon == "platino":
          print("El boleto de", nombre, "cuesta $200")
        elif tipo_cupon == "oro":
          print("El boleto de", nombre, "cuesta $400")
        elif tipo_cupon == "plata":
          print("El boleto de", nombre, "cuesta $500")
      elif cupon == "no":
        print("el boleto de", nombre, "cuesta $700")
    elif dia == "viernes" or dia == "sabado" or dia == "domingo":
      print("cupon no valido")
      print("el boleto de", nombre, "cuesta $700")
  otro = input("Hay algun otro cliente?:")
  if otro == "si":
    contador_b += 1
  elif otro == "no":
    break
print("En total se vendieron", contador_b, "boletos")
