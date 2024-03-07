a,b = [int(i) for i in input('Enter the minimum and maximum limit: ').split(',')]

x = a
if(x % 2 != 0):
    x += 1

while(x<=b):
    print(x,end=',')
    x += 2