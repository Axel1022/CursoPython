# Lectura ('r')
with open('archivo.txt', 'r') as file:
    contenido = file.read()
print("Contenido después de lectura:", contenido)

# Escritura ('w')
with open('archivo.txt', 'w') as file:
    file.writelines("Nuevo contenido\n")

# Lectura después de escritura ('w')
with open('archivo.txt', 'r') as file:
    contenido = file.read()
print("Contenido después de escritura:", contenido)

# Adjuntar ('a')
with open('archivo.txt', 'a') as file:
    file.writelines("Contenido adicional\n")

# Lectura después de adjuntar ('a')
with open('archivo.txt', 'r') as file:
    contenido = file.read()
print("Contenido después de adjuntar ('a'):", contenido)

# Lectura y escritura ('r+')
with open('archivo.txt', 'r+') as file:
    contenido = file.read()
    file.writelines("Nuevo contenido\n")
    # Vuelve al principio para leer el contenido completo
    #file.seek(0)
    contenido = file.read()
print("Contenido después de lectura y escritura ('r+'):", contenido)

#Leer linea por linea
with open('archivo.txt', 'r') as file:
    for linea in file:
        print(linea)



