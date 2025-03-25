xcase = int(input("Enter Your Choice"))
def python_switch(case):
    
    match case:
        case 1:
            n = 20
            if(n>18):
                print("You are an adult")
            else:
                print("You are not an adult")

        case 2:
            print("you are wishing to print factorial of a number")
            num = int(input("Enter a number: "))
            factorial = 1
            for i in range(1, num + 1):
                factorial *= i
            print("Factorial of", num, "is", factorial)
            
        case _:
            print("Enter valid choice")
python_switch(case) 