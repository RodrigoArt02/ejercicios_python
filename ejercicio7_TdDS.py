#Ejercicios Python
#Tipos de Datos Simples
#Ejercicio 7
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros)
#Calcule el índice de masa corporal y lo almacene en una variable 
#Muestre por pantalla la frase Tu índice de masa corporal es <imc>
#Donde <imc> es el índice de masa corporal calculado redondeado con dos decimales

peso = float(input("Ingresa tu peso (En KG): "))
altura = float(input("Ingresa tu altura (En M): "))

imc = peso / (altura ** 2)
imc_redondeado = round(imc, 2)

print(f"Tu índice de masa corporal es: ", imc_redondeado)