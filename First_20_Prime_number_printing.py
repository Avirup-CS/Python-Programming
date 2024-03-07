def isPrime(n):
    flag=0
    for i in range(1,n+1):
            if(n%i == 0):
                flag = flag + 1

    if(flag==2):
        return True
    else:
        return False

print('The 20 Primes are: ')
count=0
num=2
while(count < 20):
    if(isPrime(num)):
        print(num,end=',')
        count += 1
    num += 1

