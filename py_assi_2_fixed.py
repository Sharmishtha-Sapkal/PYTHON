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
    for i in range(len(lst)):
        new_list.append(lst[i])  
        if (i + 1) % n == 0:  
            print("New list after adding", lst[i], ":", new_list)  
            new_list = []  

# Example usage
performAction([1, 2, 3, 4, 5, 12, 1, 2, 4, 5, 1], 3)
