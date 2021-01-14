"""
P = eval(input("Principal Amount : "))
T = eval(input("Period of Investment:"))
R = eval(input("Interest Rate:"))

if((type(P) is float) and (type(T) is float) and (type(R) is float) ):
    print("Interest Amount is :" + str((P*T*R)/100))
else :
    print("Invalid Input")
"""


p=float(input("Enter the principle amount:"))
t=float(input("Enter the time(years):"))
r=float(input("Enter the rate:"))
simple_interest=(p*t*r)/100
print("The simple interest is:", simple_interest)
print("The compound interest is:",(p*(1+r/100)*t))