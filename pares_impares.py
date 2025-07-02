pares = 0
impares = 0

while True:
    entrada = input("Ingrese un número: ")
    if entrada.lower() == "salir":
        break

    numero = int(entrada)
    if numero % 2 == 0:
        pares += 1
        
    else:
        impares += 1


print("La cantidad de números pares es:", pares, "y la cantidad de números impares es:", impares)

