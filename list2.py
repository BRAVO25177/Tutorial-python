#3. Write a python program to take a list of integers. Create another list with those numbers in the master list that are less than a number entered by the user. Print the new list contents.
l=list((input("ENter elements of a list seperated by space :")).split())
print("master list :",l)
l1=[]
c=int(input("Enter a number : "))
for i in l:
    if int(i)<c:
        l1.append(int(i))
print(l1)