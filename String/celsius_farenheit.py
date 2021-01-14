def celsius(degree):
    cel = (degree-32)*(5/9)
    return cel

def Farenheit(degree):
    Faren = (degree*9/5)+32
    return Faren

print("100 Farenheit is ", celsius(100), "Celsius")
print("40 Celsius is ", Farenheit(40), "Farenheit")