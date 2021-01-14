txt = input("Enter a String:")
strList = []
for n in txt:
    strList.append(n)
strLen = len(strList)
print("String Length is ",strLen)
outputStr = ""
outputStr += strList[0] + strList[1] + strList[strLen-2] + strList[strLen-1]
print("Final Output: ", outputStr)
#print(strList[0] + strList[1] + strList[strLen-2] + strList[strLen-1])
