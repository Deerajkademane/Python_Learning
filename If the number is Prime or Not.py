# Check given number is Prime or Not.
x = int(input('Enter the Number : '))
if x%2!=0 and x%3!=0:
    print(x,'is Prime Number')
else:
    print(x,'is not Prime Number')