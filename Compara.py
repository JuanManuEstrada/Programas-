numero1 = input("Numero 1:")
numero2 = input("Numero 2:")
salida = "Numero proporcionados: {} y {}. {}."
# Creamos y preguntamos las variables que se ocupan con input
if (numero1==numero2):
    # Si los numeros que nos dan son iguales entrara aqui
    print(salida.format(numero1, numero2, "Los numeros son iguales"))
else:
    # Si los numeros no son iguales entrara aqui
    # Sera un if dentro de otro if
    if numero1 > numero2:
        # Dice que el primer numero es mayor
        print(salida.format(numero1, numero2,"El mayor es el primero"))

    else:
        # Si el primero es menor, entrara aqui
        print(salida.format(numero1, numero2,"El mayor es el segundo"))
