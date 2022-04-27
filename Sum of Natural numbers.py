#Program to find sum of natural numbers
x = int(input('Enter the number'))
if x<0:
    print('Please enter the positive number')
else:
    sum=0
    while x>0:
        sum+=x
        x-=1
    print('The sum of Natural number is',sum)