f1=open('int.txt','r')
f2=open('text.txt','r')
try:
    f3=open('helo.txt','r')
except FileNotFoundError as f:
    print('hoo')
except Exception as e:
    print(e)

ch='y'
integer=[]
while(ch!=""):
    ch=f1.readline()
    y=ch.split()
    for i in y:
        integer.append(int(i))
print(integer)
f1.close()
content=f2.readline()
content=f2.readline()
print(content)
f2.close()