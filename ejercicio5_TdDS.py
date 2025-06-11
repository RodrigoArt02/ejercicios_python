#Ejercicios Python
#Tipos de Datos Simples
#Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
#Después debe mostrar por pantalla la paga que le corresponde.

h = int(input("¿Cuantas horas has trabajado? "))
c = int(input("¿Cuanto ganas por hora? "))

paga = (h * c)

print(f"El total de tu paga es:", paga)
