#Algoritmo que le solicita al usuario que ingrese un valor A y otro valor B, e intercambia los valores de dichas variables y los muestra por consola.

print("Ingrese un número")
unNumero = float(input())

print("Ingrese otro número")
otroNumero = float(input())

print(unNumero)
print(otroNumero,'\n')

auxiliar = otroNumero # Almacena temporalmente el valor de uno de los números ingreados.

otroNumero = unNumero
unNumero = auxiliar

# Luego muestra por consola los valores intercambiados.
print(unNumero)
print(otroNumero)
