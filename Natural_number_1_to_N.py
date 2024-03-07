#Natural Number - Natural numbers are all positive integers from 1 to infinity. 
#They are also called counting numbers as they are used to count objects.

n=int(input('Enter the number you want to stop: '))

print('The natural numbers between 1 to {} is -->'.format(n))
for i in range(1,n+1,1):
    print(i,end=', ')