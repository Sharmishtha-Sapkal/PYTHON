# Simple Python Problem: Even or Odd Checker

def check_even_odd(number):
    """Check if a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Example usage
if __name__ == "__main__":
    num = int(input("Enter a number to check if it is even or odd: "))
    result = check_even_odd(num)
    print(result)
