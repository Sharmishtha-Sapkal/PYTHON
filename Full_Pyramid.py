def full_pyramid(n):
    for i in range(n+1):
        for j in range(n-i):
            print(" ", end=" ") 
        # print()
        for k in range(1, 2*i):
            print(".", end=" ")
        print()    


full_pyramid(5)            