from Inputs import *

#GENERAL
def crear_matriz(cantidad_filas:int,cantidad_columnas:int,valor_inicial:any) -> list:
    """Se encarga de crear la matriz 

    Args:
        cantidad_filas (int): Crea la matriz segun la cantidad de filas que tiene como parametro
        cantidad_columnas (int): Crea la matriz segun la cantidad de columnas que tiene como parametro
        valor_inicial (any): El valor inicial puede ser cualquiera (por ejemplo, "matriz_puntajes" inicia en 0 )

    Returns:
        list: La matriz creada
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
        
    return matriz

#GENERAL
def crear_array(cantidad_elementos:int,valor_inicial:any) -> list:
    """Se encraga de crear un array

    Args:
        cantidad_elementos (int): La cantidad de elementos que, como parametro, voy a guardar en mi array
        valor_inicial (any): El valor inicial puede ser cualquiera

    Returns:
        list: El array creado
    """
    array = [valor_inicial] * cantidad_elementos
    return array 

#ESPECIFICA
def mostrar_participante(array_nombres:list,matriz_puntajes:list,indice_participante:int) -> None:
    """Se encraga de mostrar al participante

    Args:
        array_nombres (list): El array creado anteriormente (contiene los nombres de los participantes)
        matriz_puntajes (list): La matriz creada anteriormente (contiene los puntajes de cada participante)
        indice_participante (int): VALIDACION -> Como el programa puede generar un indice fuera de rango, 
        hay que validar y evitar que los arrays/matrices esten vacios y sean realmente de tipo list (se usa 
        el indice de los participantes del "array_nombres")

    Returns:
        _type_: Si los datos de los participantes se cargaron correctamente (haber ingresado las opciones 1 y 
        2 anteriormente)
    """
    if indice_participante >= len(array_nombres) or indice_participante < 0:
        retorno = False
    else:
        retorno = True
        print(f"NOMBRE PARTICIPANTE: {array_nombres[indice_participante]}")
        print(f"PUNTAJE JURADO 1: {matriz_puntajes[indice_participante][0]}")
        print(f"PUNTAJE JURADO 2: {matriz_puntajes[indice_participante][1]}")
        print(f"PUNTAJE JURADO 3: {matriz_puntajes[indice_participante][2]}")
        suma_puntajes = sumar_fila(matriz_puntajes,indice_participante)
        cantidad_jurados = len(matriz_puntajes[0])
        promedio_puntajes = calcular_promedio_puntajes(suma_puntajes,cantidad_jurados)
        print(f"PUNTAJE PROMEDIO: {round(promedio_puntajes,2)}/10")


    return retorno

#ESPECIFICA
def mostrar_participantes(array_nombres:list,matriz_puntajes:list) -> None:
    """Se encraga de mostrar a todos los participantes

    Args:
        array_nombres (list): Muestra los nombres que se encuentran en el array por consola
        matriz_puntajes (list): Muestra los puntajes que se encuentran en la matriz por consola
    """
    for i in range(len(array_nombres)):
        mostrar_participante(array_nombres,matriz_puntajes,i)
        print("")


def buscar_nombre_participante(array_nombres:list,matriz_puntajes:list) -> None:
    """Se encarga de buscar a un participante mediante su nombre

    Args:
        array_nombres (list): Usa el array con los nombres de los participantes para buscar y mostrar (si es 
        que existe) al participante que ingrese el usuario
        matriz_puntajes (list): Usa la matriz con los puntajes que obtuvo el participante (si es que existe) 
        que quiere buscar el usuario para mostrarlo
    """
    bandera = False
    nombre_ingresado = ingresar_nombre("Ingrese el nombre del participante que quiere buscar: ")
    for i in range(len(array_nombres)):
        if nombre_ingresado == array_nombres[i]:
            bandera = True
            mostrar_participante(array_nombres,matriz_puntajes,i)
    if bandera == False:
        print(f"No se encontro al participante con el nombre ingresado.")


def calcular_promedio_puntajes(acumulador:float | int, contador:int) -> int | float:
    """Se encarga de calcular el promedio de puntajes que obtuvo un participante

    Args:
        acumulador (float | int): Almacena la suma ya sea de las filas o de las columnas para realizar la 
        operacion
        contador (int): Almacena la cantidad ya sea de las filas o de las columnas para realizar la 
        operacion

    Returns:
        int | float: El resultado de la operacion
    """
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = None
        
    return promedio


def sumar_columna(matriz_numerica:list,indice_columna:int) -> int | float:
    """Se encarga de sumar las columnas de una matriz

    Args:
        matriz_numerica (list): La matriz usada para la operacion
        indice_columna (int): El indice que corresponde a cada

    Returns:
        int | float: El rsultado de la suma
    """
    suma_columna = 0
    
    for fil in range(len(matriz_numerica)):
        if type(matriz_numerica[fil][indice_columna]) == int or type(matriz_numerica[fil][indice_columna]) == float :
            suma_columna += matriz_numerica[fil][indice_columna]
    
    return suma_columna

#GENERAL
def calcular_promedio(acumulador:float | int, contador:int) -> float | None:
    """Se encarga de calcular el promedio de puntajes que obtuvo un participante

    Args:
        acumulador (float | int): Almacena la suma ya sea de las filas o de las columnas para realizar la 
        operacion
        contador (int): Almacena la cantidad ya sea de las filas o de las columnas para realizar la 
        operacion

    Returns:
        float | None: El resultado de la operacion
    """
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = None
        
    return promedio


#GENERAL
def sumar_fila(matriz_numerica:list,indice_fila:int) -> int | float:
    """Se encarga de sumar las filas de una matriz

    Args:
        matriz_numerica (list): La matriz usada para la operacion
        indice_fila (int): El indice que corresponde a cada fila

    Returns:
        int | float: El resultado de la suma
    """
    suma_fila = 0
    
    for col in range(len(matriz_numerica[0])):
        if type(matriz_numerica[indice_fila][col]) == int or type(matriz_numerica[indice_fila][col]) == float :
            suma_fila += matriz_numerica[indice_fila][col]
    
    return suma_fila

def mostrar_participantes_promedio(array_nombres:list,matriz_puntajes:list,promedio:float) -> None:
    """Se encarga de mostrar el promedio obtenido por cada participante

    Args:
        array_nombres (list): Usa el array con los nombres de los participantes para mostrar al participante
        matriz_puntajes (list): Usa la matriz con los puntajes que obtuvo cada participante para calcular y 
        mostrar por consola  
        promedio (float): Si hay participantes que hayan superado el promedio definido como parametro
    """
    bandera = False
    for fil in range(len(matriz_puntajes)):
        suma_puntaje = sumar_fila(matriz_puntajes,fil)
        cantidad_jurados = len(matriz_puntajes[0])
        promedio_puntaje = calcular_promedio(suma_puntaje,cantidad_jurados)

        if promedio_puntaje > promedio:
            mostrar_participante(array_nombres,matriz_puntajes,fil)
            print("")
            bandera = True
    if bandera == False:
        print(f"No hubo participantes con promedio mayor a {promedio}")

def mostrar_jurados_promedio(array_nombres:list,matriz_puntajes:list,array_promedio_jurados:list) -> None:
    """Se encarga de mostrar el promedio obtenido por cada jurado

    Args:
        array_nombres (list): Usa el array con los nombres de los participantes para realizar la operacion
        matriz_puntajes (list): Usa la matriz con los puntajes de cada participantes para realizar la operacion
        array_promedio_jurados (list): Guarda los promedios en su respectivo array
    """
    for fil in range(len(matriz_puntajes[0])):
        suma_puntaje = sumar_columna(matriz_puntajes,fil)
        cantidad_participantes = len(array_nombres)
        promedio_jurado = calcular_promedio(suma_puntaje,cantidad_participantes)
        print(f"JURADO {fil+1}")
        print(f"PUNTAJE PROMEDIO: {round(promedio_jurado,2)}/10")
        array_promedio_jurados[fil] = promedio_jurado

def mostrar_jurado_estricto(array_promedio_jurados:list) -> None:
    """Se encarga de mostrar al jurado con promedio mas bajo

    Args:
        array_promedio_jurados (list): Usa el array con los promedios de los jurados para hallar al mas bajo
    """
    promedio_mas_bajo = array_promedio_jurados[0]
    indice_jurado_estricto = 0
    for i in range(1, len(array_promedio_jurados)):
        if array_promedio_jurados[i] < promedio_mas_bajo:
            promedio_mas_bajo = array_promedio_jurados[i]
            indice_jurado_estricto = i
    print(f"PROMEDIO MAS BAJO: JURADO {indice_jurado_estricto + 1} con: {round(promedio_mas_bajo,2)}/10")

def calcular_y_mostrar_top_3_participantes(array_nombres:list,matriz_puntajes:list) -> None:
    """Se encarga de mostrar el TOP 3 de los participantes con mayor puntuacion

    Args:
        array_nombres (list): Usa el array con los nombres de los participantes para mostrar en consola 
        matriz_puntajes (list): Usa la matriz con los puntajes de los participantes para calcular y mostrar en 
        consola
    """
    promedios_participantes = [(array_nombres[i], calcular_promedio_puntajes(sumar_fila(matriz_puntajes, i), len(matriz_puntajes[0]))) 
                                   for i in range(len(array_nombres))]


    for fil in range(len(promedios_participantes)):
        for col in range(fil+1,len(promedios_participantes)):
            if promedios_participantes[col][1] > promedios_participantes[fil][1]:
                promedios_participantes[fil], promedios_participantes[col] = promedios_participantes[col], promedios_participantes[fil]


    print("TOP 3 PARTICIPANTES CON MAYOR PUNTAJE PROMEDIO:")
    for i in range(min(3, len(promedios_participantes))): 
        print(f"{i+1}. {promedios_participantes[i][0]} - Promedio: {round(promedios_participantes[i][1], 2)}")


#ESPECIFICA     
def ordenar_participantes_alfabeticamente(array_nombres:list,matriz_puntajes:list) -> None:
    """Se encarga de ordenar a los participantes alfabeticamnete

    Args:
        array_nombres (list): Usa el array con los nombres de los participnates para ser ordenados 
        alfabeticamente (usando la funcion "intercambiar_elementos")
        matriz_puntajes (list): Usa la matriz con los puntajes para cargar los puntajes otorgados por cada 
        jurado
    """
    for izq in range(len(array_nombres) - 1):
        for der in range((izq + 1),len(array_nombres)):        
            if array_nombres[izq] > array_nombres[der]:
                #Intercambiar sus nombres
                intercambiar_elementos(array_nombres,izq,der)
                intercambiar_elementos(matriz_puntajes,izq,der)

#GENERAL
def intercambiar_elementos(array:list,izq:int,der:int) -> None:
    """Se encarga de intercambiar los elementos que se encuetran en el array segun las condiciones que se 
    establezcan posteriormente

    Args:
        array (list): El array a usar
        izq (int): Los elementos de la izquierda se van a comparar con los de la derecha
        der (int): Los elementos de la derecha se van a comparar con los de la izquierda
    """
    auxiliar = array[izq]
    array[izq] = array[der]
    array[der] = auxiliar
