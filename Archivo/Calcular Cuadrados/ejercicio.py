"""
Escribe un programa que tome un archivo de texto llamado "numeros.txt" que contiene números enteros en cada línea y escriba en un nuevo archivo llamado "cuadrados.txt" el cuadrado de cada número.
"""
with open("numeros.txt", "r") as file:
    #para que no reemplace los datos debo usar a+
    with open("cuadrados.txt", "w") as numeros:
        for num in file:
            num = int(num)
            numCuadrado = num * num
            numeros.write(f"{numCuadrado}\n")

