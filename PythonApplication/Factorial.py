
# Using Recurssion
"""
num = input("Enter a number: ")
def recur_factorial(n):
 if n == 1:
   return n
 elif n < 1:
   return ("NA")
 else:
   return n*recur_factorial(n-1)
print (recur_factorial(int(num)))


"""

# Using for Loop

x= eval(input("Enter a number :"))

fact = 1

if x > 0 :
    for i in range(1,x+1):
        fact = fact * i
    print(fact)
else: print("Invalid Input")




# Using while Loop


x= eval(input("Enter a number :"))

fact = 1

if x > 0 :
    i=1
    while (i<=x):
        fact = fact * i
        i=i+1
    print(fact)
else: print("Invalid Input")
