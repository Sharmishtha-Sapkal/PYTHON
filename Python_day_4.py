from functools import reduce  # Import reduce from functools
x = ["hello", "I", "am", "Sharmishtha"]

#greater than n lenght
def greater_no(n):
    greater_no_list = []
    for i in x :
        if len(i)>n:
            greater_no_list.append(i)
    return greater_no_list

print(greater_no(2))

def square(a):
    return a*a


numbers = [1,2,3,4,5]
# map 
x = map(square, numbers)

for i in x :
    print(i)

#we can use 2 iterator in map 
# 3 separate lists using map function on 1 list 

even_number = [2,4,6,8,10]
odd_number = [1,3,5,7,9]

x = list(map(lambda a, b : a+b, even_number, odd_number))
print(x)


num = [1,2,3,4,5,6,7,8,9,10]
x = list(map(lambda a : a%2==0, num))
print(x)

five_multiples = list(map(lambda a : a%5 == 0, num))
print(five_multiples)

#filter
fruits = ["apple", "banana", "orange", "gauva", "resins", "water Melon", "papaya"]
vowels = ["a", "e", "i", "o", "u"]

def start_with_vowel(word):
    return word[0].lower() in vowels


x = list(filter(start_with_vowel, fruits))
print(x)

# Reduce

def add(a,b):
    return a + b

x = reduce(add, num)
print(x)

#find Common elements 
a = [1,2,3,4,5]
b = [4,5,6,7,8]
common = []

def find_common(a):
    for i in a:
        for j in b:
            if a[i] == b[j]:
                common.append(a[i])
    return common

new_list = list(filter(find_common,a))          

