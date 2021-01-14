
x = int(input("Enter the start of range:"))
y = int(input("Enter the end of range:"))

for i in range(x, y+1):
  if i > 1:
     rangeVal = int(i/2)
     print("i, rangeVal : ", i, rangeVal)
     for p in range(2, rangeVal):
        print ("i, rangeVal, p : ", i, rangeVal, p)
        if i%p == 0:
            break
     else:
        print(i)