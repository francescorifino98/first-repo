def numberBetween(end, start):
    list=[]
    i = min(start, end)
    while i<=max(start,end):
        list.append(i)
        i+=1
    print(list)

numberBetween(25,12)
