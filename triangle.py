#triangle pattern
def triangle(n):
    for i in range(1,n):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
triangle(5)  

#print ABC 
print("triangle ABC pattern")
def triangle_ABC(n):
    for i in range(1,n):
        for j in range(1,i+1):
            print(chr(65+j-1),end=" ")
        print()

triangle_ABC(5)
