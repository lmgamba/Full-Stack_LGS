""" 
###########################################

4. EJERCICIO: Trabajar con la API de Rick & Morty usando requests
Construir un pequeño programa en Python que consulte la API pública de Rick & Morty y realice varias búsquedas y filtrados utilizando la librería requests.

sando la API pública de Rick and Morty:

URL base:
https://rickandmortyapi.com/api/character

Debes crear un script en Python que:

Debes crear un script en Python que:

1️⃣ Obtenga 20 primeros personajes de la API

Guarda el resultado final en una lista llamada personajes.

2️⃣ Imprima:

El número total de personajes
Los primeros n personajes siendo n un numero pedido al usuario


3️⃣ Filtrar personajes raza

Crear una lista con todos los personajes cuya especie sea "Human". Siendo Human algo pedido por pantalla

4️⃣ Buscar personajes por estado

Pide al usuario un estado (Alive, Dead, unknown) y muestra:
El número total de personajes con ese estado.
    """
import requests as rq
from lib.fuctions import *
    
def main():
    menu="""
    [1]Mostrar los 20 primeros personajes
    [2]Mostrar n personajes entre los 20 primeros.
    [3]Filtrar personajes segun especie
    [4]Buscar numero de personajes por status
    """
    print(menu)
    option= input('Que quieres hacer? (Elije entre op.: 1,2,3 o 4): ')
    personajes= obtener_personajes()
    if option == '1':
        show_personajes(personajes)
    elif option == '2':
        n = int(input('Dime el numero (entre 1 y 20) de personajes que quieres ver: '))
        print(f' El numero total de personajes es {len(personajes)}, tu has pedido {n}: ')
        show_personajes(personajes,n)
    elif option == '3':
        especie= input('Dime que especie quieres consultar: ')
        lista_especie= filtrar_especie(especie,personajes)
        show_personajes(lista_especie)
    elif option == '4':
        estado = input('Dime el estado que quieres consultar: ')
        lista_estado= filtrar_estado(estado,personajes)
        print(f' Hay {len(lista_estado)} personajes con el estatus {estado}')
    else:
        print('Opcion no válida, vuelva a intentar ')
        main()
    
    
if __name__ == "__main__":
    main()