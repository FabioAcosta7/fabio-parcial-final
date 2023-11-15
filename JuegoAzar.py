import random
contador = 0
print("Adivina el numero del 1 al 10. Solo tienes tres intentos")
num = random.randint(1,10)
intento = int(input("Ingresa un numero:"))
contador += 1
if intento == num:
  print("Adivinaste en", contador, "intentos")
  contador += 4
elif intento != num:
  print("No adivinaste")
while contador < 3:
  contador += 1
  s_intento = int(input("Ingresa un numero:"))
  if s_intento == num:
    print("adivinaste en", contador, "intentos")
    break
  elif s_intento != num:
    print("no adivinaste")
if s_intento != num:
  print("Has perdido el juego")
