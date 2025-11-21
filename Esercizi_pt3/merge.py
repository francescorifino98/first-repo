list1 = [1,2,3,4,5]
list2 = [6,7,8]

def merge(list1, list2):
    list3 = []
    i = 0 
    z = 0

    while i < len(list1) and z < len(list2):
        list3.append(list1[i])
        list3.append(list2[z])
        i +=1
        z +=1

    while i < len(list1):
        list3.append(list1[i])
        i +=1

    while z < len(list2):
        list3.append(list2[z])
        z +=1

    return list3

print(merge(list1, list2))