# Multiplication Table using While Loop.
z = int(input('Enter the Number'))
i=0
while i<10:
    i+=1
    print(z,'x',i,'=',z*i)

# Multiplication Table using For Loop.
z = int(input('Enter the Number'))
for i in range(1,11):
    print(z,'x',i,'=',z*i)