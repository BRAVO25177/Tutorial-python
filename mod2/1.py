'''word = input('Enter a word :')
dis=int(input('Enter the distance :'))
new=''
for i in word:
    ordinal=ord(i)+dis
    if(ordinal>ord('z')):
        ordinal-=26
    new+=chr(ordinal)
print(new)
word1=''
for i in new:
    ordinal=ord(i)-dis
    if(ordinal<ord('a')):
        ordinal+=26
    word1+=chr(ordinal)
print(word1)'''

def sum(high):
    return high

def odd(a):
    if a%2!=0:
        return True
l=[2,4,5,7,3,4,2]
out=list(filter(odd,l))
print(out)
from functools import reduce
def mul(x,y):
    return x*y
print(reduce(mul,l))

#lambda
print(reduce(lambda x,y:x*y,l))