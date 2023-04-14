for i in range(2,1001):
    is_prime=True
    for k in range (2,i):
        if i % k ==0:
            is_prime=False
            break
    if is_prime:
        print(i)

