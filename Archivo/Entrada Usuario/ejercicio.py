"""
Crea un programa que solicite al usuario ingresar líneas de texto y las escriba en un archivo llamado "usuario.txt". Detén la entrada de texto cuando el usuario escriba "fin".
"""

while True:
    dato: str = input(">>>").upper()
    if dato == "FIN":
        break
    #Para que no sobreescriba debo colocar a+
    with open("usuario.txt", "a+") as datoUser:
        datoUser.writelines(f"{dato}\n")



