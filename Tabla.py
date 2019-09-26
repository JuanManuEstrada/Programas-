Numero = input("Dame un numero del 1 al 9: ")
Numero = int(Numero)
# Pedimos la variable del 1 al 9
# Que el valor dado sea en int

for i in range(1,11):

    Salida = "{} x {} = {}"
    # Se van a multiplicar el numero dado en su tabla
    # dando la multiplicacion correcta del 1 al 10
    print(Salida.format(Numero,i,i*Numero))
