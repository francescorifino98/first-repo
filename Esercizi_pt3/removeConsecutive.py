
def removeConsecutive(stringa):
    new_stringa = stringa[0]
    i = 1
    while i < len(stringa): #while loop
        if stringa[i]!=stringa[i-1]: #se la lettera in posizione i è diversa dalla precedente, aggiungila alla nuova stringa
            new_stringa = new_stringa + stringa[i]
        i +=1
    return new_stringa

print (removeConsecutive("Giallo")) #return Gialo

