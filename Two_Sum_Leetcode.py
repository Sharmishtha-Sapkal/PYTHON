num = list(map(int, input("Enter an array: ").split()))
target = int(input("Enter your Target: "))

pairs = []

for i in range(len(num)):  
    for j in range(i + 1, len(num)):  
        if num[i] + num[j] == target:
            pairs.append((i, j))

if pairs:
    for pair in pairs:
        print(f"Pair found: {pair}")
else:
    print("No pair found")
