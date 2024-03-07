#Checking a number is armstrong or not.

num=int(input('Enter a number : '))

n=num
rnum=0
c=0

while(num>0):
    rem = num % 10
    c = c + 1
    rnum = rnum*10 + rem
    num = num // 10
    
        
while(rnum>0):
    rem = rnum % 10
    num = num + (rem**c)
    rnum = rnum // 10
        
if(num == n):
    print(n,' is a Armstrong Number.')
else:
    print(n,' is a not a Armstrong Number.')
    