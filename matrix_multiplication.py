r=int(input('Enter the no. of rows: '))
c=int(input('Enter the no. of columns: '))

print('Enter the data for the 1st matrix: ')
a1=[]
for i in range(r):
    b1=[]
    for j in range(c):
        b1.append(input('Enter the data: '))
    a1.append(b1)

print('Enter the data for the 2nd matrix: ')
a2=[]
for i in range(r):
    b2=[]
    for j in range(c):
        b2.append(input('Enter the data: '))
    a2.append(b2)

print('The input 1st matrix is: ')
for x in a1:
    for y in x:
        print(y,end=' ')
    print()

print('The input 2nd matrix is: ')
for x in a2:
    for y in x:
        print(y,end=' ')
    print()

mat=[]
for i in range(r):
    c=[]
    for j in range(c):
        m=0
        for k in range(c): 
            m += a1[i][k] * a2[k][j]  
        c.append(m)
    mat.append(c)

print('The output matrix is: ')
for x in mat:
    for y in x:
        print(y,end=' ')
    print()    