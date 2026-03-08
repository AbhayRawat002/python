#conditonal statements
#if-elif-else statements 
#syntax: 
# if(condition):
#     statement1
# elif(condition):
#     statement2
# else:
#     statement

#program to check if a person can vote or not 
age=int(input("enter your age:"))

if age < 0:
    print("invalid age")
elif age >= 18:
    print("you can vote")
else:
    print("you cannot vote")


#wap to check if a no is odd or even 
num=int(input("enter a number:"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")

#wap program to check the greatest of 3 numbers given by user
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
num3=int(input("enter number3:"))

if num1 >= num2 and num1 >= num3:
    print(num1, "is greatest")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is greatest")
else:
    print(num3, "is greatest")


#wap to check if a number is multiple of 7 or not 
num4=int(input("enter a number:"))
if(num4%7==0):
    print(num4,"is multiple of 7")
else:
    print(num4,"is not a multiple of 7")

#Given 3 numbers, print: second largest number
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
num3=int(input("enter number3:"))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    print("Second largest number is:", num1)

elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    print("Second largest number is:", num2)

elif (num3 > num1 and num3 < num2) or (num3 < num1 and num3 > num2):
    print("Second largest number is:", num3)

else:
    print("Cannot determine (numbers may be equal)")


#nesting
age =int(input("enter your age: "))
if age>=18 :
    if age>=80:
        print("cannot drive")
    else:
        print("can drive")
else:
        print("cannot drive")