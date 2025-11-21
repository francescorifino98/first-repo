N = 50
L = [3, 5]
results = []

i = 1
while i <=N:
    divisible = True
    x = 0
    while x < len(L):
        if i%L[x] != 0:
            divisible = False
            break
        x +=1
    if divisible == True:
        results.append(i)
    i +=1

print(results)