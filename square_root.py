x=int(input("Enter a number  :"))
if x<2:
    print(x)
else:
    y = x
    z = (y + (x/y)) / 2
    while abs(y - z) >= 0.00001:
        y = z
        z = (y + (x/y)) / 2
    print(z)