lista = [2,4,8,12,-4,7]
def secondMax (lista):
    if lista[0] > lista[1]:
        max, max2 = lista[0], lista[1]
    else: 
        max,max2 = lista[1], lista[0]

    i = 2
    while i < len(lista):
        if lista [i] > max:
            max2, max = max, lista[i]
        elif lista [i] > max2:
            max2 = lista[1]
        i +=1
    return max2

print(secondMax(lista))