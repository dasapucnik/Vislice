def prastevila(n):
    for i in range(i, n):
        if n % i == 0:
            return False
    return True

    
for i in range (1, 200):
    if prastevila(i):
        print(i)