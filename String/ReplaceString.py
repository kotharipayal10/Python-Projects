def replace(str1):
    if len(str1) < 3:
        return str1
    elif str1[-3:] == "ing":
        #str1 = str1 + "ly"
        return str1 +"ly"
    else:
        #strl = str1 + "ing"
        return str1 + "ing"


print(replace("haieing"))
#print (str[-3:])
