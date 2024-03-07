#Calculating the palindrome of a number

n=int(input('Enter a number : '))
temp=n
rev=0

while(n>0):
    rem = n % 10
    rev = rev*10 + rem
    n = n // 10
    
print('The palindrome of {} is: {}'.format(temp,rev))