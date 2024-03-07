marks = float(input('Enter your marks: '))

if(marks >= 75):
    print('Your Remarks: Divison-1')
elif(marks >= 65 and marks <75):
    print('Your Remarks: Divison-2')
elif(marks >= 50 and marks <65):
    print('Your Remarks: Divison-3')
else:
    print('Your Remarks: Failed')