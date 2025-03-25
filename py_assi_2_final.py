# Write a function to add n numbers
def add_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Sum:", add_numbers([10, 20, 30, 40, 50]))

# Write a function to take two parameters first is list second is int n e.g performAction(mylist,n)
def performAction(lst, n):
    print("in perform action")
    new_list = [] 
    separate_lists = []  
    for i in lst:
        new_list.append(i)  
        if i == n:  
            separate_lists.append(new_list.copy())  
            new_list = []  
    print("Separate lists when", n, "is found:", separate_lists)  

performAction([1, 2, 3, 1, 4, 5, 1, 2, 4, 5, 1], 1)
