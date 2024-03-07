print(' F(x) = 3x^2 + 5  if x<=10 ')
print('      = 5x        if x>10 and x<=20')
print('      = 2x^2-x+9   if x>20')

x = float(input('Enter a value: '))

if(x>20):
    value = (2*pow(x,2))-x+9
    print('Value is: ',value)
elif(x>10 and x<=20):
    value = 5*x
    print('Value is: ',value)
elif(x<=10):
    value = (3*pow(x,2))+5
    print('Value is: ',value)