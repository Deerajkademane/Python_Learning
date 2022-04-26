# program 2 - Simple calculator
x = int(input('Enter the First Number'))
op = input('Enter the operator')
y = int(input('Enter the second Number'))

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return print('wrong input')
    else:
        return x/y

if '+' == op:
    print('The Addition number is',add(x,y))
elif '-' == op:
    print('The Substraction number is',sub(x,y))
elif '*' == op:
    print('The Multiplication number is',mul(x,y))
elif '/' == op:
    print('The Division number is',div(x,y))
else:
    print('Invalid operator')
