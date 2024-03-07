num = [5,8,11,2,3,7,44]
key = int(input('Enter the element to find: '))

for x in num:
    if(key==x):
        print('Element is found.')
        break
else:
    print('Element is not found !!')

