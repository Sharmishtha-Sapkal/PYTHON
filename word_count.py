input_string = "Hello my name is sharmishtha. I am currently living in pune and I am from karad"
print(input_string)

# Split the string into words
words = input_string.split()

print(words)
print(words[0])

words_frequency = {}

for word in words:
    if word in words_frequency:
        words_frequency[word] += 1
    else:
        words_frequency[word] = 1

for word, frequency in words_frequency.items() :
    print(f"{word} : {words_frequency}")        

          
