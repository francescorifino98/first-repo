def convertGrade (n):
    if type(n) != int:
        return "Errore: il voto deve essere un numero"
    if n < 0:
        return "Errore: il voto deve essere maggiore di 0"
    if n >= 100:
        return "A"
    if n > 90 and n < 99:
        return "B"
    if n>80 and n<89:
        return "C"
    if n>66 and n<79:
        return "D"
    else:
        return "F"
    
print(convertGrade(65))
