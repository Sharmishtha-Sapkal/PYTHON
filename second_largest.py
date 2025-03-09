#Write a Python program that takes a list of numbers as input 
# and returns the second largest number in the list.

my_set = {10, 20, 30}
maximum = max(my_set)
print("first max value :", maximum)
my_set.remove(maximum)

#print(my_set)
second_max = max(my_set)
print("second max value :", second_max)

    