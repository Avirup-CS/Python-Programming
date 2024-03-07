def isPrime(n):
    fact=0
    for i in range(1,n+1):
        if(n%i==0):
            fact+=1
    
    if(fact==2):
        return True
    else:
        return False
    
num=int(input('Enter the upper bound: '))
print('The Twin Primes are: ')
for n in range(2,(num+1)-2): # (num+1)-2 is done otherwise the last number will exceed the upper limit. 
    if(isPrime(n) and isPrime(n+2)):
        print(n,n+2) 