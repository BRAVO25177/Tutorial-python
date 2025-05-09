

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.scores=[]

    def add_score(self,score):
        self.scores.append(score)
    def avg_score(self):
        return sum(self.scores)/len(self.scores)
    def printf(self):
        return f'Student:{self.name},Rollno : {self.rollno},Scores :{self.scores}'
    
'''st1=Student('Blesson',4)
st1.add_score(80)
st1.add_score(90)
print(st1.avg_score())
print(st1.printf())'''


#2SIngle Inheritance
class Animal:
    def __init__(self,species):
        self.species=species
    def make_sound(self):
        print('Generic animal sound')
    def swim(self):
        print('cant swim')
    
    
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__('dog')
        self.name=name
        self.breed=breed
    def make_sound(self):
        print('Woof')
    def __str__(self):
        return f'{self.name},{self.breed}'

#animal=Animal('unknown')
d1=Dog('jimmy','German Shephard')
d1.make_sound
d1.swim()
print(d1)