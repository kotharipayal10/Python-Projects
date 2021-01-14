"""def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))"""

def insert_string(original_string, to_insert_string):
    #original_string = original_string.split()
    count = len(original_string)
    #print(count)
    length = int(count/2)
    #print(length)
    return original_string[:length] + to_insert_string + original_string[length:]

x = input("Enter a string: ")
y = input("Enter a string to be inserted: ")
print (insert_string(x,y))