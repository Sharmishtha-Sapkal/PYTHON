for i in range (1,31):
    first = i % 7 
    second = i % 7
    third = i % 7
    fifth = i % 7
    sixth = i % 7
    seventh = i % 7
    if first==1:
       print(i,"Monday")
    elif second == 2:
        print(i,"Tuesday")
    elif third == 3:
        print(i,"Wednesday")
    elif fifth == 4:
        print(i,"Thursday")
    elif sixth == 5:
        print(i,"Friday")
    elif seventh == 6:
        print(i,"Saturday")
    else:
        print(i,"Sunday")

#word occurance

word = "Python is a fun language to learn"
words = word.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

#Anagram
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram('listen', 'silent'))


#snake_case To CamelCase conversion

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
print(snake_to_camel('snake_case_to_camel_case'))

   



