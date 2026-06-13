# q1 Take two numbers from user and print: sum, difference, product, quotient
num1=float(input("enter num1: "))
num2=float(input("enter num2: "))
print("sum=",num1+num2)
print("diff=",num1-num2)
print("product=",num1*num2)
print("qutient=",num1/num2)

#q2 # Take age from user and check: print type before and after conversion
age=input("enter age:")
print(type(age))
age=int(age)
print(type(age))

#q3 # Take two numbers: Print True if both are positive
num1=float(input("enter num1: "))
num2=float(input("enter num2: "))
print( num1>=0 and num2>=0)

#q4 # Take a number and check: even or odd 
num = int(input("enter a number: "))
result = ["odd", "even"]
print(result[num % 2 == 0])

#q5 # Take price and quantity from user Print total bill
price=float(input("enter price:"))
quantity=float(input("enter quantity:"))
total_bill=price*quantity
print("total=",total_bill)

#q6 Predict output before running:

print(not (5 > 3 and 2 < 1)) # will give true cause: 5>3 is T and 2<1 is F so output will be F but since not is there so output will be reversed