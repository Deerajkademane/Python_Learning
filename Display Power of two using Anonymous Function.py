# Display Power of two using Anonymous Function.

terms = int(input('How many Terms : '))

func = list(map(lambda x:x**2,range(terms)))

for i in range(terms):
    print('2 raised to power of',i,'is',func[i])