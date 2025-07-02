pares = 0
impares = 0
total = 0
lista_pares = []
lista_impares = []

while True:
    entrada = input("Ingrese un número o "salir" para terminar ")
    if entrada.lower() == "salir":
        break
        
    try
        numero = int(entrada)
        
        if numero < 0:
            print("Solo se permiten números positivos.")
            
        total += 1
        if numero % 2 == 0:
            pares += 1
            lista_pares.append(numero)
            
        else:
        impares += 1
        lista_impares.append(numero)
    except ValueError:
         print("  Entrada no válida, por favor escriba un número o 'salir'.  ")

print("Total de números ingresados:", total)
print("Total de números ingresados:", total)

