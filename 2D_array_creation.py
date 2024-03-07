r=int(input('Enter the no. of rows: '))
c=int(input('Enter the no. of columns: '))

print('Enter the data for the matrix: ')
#taking input from the user
a=[]
for i in range(r):
    b=[]
    for j in range(c):
        b.append(int(input('Enter the data: ')))
    a.append(b)

print('The matrix is: ')
#printing the entire matrix
for x in a:
    for y in x:
        print(y,end=' ')
    print() 

