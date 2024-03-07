def getData(m,row,col):
  m=[]
  for i in range(row):
    b=[]
    for j in range(col):
      x=int(input("enter data:"))
      b.append(x)
    m.append(b)
  return m

def display(m):
    for x in m:
      for y in x:
        print(y,end=' ')
      print()
         
row1=int(input("enter the row for 1st matrix:"))
col1=int(input("enter the col for 1st matrix:"))
row2=int(input("enter the row for 2nd matrix:"))
col2=int(input("enter the col for 2nd matrix:"))
m1=[]
m2=[]
if(row1==row2 and col1==col2):
  print("enter the data for 1st matrix:")
  m1=getData(m1,row1,col1)
  print("enter the data for 2nd matrix:")
  m2=getData(m2,row2,col2)
  m3=[]
  for i in range(row1):
    b=[]
    for j in range(col1):
      x=m1[i][j]+m2[i][j]
      b.append(x);
    m3.append(b)
  print("1st matrix is:")
  display(m1)
  print("2nd matrix is:")
  display(m2)
  print("Addition matrix is:")
  display(m3)
  
else:
  print("Addition is not possible !! ")