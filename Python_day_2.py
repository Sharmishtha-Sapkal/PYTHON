#list of all odd numbers

for i in range (1,101,2):
    print (i)

#prime number code in range 1-100


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
primes = [num for num in range(1, 101) if is_prime(num)]
print("Prime numbers between 1 and 100:", primes)

#swap last two digits 
def swap_last_two_digits(num):
    last_two_digits = num % 100
    first_two_digits = num // 100
    swapped_num = (first_two_digits * 100) + (last_two_digits % 10)
    return swapped_num

# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input from the user
num = int(input("Enter a number: "))

# Function call and output
print(f"Factorial of {num} is {factorial(num)}")


#reverse 
text = input("Enter a string: ")

# Reverse the string using reversed() function
reversed_text = "".join(reversed(text))

# Output the result
print("Reversed string:", reversed_text)