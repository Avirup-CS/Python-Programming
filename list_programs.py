# WAP to remove duplicate from the list.

original_list=[1,2,6,2,7,4,6,8,8,9]
print(original_list)
new_list=[]

for x in original_list:
    if x not in new_list:
        new_list.append(x)
print(new_list)

