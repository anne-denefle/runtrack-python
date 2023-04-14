

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
nombrepairs = []
somme=0


for n in L :
    if n%2 == 0 :
        nombrepairs.append(n)

for element in nombrepairs :
    somme += element

print ("le total des nombres pairs est : ", somme)