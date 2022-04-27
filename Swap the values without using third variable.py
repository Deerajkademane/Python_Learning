#Swap the variables without using third variable
x = int(input('Enter the First number'))
y = int(input('Enter the Second number'))
print('This two variables needs to b swapped',x,y)
a = x+y
b = a-y
a = a-b
print('Variables has been swapped',a,b)

#Swapping variables using third variable
x = int(input('Enter the First number'))
y = int(input('Enter the Second number'))
print('This two variables needs to b swapped',x,y)
temp = x
x=y
y=temp
print('Variables has been swapped',x,y)