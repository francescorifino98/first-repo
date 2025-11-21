list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

def mergeEqual(list1, list2):
    i = 0
    list3 = []
    if len(list1) == len(list2):
        while i < len(list1):
            list3.append(list1[i])
            list3.append(list2[i])
            i +=1
    return list3

print(mergeEqual(list1, list2))
    