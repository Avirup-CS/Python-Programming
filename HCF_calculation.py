num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))

while(num1 != num2):
    if(num1 > num2):
        num1 = num1 - num2
    else:
        num2= num2 - num1

print('The HCF is = {}'.format(num1))

