"""1. Find the largest and smallest numbers in a list.
2. Find the third largest number in a list.

"""
l=[10,45,23,33,12,88]
print("Largest number in the list is:",max(l))
print("Smallest number in the list is :",min(l))

#Third largest element
l.sort()
print("Third largest number in the list is:",l[-3])
