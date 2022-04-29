class student:
    def __init__(self,fname,lname,id,score):
        self.fname = fname
        self.lname = lname
        self.id = id
        self.score = score

    def grade(self):
        per = int(sum(self.score)/(len(self.score)))
        if 90<=per<=100:
            return 'O'
        elif 80<=per<90:
            return 'E'
        elif 70<=per<80:
            return 'A'
        elif 55<=per<70:
            return 'P'
        elif 40<=per<55:
            return 'D'
        elif per<40:
            return 'F'

    def show(self):
        print('Name :',self.fname,self.lname)
        print('ID : ',self.id)

fname = input('Enter the student first name : ')
lname = input('Enter the student last name : ')
id = input('Enter the student ID number : ')
score = list(map(int,input('Enter the score : ').split(',')))
stud = student(fname,lname,id,score)
stud.show()
print('Grade : ',stud.grade())