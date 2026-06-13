# Loops: are used to repeat instructions

# While Loop, Syntax :
# while (condition): 
#           instruction

#will print hello till counts value reaches 5
# in this code "count" is itrator and one cycle performed is called itration
count=1
while count<=5:
    print("hello", count)  
    count+= 1

print(count) #counts value will be 6 as the loop breaks/ends when count reach more than 5


#this code prints counting till 10
i=1
while i<=10: #python/compiler checks if "i" is less than 10 or euqal to 10 if yess it moves to next line, when value of i reach 11 program will end 
    print(i) # here it prints value of i 
    i+=1     #here value if i is increased by 1 or we can say 1 is added to current value of i


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




# Break: used to terminate the loop when encountered 
i=0
while i<=10:
    print(i)
    if(i==6):
        break
    i+=1

print("code ended")

# search for a number x in this tuple using loop
nums=(1,4,9,16,25,36,49,64,81,100)
x=100
i=0
while i<len(nums):
    if(nums[i]==x):
        print("number found at index",i)
        break
    else:  # this will be printed for each index in which number is not found
        print("finding")
    i+=1


# Continew: terminates execution in the current iteration and continew execution of the loop with next iteration 
i=0
while i<=5:
    if(i==3):
        i+=1
        continue # 3 will be skiped and then whole loop will execute 
    print(i)
    i+=1

i=0
while i<=10:
    if(i%2==0):
        i+=1
        continue #even numbers will be skiped
    print(i)
    i+=1

i=0
while i<=10:
    if(i%2!=0):
        i+=1
        continue #odd numbers will be skiped
    print(i)
    i+=1


