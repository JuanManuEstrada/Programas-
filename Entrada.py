Entrada = input()
print(type(Entrada))
# Agregamos la variable type para entrada
esEntero = (Entrada.isdigit() and Entrada.flind(".")==-1)
if (esEntero):
# si es correcto el dato estara bien 
    print("Dato entero. ¡Muy bien!")
else:
# pero si es incorrecto estara mal
    print("Dato no es entero. Intenta nuevamente")
