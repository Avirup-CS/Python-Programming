def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x//y


def operation(i,x,y):
    return{
        1: add(x,y),
        2: sub(x,y),
        3: mul(x,y),
        4: div(x,y)
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

