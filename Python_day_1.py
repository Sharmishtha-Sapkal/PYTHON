import math

#reverse order of number
a=10
b=20
print("Original order : ",a,b)
temp = a
a = b
b = temp
print("Reverse order : ",a,b)


#Sum of Digits 
num = int(input("Enter a number a digit number : "))


digit = num%10
num1 = num//10
digit2 = num1%10
digit3=num1//10

print(digit,digit2,digit3)
sum = digit + digit2 + digit3
print("digit Sum is : ",sum)

#Even_Odd
num = int(input("Enter a number to find out even or odd : "))
if num % 2 ==0 :
    print("Number is even")
else :
    print("Number is odd !") 

#Grade Printing 

marks = int(input("Enter your marks : "))   
if marks>90:
    print("Grade A")

elif marks<=80 and marks>=70:
    print("Grade B")

elif marks<=70 and marks>=60:
    print("grade c ")   

else:
    print("Grade D")

#prime Number 

number = int(input("Enter a number to find out prime or not : "))
for i in range(2,int(math.sqrt(number)) + 1) :
    if number % i == 0 :
        print(number,"  is not a prime number")
        break
else:
        print(number, " is a prime number")    


#factorial Code
num = int(input("Enter a number to find out factorial : "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print("Factorial of",num,"is",fact)
