n = int(input('Enter a multi-digit number: '))

sum=0
while(n>0):
    rem = n % 10
    sum = sum + rem
    n = n // 10

print('Sum of Digits of the Given number = ',sum)