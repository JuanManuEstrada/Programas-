numero = int(input("Dame un numero entero: "))
# Capturamos el numero y luego lo convertimos a int

esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
# Almacenamos los valores booleanos, si el residual
# es cero, entonces quiere decir que el numero es multiplo

if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto")
else:
    print("Incorrecto")
#El and se resolvera veradero si todas las condiciones establecidas
# son correctas, cuando se usa el or, sera verdadero
# si aunque sea una condicion es correcta
# Los parentesis diran que las primeras dos condiciones van a ser juntas
# y la tercera es independiente
