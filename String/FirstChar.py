txt = input("Enter a string:") # string -> txt = rzstazrt
initial_char = txt[0] # txt[0] = r
x = ""
x = x + initial_char
print(initial_char)

for i in range (1, len(txt)): # z t range (1, 10) --> (1, 7)
    if txt[i] == initial_char:
        x = x + "$"
    else:
        x = x + txt[i]
    print(x)



print("Final Output:", x)
