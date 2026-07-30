##list


my_list = [1,2,3,4,5]
print(my_list)
print(type(my_list))

#properties of list
#1.ordered
fruit = ['apple','banana']
print(fruit)
fruit = ['banana', 'apple']
fruit = ['banana', 'apple']
print(fruit)

#2.allows duplicates              
fruit= ['banana','apple','banana']
print(fruit)

#heterogenous : can store any data type
mixed = [1,'hello',3.14,True]
print(mixed)

l = [1,2,3,4,5]
Ii = [3,'hello',4.6,None,'A',3,True,False,4,"hi",[1,2,3,4],True,["hi","hoi"],2+1j]
print(Ii)
print(type(Ii))
print(1)
print(type(1))

#mutable : element can change
my_list = [1,2,3]
my_list[0]=100
print(my_list)

#Slicing and index
l= ["hello","hi",23,45.6,True,12,78,False,[1,2,3,4,5]]

print(l[3])           
print(l[1])

print(l[-1])
print(l[-2])

print(l[2:4])
print(l[-5:-1])

print(l[-1:-6:-1])
print(l[::-1])
print(l[-1::-1])
print(l[:-1])
