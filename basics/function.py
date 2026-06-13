# Functions: block of statements that perform specific task 

def sum_numbers(a, b): #this line defines the function, a and b are the parameters of the function i.e. we perform some action on these parameters only. we can give more parameters a,b,c,d...
    result = a + b
    return result


sum(10,2)  #this is calling a function 10 and 2 are the arguments or values we pass to the function and are stored in parameters , we can also call this function multiple times with diffrent 

sum(2,3)


# creat a function that gives avg of 3 values
def avg(a,b,c):
    avg=(a+b+c)/3
    print(avg)
    return avg
 
avg(2,4,6)
avg(12,24,36)


# Types: a> built-in functions (ex: print(),len(),range() ect..) and b> user defined :
print("abhay","rawat") #sep=" " automatically puts space b/w 2 arguments and its pre-defined 
print("abhay")   #end="\n" next statement will be printed in next line 
print ("rawat")

print("Abhay",end=" ") # now output will not end with new line but with space
print("Rawat")
print("hello","world", sep="$")  # now their will be '$' sign b/w 2 agruments.. will print hello$world


#defult parameters: assigning a defult value to parameters, which is used when no argument is passed.

def product(a,b):
    print(a*b)
    return a*b

product() # as their are no defult values are assigned to parameters this will throw an error that 2 arguments are missing, to avoid this error we give defult values that run when no arguments are passed by user 


def product(a=1,b=1):  # now if we dont pass any arguments it will do 1*1 
    print(a*b)
    return a*b
product()


def product(a,b=1):  
    print(a*b)
    return a*b
product(3)


