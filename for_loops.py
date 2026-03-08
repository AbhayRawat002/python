# For loops: used for sequential traversal, for traversing lits,tuples,strings etc..

nums=[1,2,3,4]
for val in nums:
    print(val)  # will print each element of the list

name=input("enter a string:")
print("characters of the string: ") 
for char in name:
    print(char)  # will print each character of the string 

    
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
# range() - Range function :it returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and stops before a specific number

#syntax: range(start?,stop,step?) - start from(this value is optional, by default it will start from 0), stop(this value is needed to tell where to stop), step(this one is optional too it tells how many steps will it increment if not mentioned it will be 1 by default)


for el in range(5):  # range(stop)
    print(el)  

for el in range(1,11):  # range(start,stop)
    print(el)  

for el in range(1,11,2):  # range(start,stop,step) will start from 1 go till (11-1) and increment by 2
    print(el)  


# pass statement: pass is a null statement that does nothing, it is used as placeholder for future code 
for i in range(5):
    pass 
print("some usefull work")


