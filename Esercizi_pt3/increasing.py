def increasing (list):
    i=0
    while i < len (list)-1:
        if list [i] > list [i+1]:
            return False
        i+=1
    return True

print(increasing ([1,2,3,4,5]))

