# Find the largest among three numbers.
x = int(input('Enter the First Number'))
y = int(input('Enter the Second Number'))
z = int(input('Enter the Third Number'))
if x>y and x>z:
    print(x,'is greater')
elif y>x and y>z:
    print(y,'is greater')
elif z>x and z>y:
    print(z,'is greater')
else:
    print('All are equal')