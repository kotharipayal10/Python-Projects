def wordSort(txt):
    #words = []
    #for word in txt.split(","):
        #words.append(word)
    words = [word for word in txt.split(",")]
    print(words)
    print(",".join(sorted(set(words)))) #remove the repeatitive words using set() and then sort it using sorted() and join with comma.

#str1 = input("Enter few comma (,) seperated words : ")
wordSort("how,much,wood,would,a,woodchuck,chuck,if,a,woodchuck,could,chuck,wood")
#str1 = str1.split(',')
#str1.sort()
#print(str1)

