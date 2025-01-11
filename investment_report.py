startingbalance = float(int(input("Enter your investment amount:")))
years = int(input("Enter the number of years of your investment:"))
rate = float(input("Enter your rate in %:"))

endingbalance = startingbalance
x=startingbalance

print('Years:\tStarting Balance:\tInterest:\tEnding Balance:\n')

for years in range (1, years +1):
    interest = startingbalance * (rate/100)
    endingbalance = x + interest
    x=endingbalance
    print(f"{years}\t{startingbalance:,.2f}\t\t{interest:,.2f}\t{endingbalance:,.2f}")
    
interestearnt = endingbalance - startingbalance

print(f"Ending balance: ${endingbalance:,.2f}")
print(f"Interest earnt: ${interestearnt:,.2f}")