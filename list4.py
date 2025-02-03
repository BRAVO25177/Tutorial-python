#4. Write a python program to take a list of integers. Create another list to store all the even
#numbers from the master list and print the new list contents in ascending order
l=list(int(x) for x in input("Enter a list of numbers sep by space : ").split())
print(l)
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
l1.sort()
print("new list :",l1)