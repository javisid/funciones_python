# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.2

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# --------------------------------
# Aquí dentro definir la función que solicitará
# el nombre de tres invitados
def generar_invitados(cantidad_invitados):
    invitados_ingresados = []
    print('Ingresar nombre de 3 invitados')
    i = 0
    while i < 3:
       invitado = str(input())
       invitados_ingresados.append(invitado)
       i = i + 1
    return invitados_ingresados
#def generar_invitados():
#    invitados = []
#    print('Ingresar nombre de 3 invitados')
#def generar_invitados(cantidad_invitados):
#    invitados_1 = []
#    print('Ingresar nombre de 3 invitados')
#    for i in range(1, 2, 3,):
#        invitado = str(input())
#        invitados_1.append(invitado)

      


# --------------------------------


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    cantidad_invitados = 3
    lista_invitados = []
    invitados = generar_invitados(cantidad_invitados)
    print('Listado de invitados:')
    for i in invitados:
        print(i)

    

    
    # Alumno: Crear la función "generar_invitados"

    # Dentro de esa función el sistema deberá solicitar
    # al usuario por consola que ingrese tres nombres de 
    # tres invitados.
    # IMPORTANTE: Utilizar un "input" por cada invitado
    # que se solicite ingresar

    # Los tres nombres ingresados se deberán guardar en
    # una lista

    # La función generar_invitados deberá retornar
    # la lista de invitados generados

    # NOTA: Recomendamos utilizar bucles para no repetir código
    # y solicitar los 3 invitiados, uno en cada iteración del bucle

    # Luego de crear la función invocarla en este lugar:

    # lista_invitados = generar_invitados()

    # Imprimir en pantalla "lista_invitados":

    print("terminamos")
