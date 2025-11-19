def secret(word):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    new_word = ""
    i = 0
    while i < len(word):
        if word[i] in vowels: #se la lettera è presente nella lista, la aggiunge alla nuova lista
            new_word += word [i]
        else:
            new_word += word[i] #se la lettera non è presente, aggiunge quella lettera seguita da una "o" e nuovamente dalla stessa lettera
            new_word += "o"
            new_word += word[i]
        i += 1
    return new_word

#Test per verificare che l'output sia corretto rispetto alla richiesta
variabile = secret("hello") 
print(variabile == "hohelollolo")