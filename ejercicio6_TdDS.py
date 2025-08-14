#Ejercicios Python
#Tipos de Datos Simples
#Ejercicio 6
#Escribir un programa que lea un entero positivo, n, introducido por el usuario. 
#Después muestre en pantalla la suma de todos los números enteros de 1 hasta n.

n = int(input("Introduce un número entero positivo: "))

num = n * (n + 1)
suma = num / 2

print(f"La suma de 1 hasta", n, "es: ", suma)