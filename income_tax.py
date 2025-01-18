inc=float(input("Enter taxable income : "))
tax=0
if inc > 300000 and inc <= 600000:
    tax=.05*inc
elif inc > 600000 and inc <= 900000:
    tax=.1*inc
elif inc > 900000 and inc <= 1200000:
    tax=.15*inc
elif inc > 1200000 and inc <= 1500000:
    tax=.2*inc
elif inc > 1500000 :
    tax=.3*inc

if inc>5000000 and inc <=10000000:
    surchrge=.1*inc
else:
    surchrge=.15*inc
cess=.04*inc
total=tax+surchrge+cess
print(f"Taxable income : {inc:,.2f}")
print(f"total tax :{total:,.2f}")
 