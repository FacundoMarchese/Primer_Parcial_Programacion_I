import os
from Inputs import *
from Funciones import *

#Menú

#Necesito crear un sistema que me permita guardar los puntajes de 5 participantes de un concurso de baile, 
# cada puntaje se va a guardar por jurado

#Matrices de datos con apoyo de vectores paralelos 

# 1. Cargar nombres alumnos
# 2. Cargar notas de cada trimestre
# 3. Mostrar alumnos
# 4. Mostrar promedio de notas
# 5. Mostrar nombre de los alumnos que se llevan la materias
# 6. Mostrar nombre de los alumnos que como nota final les quedo un aplazo
# 7. Ordenar alfabeticamente a los alumnos y mostrarlos
# 8. Ordenar a los alumnos por la nota del trimestre 1 más alta
# 9. Salir

array_nombres = crear_array(5,"")
array_promedios_jurados = crear_array(3,"")
matriz_puntajes = crear_matriz(5,3,0)
array_promedios_participantes = crear_array(5,"")


while True:
    print("1. Cargar nombres participantes\n2. Cargar puntajes de cada jurado\n3. Mostrar participantes, puntajes y promedio general\n4. Mostrar participantes con promedio mayor a 4\n5. Mostrar participantes con promedio mayor a 7\n6. Mostrar el promedio de puntuaciones otorgadas por cada jurado\n7. Mostrar cuál jurado otorgó los puntajes promedio más bajos\n8. Buscar participante por nombre\n9. Mostrar los tres participantes con mayor puntaje promedio\n10. Ordenar participantes alfabeticamente\n11. Salir")

    opcion = transformar_caracter_a_ascii("Ingrese su opcion: ")
    
    while True:
        if opcion == 49:
            print("CARGANDO NOMBRES")
            cargar_nombres_participantes(array_nombres)
            print("NOMBRES CARGADOS CORRECTAMENTE")
            break
        elif opcion == 50:
            print("CARGANDO PUNTAJES")
            cargar_puntaje_jurado(matriz_puntajes)
            print("PUNTAJES CARGADOS CORRECTAMENTE")
            break
        elif opcion == 51:
            mostrar_participantes(array_nombres,matriz_puntajes)
            break
        elif opcion == 52:
            mostrar_participantes_promedio(array_nombres,matriz_puntajes,4)
            break
        elif opcion == 53:
            mostrar_participantes_promedio(array_nombres,matriz_puntajes,7)
            break
        elif opcion == 54:
            mostrar_jurados_promedio(array_nombres,matriz_puntajes,array_promedios_jurados)
            break
        elif opcion == 55:
            mostrar_jurado_estricto(array_promedios_jurados)
            break
        elif opcion == 56:
            buscar_nombre_participante(array_nombres,matriz_puntajes)
            break
        elif opcion == 57:
            calcular_y_mostrar_top_3_participantes(array_nombres,matriz_puntajes)
            break
        elif opcion == '10':
            ordenar_participantes_alfabeticamente(array_nombres,matriz_puntajes)
            mostrar_participantes(array_nombres,matriz_puntajes)
            break
        elif opcion == '11':
            break
        else:
            opcion = transformar_caracter_a_ascii("Reingrese su opcion (1-11): ")
    
    if opcion == '11':
        print("Saliendo...")
        break
    
    input("Toque cualquier boton para continuar...")
    os.system("cls")
