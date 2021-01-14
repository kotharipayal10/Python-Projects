x = input("Enter a Number:")
n = [int(i) for i in str(x)]
print(n)
l = len(n)
print(l)
AN = 0
for i in n:
    AN = AN + pow (i,l)
print("Addition of digits is :", AN)
if (AN == int(x)):
    print(x, " is an Armstrong Number")
else: 
    print(x, " is not an Armstrong Number")


