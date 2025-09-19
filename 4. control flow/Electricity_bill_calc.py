print("Electricity bill calculator")

units = int(input("Enter the no. of units consumed: "))

if ( units <= 100):
    bill = units * 5
elif( units <= 200):
    bill = ( 100 * 5) + ( units - 100)* 8
else :
    bill = ( 100 * 5) + ( 100 * 8) + (units - 200) * 8

print(f"The total bill is {bill}")