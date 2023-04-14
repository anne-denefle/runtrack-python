n=10

print("+",("-"*(n+1)),"+")

def les_etoiles(n):
    for i in range(n+1):
        print("|",("#"*(n-i)), ("#"*i),"|")


les_etoiles(n)

print("+",("-"*(n+1)),"+")
