print('Armstrong Numbers between 1 to 500: ')

for num in range(1,501):
    temp = num
    sum=0
    while(num > 0):
        rem = num % 10
        sum = sum + (rem*rem*rem)
        num = num // 10

    if(temp == sum):
        print(temp, )