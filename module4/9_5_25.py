

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

class Cat(Animal):
    def __init__(self, name):
        super().__init__('cat')
        self.name=name
    def make_sound(self):
        print('Meow')
    def __str__(self):
        return f'Name :{self.name},cat'
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
'''d1=Dog('jimmy','German Shephard')
d1.make_sound
d1.swim()
print(d1)
c1=Cat('bl')
print(c1)
'''
#overloading - same method different argments
#method overloading
#operator ..
#constructor overloading

class Overloading:
    def __init__(self):
        print('no arg')
    def __init__(self,a):
        print('one arg')
    def one(self):
        print('no arg')
    def one(self,a):
        print('one arg')
    def one(self,a,b):
        print('2 arg')
'''a=Overloading()
#a.one()
a.one(3)
a.one(10,20)'''
#overriding
class Parent:
    def __init__(self):
        print('parent')
class Child(Parent):
    def __init__(self):
        super().__init__()
        print('child')
#c=Child()
from abc import ABC,abstractmethod
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self,w,h):
        return w*h
class Circle(Shape):
    def area(self,r):
        return 3.14*r*r       
#print(Circle().area(5))
#print(Rectangle().area(2,4))

#interface...-contains only abstract methods
from abc import ABC,abstractmethod
class Interface(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        pass
class Child1(Interface):
    def method1(self):
        print('m1')
    def method2(self):
        print('m2')
#m1=Child1().method2()

#Exception
def exc(a,b):
    sum=0
    if(b<0 or a<0):
        raise ValueError('input postive values')
    try:
        div=b/a
    except ZeroDivisionError as z:
        print("Zeroerror",z)
    except:
        print('unidentified error')
    else:
        print('no errors')
    finally:
        print('Execution completed')
exc(1,2)
#exc(-1,-1)
exc(0,2)
