n = int(input('Enter a number: '))

for i in range(2,n//2):
    if(n%i == 0):
        print(n,' is not prime.')
        break
else:
    print(n,' is prime.')
