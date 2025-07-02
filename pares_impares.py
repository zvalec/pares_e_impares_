pares = 0
impares = 0

while True:
    entrada = input("Ingrese un número: ")
    if entrada.lower() == "salir":
        break
        
    try
        numero = int(entrada)
        if numero % 2 == 0:
        pares += 1
        
        else:
        impares += 1
except ValueError:
         print("  Entrada no válida, por favor escriba un número o 'salir'.  ")

print("La cantidad de números pares es: ", pares, "y la cantidad de números impares es: ", impares)

