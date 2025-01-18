bin=input("Enter binay number:")
bin=bin[::-1]
dec=0
j=0
for i in bin:
    i=int(i)
    dec+=i*pow(2,j)
    j += 1
print(f"Decimal value : {dec}")