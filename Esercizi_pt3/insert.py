def insert(lista, value, index):

    new_lista = []

    if index > len(lista):
        index = len(lista)

    i = 0
    while i < len(lista):
        if i == index:
            new_lista.append(value)
        new_lista.append(lista[i])
        i += 1

    if index == len(lista):
        new_lista.append(value)
    
    return new_lista

lista1 = insert([4,9,0,-4,2,-8],6,3)
lista2 = [4,9,0,6,-4,2,-8]

print(lista1 == lista2)





