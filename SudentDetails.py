#student details to find avg marks and greather or not compare to other students scores

class student:

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def avg(self,other):
        q = (self.a+self.b+self.c)/3
        return q

    def __gt__(self,other):
        g = self.a+self.b+self.c
        h = other.a+other.b+other.c
        globals()['a'] = g
        globals()['b'] = h
        if g>h:
            return True
        else:
            return False


stu1 = student(56,47,89)
stu2 = student(89,94,76)

a = 0
b = 0

print(stu1.avg(stu2))

if stu1 > stu2:
    print('stu1 is greater',a,'compare to',b)
else:
    print('stu2 is greater',b, 'compare to stu1',a)

