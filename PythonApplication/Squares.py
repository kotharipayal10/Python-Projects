n = int(input("Enter a number:"))
s = 0
for i in range(1, n+1):
        s = s + pow(i,2)
print("Sum of the squares of first ", n , "numbers is :", s)
c = 0
for i in range(1, n+1):
        c = c + pow(i,3)
print("Sum of the cubes of first ", n , "numbers is :", c)
