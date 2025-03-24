# Write a program to swap 2 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping: a =", a, ", b =", b)

temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b)

#Write a program to calaculate sum of digits of given three digit number

num = int(input("Enter a three-digit number: "))


digit1 = num // 100       
digit2 = (num // 10) % 10 
digit3 = num % 10         

sum_of_digits = digit1 + digit2 + digit3

print("Sum of digits:", sum_of_digits)

#Find if given number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

#Print grade of student based on his marks 
marks = int(input("Enter the student's marks: "))

if marks >= 75:
    print("DISTINCTION")
elif marks >= 60:
    print("FIRST CLASS")
elif marks >= 50:
    print("SECOND CLASS")
elif marks >= 40:
    print("PASS CLASS")
else:
    print("FAIL")

#Calculate factorial of number
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "is", factorial)

#Find if given number is prime or not
num = int(input("Enter a number: "))

i = 2
while i < num and num % i != 0:
    i += 1

print("Prime number" if num > 1 and i == num else "Not a prime number")

#Write a program to reverse a list
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)

#Write a program to add all even elements in list from 1 to 100

even_numbers = list(range(2, 101, 2))
sum_even = sum(even_numbers)
print("Sum of even numbers from 1 to 100 is", sum_even)

#Write a program to print all odd numbers from list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in my_list if num % 2 != 0]
print("Odd numbers:", odd_numbers)

#Write a pogram to create a list of prime numbers from 2 to 100
prime_numbers = []

for num in range(2, 101): 
    is_prime = True
    for i in range(2, num): 
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print("Prime numbers from 2 to 100:", prime_numbers)

#Remove duplicate elements from list
my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list = []

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("Unique List:", unique_list)

#From given list of strings create another list of strings having 2 or more vowels
Students = ["Amrish", "aachal", "Ashutosh", "Shital", "Ravina", "arav","bag"]
def at_least_two_vowels(Students):
    student_with_two_vowels = []
    for i in Students:
        vowels = ["a", "e", "o", "i", "u"]
        count = 0
        for j in i:
            if j.lower() in vowels:
                count += 1
                if count >= 2:
                    student_with_two_vowels.append(i)
    return student_with_two_vowels

two_vowels = at_least_two_vowels(Students)
print(two_vowels)

#Find out total count of prime numbers and odd numbers in given tuple
numbers = (3, 7, 10, 15, 19, 23, 30, 35, 40, 41)

prime_count = sum(1 for n in numbers if all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)) and n > 1)
odd_count = sum(1 for n in numbers if n % 2 != 0)

print("Total Prime Numbers:", prime_count)
print("Total Odd Numbers:", odd_count)

#Write a program to reverse given string.
string = input("Enter a string: ")

reversed_string = string[::-1]

print("Reversed String:", reversed_string)

#Write a program to find if given string is pangram (it should have all characters from a to z)
import string
def is_pangram(s):
    alphabet = set(string.ascii_lowercase) 
    return set(s.lower()) >= alphabet       

s = input("Enter a string: ")

if is_pangram(s):
    print("The string is a pangram.")
else:
    print("The string is NOT a pangram.")


#Write a program to find if given string is anagram
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2) 

# Input strings
str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()

# Check and print result
if is_anagram(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are NOT anagrams.")

#Change the case of each vowel in given string 
def swap_vowel_case(s):
    vowels = "aeiouAEIOU"
    return "".join(char.swapcase() if char in vowels else char for char in s)

string = input("Enter a string: ")

print("Modified String:", swap_vowel_case(string))

#Reverse every word in given sentence
def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split())

sentence = input("Enter a sentence: ")

print("Modified Sentence:", reverse_words(sentence))

#Caesar cipher
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y',
'm':'z', 'n':'a','o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 
'A':'N', 'B':'O', 'C':'P', 'D':'Q','E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 
'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

def rot13(text):
    return "".join(key.get(char, char) for char in text)  # Replace using the dictionary

message = input("Enter a message: ")
result = rot13(message)
print("ROT-13 Output:", result)


