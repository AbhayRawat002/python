# Print elements of a list using for loop
lst=[1,4,9,16,25,36,49,64,81,100]
for el in lst:
    print(el)


# Search for a number x in this tuple using for loop
nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("tell the element u wanna find: "))
indx=0
for el in nums:
    if (el==x):
        print("number found at indx:",indx)
    indx+=1

# using for and range(): 1>print 1-100, 2>print 100-1, 3> print multiplication table of any number n
#1
for i in range(1,101):
    print(i)

#2
for i in range(100,0,-1):
    print(i)

#3
num=int(input("enter a number: "))
for i in range(1,11):
    print(i*num)

# wap to find the factorial of first n numbers using for
n=int(input("enter a number: "))
sum=0
i=1
    
for i in range (1,n+1):
    sum=sum+i

print(sum)

#Count how many elements are in this list:
lst = [10, 20, 30, 40, 50]

count = 0
for el in lst:
    count += 1

print("Number of elements:", count)


#Count how many times 2 appears:
lst = [1,2,3,2,4,2,5]

count=0
indx=0
for el in lst:
    indx+=1
    if(el==2):
        print("2 found at index:",indx)


#Check if a number exists in a list: If found → print "Found", Else → print "Not Found"
n = int(input("enter a number: "))
lst = [10, 20, 30, 40, 50]

for el in lst:
    if n == el:
        print("Found")
        break
else:
    print("Not Found")


# Count how many even numbers are in a list.
lst=[1,4,9,16,25,36,49,64,81,100]
n=[]
for i in lst:
    if(i%2==0):
        n.append(i)

print("numbers of even number in list=",len(n))
#or
lst=[1,4,9,16,25,36,49,64,81,100]
n=0
for i in lst:
    if(i%2==0):
        n+=1

print("numbers of even number in list=",n)


# Find the largest element in a list (no max()).
lst=[1,4,9,16,25,36,49,64,81,100]

largest_num=lst[0]

for i in lst:
    if(i>largest_num):
        largest_num=i

print("largest element in the list is: ", largest_num)



# Reverse a list using a loop.

lst=[1,4,9,16,25,36,49,64,81,100]
rev = []

for el in lst:
    rev.insert(0, el)

print(rev)

#or

lst = [1, 2, 3, 4, 5]
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print(rev)


#Create a new list containing only numbers > 10.
lst=[1,4,9,16,25,36,49,64,81,100]
new_lst = []
for el in lst:
    if(el>=10):
        new_lst.append(el)
print(new_lst)


# Count how many vowels are in a tuple of characters.
chars = ('p', 'y', 't', 'h', 'o', 'n', 'a', 'e', 'i')

count = 0
vowels = ('a', 'e', 'i', 'o', 'u')

for ch in chars:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)


# Check if a number is prime.
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
