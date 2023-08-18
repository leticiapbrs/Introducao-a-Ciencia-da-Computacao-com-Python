lista = [6, 2, 6, 6, 1, 2, 2, 3, 4, 4, 5]

def remove_repetidos(lista):
    lista_sem_repetidos = sorted(list(set(lista)))
    return lista_sem_repetidos

lista_sem_repetidos = remove_repetidos(lista)

print(lista_sem_repetidos)
        
