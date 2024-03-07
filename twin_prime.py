def twin_prime(n):
    for i in range(2,n//2+1):
        if(n % i == 0):
            return False
    return True

for i in range(2,1000):
    if(twin_prime(i) and twin_prime(i+2)):
        print(i,' ',i+2)