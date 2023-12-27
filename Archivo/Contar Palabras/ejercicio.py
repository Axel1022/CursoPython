"""
Escribe un programa que cuente el número de palabras en un archivo de texto llamado "texto.txt". Imprime el resultado al final del archivo.
"""
with open("archivo.txt", "r") as file:
    palabras: int = len(file.read().split())
    print(palabras)


