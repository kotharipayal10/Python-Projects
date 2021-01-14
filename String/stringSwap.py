def swap(str1, str2):
    char1 = str1[0] + str1[1]
    char2 = str2 [0] + str2[1]
    str1 = char2 + str1[2:]
    str2 = char1 + str2[2:]

    print(str1, str2)

def char_mix(str1, str2) :
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str1[2:]
    print(new_str1,new_str2)

str1 = input("1st String : ")
str2 = input("2nd String : ")
swap(str1,str2)

