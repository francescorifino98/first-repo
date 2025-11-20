def sumFrac (num):
    i = 1
    risultato  = 0
    somma = ""
    if type(num) == int and num >= 0:
        while i <= num:
            risultato += (1/i)
            somma += "1/" + str(i)
            if i < num:
                somma += " + "
            i+=1
    return (str(somma) + " = " + str(round(risultato,11)))

print(sumFrac(9))
