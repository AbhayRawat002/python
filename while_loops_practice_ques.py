# wap to print table of a number 
num=int(input("enter a number: "))
count=1
while count<=10:
    print(num,"X", count, "=", num*count)
    count+=1


#wap to Print numbers from 10 to 1
count=10
while count>=1:
    print(count)
    count-=1

# Print all even numbers between 1 and 20
count=1
while count<=20:
    if (count%2==0):
        print(count)

    count+=1


# Print the square of numbers from 1 to 5
count=1
while count<6:
    print(count,"^2","=",count*count)
    count+=1

# Take a number from user and print its factorial
num=int(input("enter a number:"))
fact=1
count=1
while count<=num:
    fact=fact*count
    count+=1 

print(f"{num}!={fact}")
#or
num = int(input("enter a number: "))
fact = 1

while num >= 1:
    fact = fact * num
    num -= 1

print("factorial =", fact)


# print the elements of a list using loop
nums=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<(len(nums)):
    print(nums[i])
    i+=1


# Print the sum of first n natural numbers
n=int(input("enter a number: "))
sum=0
count=0
while count<=n:
    sum=sum+count
    count+=1
print("sum of",n,"number=",sum)