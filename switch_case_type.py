def operation(i,x,y):
    return{
        1: x+y,
        2: x-y,
        3: x*y,
        4: x//y
    }.get(i,'Invalid input !!')


a = int(input('Enter 1st value: '))
b = int(input('Enter 2nd value: '))
print('1. Add')
print('2. Sub')
print('3. Mul')
print('4. Div')

ch=int(input('Enter your choice: '))
sol=operation(ch,a,b)
print(sol)

