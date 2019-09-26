# Primero hay que declarar una variable str con numeros
Numero = "1234"

print(type(Numero))
# Con el type determinamos el tipo de de dato de la variable
Numero = int(Numero)

print(type(Numero))
# Volveremos a preguntar informacion 
Salida = "El numero utilizado es {}"
# La salida va a hacer el texto y lo que esta en
# {} es e numero
print(Salida.format(Numero))
