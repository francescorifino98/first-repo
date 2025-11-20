def countletter(string):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    vow, cons = 0, 0
    i = 0
    if type(string) == str:
        while i < len(string):
            if string[i] in vowels:
                vow+=1
            else:
                cons +=1
            i+=1
        return [vow,cons]
    else:
        return "Non è una stringa"

print(countletter("Ciao come stai?"))