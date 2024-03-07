limit = int(input('Enter the range: '))
print(f"The prime numbers upto {limit} is: ")
for i in range(2,limit+1):
    for x in range(2,(i//2)+1):
        if(i%x == 0):
            break
    else:
        print(i)
