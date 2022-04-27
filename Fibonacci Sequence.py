# Program to find first 50 Fibonacci numbers.
a=0
b=1
print(a)
print(b)
for i in range(100):
    x=a+b
    if x<=50:
        print(x)
        a,b=b,x
    else:
        break
