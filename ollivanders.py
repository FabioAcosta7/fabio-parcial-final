acumulador_varitas = 0
contador_clientes_si = 0
contador_clientes_no = 0
contador_clientes_totales = 0
contador_varita_sa = 0
contador_varita_e = 0
contador_varita_se = 0
contador_varita_a = 0
cliente = input("entro un cliente?")
if cliente == "si":
  contador_clientes_totales += 1
while cliente == "si":
  cliente_c = input("compro varita? (si/no)")
  if cliente_c == "si":
      contador_clientes_si += 1
      varita = input("que varita compro? elige 1, 2, 3 o 4:")
      if varita == "1":
        contador_varita_sa += 1
        print("Compro varita de sauco")
      elif varita == "2":
        contador_varita_e += 1
        print("Compro varita de espino")
      elif varita == "3":
        contador_varita_se += 1
        print("Compro varita de Sauce")
      elif varita == "4":
        contador_varita_a += 1
        print("Compro varita de acebo")
  elif cliente_c == "no":
    contador_clientes_no += 1
    print("El cliente no compro nada")
  cliente_o = input("entro otro cliente?")
  if cliente_o == "no":
    break
  elif cliente_o == "si":
    contador_clientes_totales += 1
  
print("clientes totales:", contador_clientes_totales)
print("clientes que compraron:", contador_clientes_si)
print("clientes que no compraron:", contador_clientes_no)
print("se vendieron", contador_varita_sa, "varitas de sauco,", contador_varita_e, "varitas de espino,", contador_varita_se, "varitas de sauce y", contador_varita_a, "varitas de acebo")
