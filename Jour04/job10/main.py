L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
tri=[]
result=1

for i in L:
    if i>25 and i<90:
        tri.append(i)


for n in tri:
    result *= n

print (result)