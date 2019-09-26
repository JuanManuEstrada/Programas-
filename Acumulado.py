acumulado = int(0)
numero = str("")
# Se van a declarar las variables de acumulado y numero

while True:
    # Cuando colocamos True como condicion de While, se van a formar
    # un ciclo infinito, este no se rompera hasta que tengamos el termino
    # que deseamos
    numero = input("Dame un numero entero: ")
    if numero=="":

        print("Vacio. Salida del programa.")
        break
    # Si el numero es vacio, lo va a reportar y saldra
    else:

        acumulado += int(numero)
        salida = "Monto acumulado: {}"
        print(salida.format(acumulado))
        #Si se da el valor que queremos se realiza el calculo
        # por tanto sera correcto y dara  el resultado bien
