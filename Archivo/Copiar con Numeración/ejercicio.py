"""
Crea un programa que lea el contenido de un archivo de texto llamado "entrada.txt" y escriba cada línea en un nuevo archivo llamado "salida.txt". Asegúrate de agregar un número de línea al principio de cada línea en "salida.txt".

"""
with open("Entrada.txt", "r") as file:
    for i,linea in enumerate(file):
        with open(f"refran{i+1}.txt", "w") as file:
            file.write(linea)
            if i >+10:
              break

