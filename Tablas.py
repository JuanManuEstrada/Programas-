for i in range(1,11):
    encabezado = "Tabla del {}"
    print(encabezado.format(i))
    # Pedimos el dato del encabezado que sea un numero
    # del 1 al 10

    print()
    # Con el print en blanco saltamos de linea

    for j in range(1,11):
        # El i tiene el numero que se multiplicara de la tabla
        # La j sera el elemento de la tabla
        salida = "{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        # Si es correcto los numeros dados en la tabla
        # el codigo se ejecutara sin problema
        print()
