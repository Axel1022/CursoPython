"""
Lectura ('r'): Abre un archivo existente para lectura. Si el archivo no existe, se
producirä un error.
Escritura ('w'): Abre un archivo para escritura. Si el archivo no existe, se crearä. Si
el archivo existe, se truncarä (se eliminarä su contenido).
Adjuntar ('C'): Abre un archivo para agregar contenido a1 final. Si el archivo no existe,
se crearä.
Lectura y escritura ('r+'): Abre un archivo para lectura y escritura.
Binario ('b'): Abre un archivo en modo binario.
"""


#Abre archivo (SOLO LECTURA)
archivo = open("archivo.txt", "r")
#Al colocarle 'r' el archivo se abrira en solo lectura.
#Lee archivo
contenido = archivo.read()
#Imprime archivo
print(contenido)
#Cierra archivo
archivo.close()

##Abre archivo (SOLO ESCRITURA)
archivo = open("archivo.txt", "w")
#Sobre escribe el archivo
archivo.writelines("Este es otra linea que estoy agregando al documento.")
#Imprime archivo
print(contenido)
archivo.close()


