# Creating Tuples

t1= ()			# empty tuple
t2 = (5,'RCCIIT', 6.5)	# tuple with different types of elements
t3 = (8, )		# tuple with one element   
t4 = 10,20,30,40,50     #no braces
print(type(t1))	# <class 'tuple'>
print(type(t2))	# <class 'tuple'> 
print(type(t3))	# <class 'tuple'> 
print(type(t4))	# <class 'tuple'> 
 

# # Accessing the tuple Elements

# tp = (5,6,7,8,6,9)
# print(tp[2])    # 7
# print(tp[-1])   # 9
# print(tp[1:4])  # (6,7,8)
# print(tp[-4:-1])    #(6, 7, 8)


# #Basic Operation on Tuples

# name = ('Ram','Sam','Kamal')
# age = (21,25,18)
# salary = (25000.00,)
# print(len(name))    # 3
# salary = (25000.00,)*3
# print(salary)   # (25000.0, 25000.0, 25000.0)
# details=name+age
# print(details)  # ('Ram', 'Sam', 'Kamal', 21, 25, 18)
# name1 = 'Sam'
# print(name1 in name)    # True

# In-built Functions

tp = (10,50,30,60,10,40,10,50,20)
print(len(tp))  # 9
print(max(tp))  # 60
print(min(tp))  # 10
print(tp.count(10)) # 3
print(tp.index(50)) # 1
print(sorted(tp))   # [10, 10, 10, 20, 30, 40, 50, 50, 60]
print(sorted(tp,reverse=True))  # [60, 50, 50, 40, 30, 20, 10, 10, 10]

