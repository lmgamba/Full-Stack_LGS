import requests as rq

def obtener_personajes(n=20):
    url='https://rickandmortyapi.com/api/character/'
    personajes=[]
    try:
        ## Cuando son solo 20:
        response= rq.get(url)
        respuesta=response.json()['results']
        ####
        # # Necesario cuando n es mayor a 20:
        # for i in range(1,n+1):
        #     response= rq.get(url+str(i))
        #     respuesta=response.json()
        #     personajes.append(respuesta)
    except KeyError:
        print('Error')
    return respuesta

def show_personajes(lista,n=20):
    if len(lista)<n: #en caso que se filtra la lista.
        n=len(lista)
        
    for i in range(0,n):
        print(f'############ {i+1}:## {lista[i]['name']}  ##  {lista[i]['species']}  ##  {lista[i]['status']} ## ##################')
            
def filtrar_especie(especie, lista):
    filtrado = list(filter(lambda personaje: personaje['species'].lower()== especie.lower(), lista))
    return filtrado

def filtrar_estado(estado, lista):
    filtrado = list(filter(lambda personaje: personaje['status'].lower()== estado.lower(), lista))
    return filtrado