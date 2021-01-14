txt = input("Enter a text: ")
#char_dict ={}

def freq(x):
    char_dict = dict()
    for i in x:
        if i in char_dict:
            char_dict[i] +=1
        else:
            char_dict[i] = 1
    return char_dict

def word_count(txt):
    count = dict()
    words = txt.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count



print ("Following is the frequency of each character: ", freq(txt))
print(word_count("How much wood would a woodchuck chuck if a woodchuck could chuck wood"))

