#5. Write a python program to take two list of integers and return a list containing the elements that are common in both the list. Also print the contents of new list.
l=list(int(x) for x in input("Enter a list of numbers sep by space : ").split())
m=list(int(x) for x in input("Enter a list of numbers sep by space : ").split())
print("list1 :",l)
print("list2 :",m)
common=[]
for i in l:
    if i in m:
        common.append(i)
print("common elements : ",common)