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
    new_list = []  # Initialize new_list to store elements
    for i in range(len(lst)): 
        new_list.append(lst[i])  # Append the current element to new_list
        if (i + 1) % n == 0:  # Check if the current index + 1 is a multiple of n
            print("New list after adding", lst[i], ":", new_list)  # Print the current state of new_list
            new_list = []  # Reset new_list after printing

        
        if i == n:  # Check if the current element is equal to n
            second_list.append(i)  # Append to second_list if it matches
            print("Occurrences of", n, "in the list:", second_list)  # Print the second_list


        # if n in lst:
        #     second_list = [i for i in lst if i == n]  # Create a list of elements equal to n
        #     print(second_list)  # This will print the elements that match n

performAction([1, 2, 3, 4, 5, 12, 1, 2, 4, 5, 1], 1)
