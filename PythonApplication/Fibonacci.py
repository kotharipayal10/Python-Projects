"""
x = int(input("Enter a number:"))
fibo = [0,1]
p = 0
q = 1

for i in range (1, x):
    r = p + q
    fibo.append(r)
    p =q
    q = r
    
print (x, "th Fibponacci number is :", fibo[x-1]) #print nth fibonacci  number
print ("Fibonacci Series is :", fibo) # print fibonacci series
"""
n = int(input("Enter a fibonacci number :"))

def isSquare(s) :
    sqrt = int(pow(s, 0.5))
    return sqrt*sqrt == s

if (isSquare(5*n*n + 4) or isSquare(5*n*n - 4) ):
    print (n, "is a Fibonacci number.")
else:
    print (str(n)+ "is not a Fibonacci number.")