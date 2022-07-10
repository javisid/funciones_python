# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí copiar la función "generar_invitados"
# ya elaborada

# --------------------------------

# --------------------------------
# Aquí copiar la función "ordenar"
# ya elaborada
def generar_invitados(cantidad_invitados):
    invitados_ingresados = []
    print('Ingresar nombre de 3 invitados')
    i = 0
    while i < 3:
       invitado = str(input())
       invitados_ingresados.append(invitado)
       i = i + 1
    return invitados_ingresados

# --------------------------------
def ordenar(lista):
    ordenados = sorted(lista)
    return ordenados


if __name__ == '__main__':
    print("Listado de Invitados")
    cantidad_invitados = 3
    lista_invitados = []
    invitados = generar_invitados(cantidad_invitados)
    invitados_ordenados = ordenar(invitados)

    print('Listado de invitados ordenados:')
    for i in invitados_ordenados:
        print(i)
    # Alumno: Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bucle "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenala

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el resultado en "lista_invitados"

    # lista_invitados = generar_invitados()

    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada

    # lista_invidatos_ordenada = ordenar(lista_invitados)

    # Imprimir en pantalla "lista_invidatos_ordenada":

    print("terminamos")
