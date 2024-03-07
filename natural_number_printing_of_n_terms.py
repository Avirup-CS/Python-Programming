n=int(input('Enter the number of terms: '))

sum=0
for i in range(1,n+1):
    sum = sum + i
    
print('The sum of {} natural number is = {}'.format(n,sum))