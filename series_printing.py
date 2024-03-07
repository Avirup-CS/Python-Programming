# Series --> 1,3,7,13,21,31

n = int(input('Enter the number of terms: '))
value=0
print('The Series are - - - - -')
for i in range(1,n+1):
    value = (i**2) - (i - 1)
    print(value,end=',') 
