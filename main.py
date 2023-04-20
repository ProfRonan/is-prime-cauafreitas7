cont = 0
número =int(input("Digite um número: "))
if número < 0 or número == 0:
   print("Número Inválido")
else:
  for primos in range(1, número+1):
     if (número % primos) == 0:
        cont += 1
  if cont > 2 or número == 1:
     print("Não é primo")
  else:
    print("É primo")