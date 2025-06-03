#ESPECIFICA
def cargar_nombres_participantes(array_nombres:list) -> None:
    """Se encarga de ingresar y guardar los nombres de los participanttes en un array

    Args:
        array_nombres (list): El array con los nombres de los participantes (a cargar)
    """
    for i in range(len(array_nombres)):
        #Pido el dato
        nombre = input(f"Ingrese el nombre del participante {i+1}: ")
        while len(nombre) < 3:
            print(f"ERROR. Nombre no valido.")
            nombre = input(f"Reingrese el nombre del participante {i+1}: ")
        #Lo guardo en el array
        array_nombres[i] = nombre
        
       
#ESPECIFICA 
def cargar_puntaje_jurado(matriz_puntajes:list) -> None:
    """Se encarga de ingresar y guardar los puntajes de los participanttes en un array

    Args:
        matriz_puntajes (list): La matriz donde se guardan los puntajes de cada participante que otorgo cada 
        jurado (a cargar)
    """
    for fil in range(len(matriz_puntajes)):
        for col in range(len(matriz_puntajes[0])):
            #Pedir el dato
            puntaje = int(input(f"Ingrese el puntaje del participante {fil+1} para el jurado {col+1}: "))
            #VALIDARLA (1-10)
            while puntaje < 1 or puntaje > 10:
                print(f"ERROR. Puntaje no valido.")
                puntaje = int(input(f"Reingrese el puntaje del participante {fil+1} para el jurado {col+1}: "))
            #Lo guardo en la matriz
            matriz_puntajes[fil][col] = puntaje

def ingresar_nombre(mensaje:str) -> str:
    """Se encarga de ingresar un nombre por consola para su posterior uso

    Args:
        mensaje (str): El mensaje que se le pide al usuario; que ingrese el nombre a buscar

    Returns:
        str: El nombre ingresado por el usuario
    """
    nombre = input(mensaje)

    return nombre

def transformar_caracter_a_ascii(mensaje:str) -> None:
    """Se encarga de transformar, si es posible, un caracter a codigo ASCIII

    Args:
        mensaje (str): El mensaje que se le pide al usuario; que ingrese una opcion entre 1 y 11

    Returns:
        _type_: Puede retornar como una cadena de texto si la opcion ingresada es igual a 10 o igual a 11 o
        si no pertenece a ninguna de las opciones que ofrece el menu
        O, puede retornar la opcion ingresada (opcion valida entre 1 y 9) y lo transforma a codigo ASCII
    """
    opcion = input(mensaje)
    if opcion != '1' and opcion != '2' and opcion != '3' and opcion != '4' and opcion != '5' and opcion != '6' and opcion != '7' and opcion != '8' and opcion != '9':
        return opcion
    else:
        caracter = ord(opcion)
        return caracter
    