#using a temporay variable

a=5
b=9
print('Before Swapping Value of a is: {} and b is: {}'.format(a,b))
temp=a
a=b
b=temp
print('After Swapping Value of a is: {} and b is: {}'.format(a,b))

print('-----------------------------------------------------')
#without using a temporay variable

a,b=10,20
print('Before Swapping Value of a is: {} and b is: {}'.format(a,b))
b,a=a,b
print('After Swapping Value of a is: {} and b is: {}'.format(a,b))