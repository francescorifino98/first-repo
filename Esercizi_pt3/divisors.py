def divisors(dividendo):
    i = 2
    lista = [1, dividendo]
    while i < dividendo:
        resto = dividendo % i
        if resto == 0:
            lista. insert(-1, i)
        i+=1
    return lista

print(divisors(100))