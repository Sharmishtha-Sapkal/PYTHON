def pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print asterisks
        for j in range(1, 2 * i):
            print("*", end="")
        # Move to the next line after each level
        print()


pyramid(5)
