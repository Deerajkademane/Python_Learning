# Find the Factorial of a number.

def fact(x):
    if x==0:
        return 1
    else:
        return x*fact(x-1)

x = int(input('Enter the Factorial Number : '))
result = fact(x)
print(result)
