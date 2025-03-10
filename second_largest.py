#Write a Python program that takes a list of numbers as input 
# and returns the second largest number in the list.

my_set = {}

if(len(my_set)==0):
    print("set is empty")

elif((my_set)<2):
    print("their is no second value")
    
else:
    maximum = max(my_set)
    print("first max value :", maximum)
    my_set.remove(maximum)

    #print(my_set)
    second_max = max(my_set)
    print("second max value :", second_max)
