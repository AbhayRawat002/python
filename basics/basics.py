# Datatypes:
#    integers: {-1,0,1} 
#    string : contains alphabets/words/sentences {"hello" "jlsadfbvn"}
#    float : decimal values {2.3,1.5}
#    boolean : True(1) and False(0)
#    none: this tells no value is assignes to variable 

age=22
name="Abhay"
grade=7.73
Male=True
a=None

print(type(age))
print(type(name))
print(type(grade))
print(type(Male))
print(type(a))

#keywords:reserved words in python, like- and,or,is,True etc..
#keywords cannot be used as identifiers(name of variable)

num1=2
num2=8
sum=num1+num2
print(sum)

#operators: symbols that perform certain operations, ex- (+, - , * , %)
#   arithmetic operators: + , - , * , /, etc..(used to perform mathematical operations)
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b) # will give solution in bool
print(a%b) # used to find remainder 
print(a**b) # will give power of a to b(a^b)


#   relational operators: = , > , < , != , <= , == (used to compare values)
print(a==b) # will give False caus it checks if a is equal to b
print(a!=b) # will give True caus it checks if a is not equal to b
print(a>=b) # will give True caus it checks if a is greater than and equal to b
print(a<=b) # will give False caus it checks if a is less than and equal to b
print(a>b)  # will give True caus it checks if a is greater than b



#   assignment operators: = , += ,-= , **= etc..(used to assign values)
num=10 #  " = " is used to assign value i.e. value of num is 10
num=num+10 # adds 10 to previous value
num+=10 #does same as above statement 
print("num: ", num)

num-=10 # subtracts 10 from num
print("num: ", num)
num*=5 # mnultiply 5 to num
print("num: ", num)
num/=2  # divide num by 10
print("num: ", num)
num**=10  
print("num: ", num)
num%=10 
print("num: ", num)



#   logical operators: not , and , or 
# not returns the opposite of the starment ... works on only one value/statement 
print(not False) # will print true as not of false is true
print(not True) # will print false as not of true is false

# and operator works on 2 values
a=2
b=3
print("or operators:", (a>b) and (a<b)) # will give true when all values/statements are true



# or operator works on 2 values
a=2
b=3
print("or operators:", (a>b) or (a<b)) # will give true even if one statement is true doesnt matter if other one is false


# type conversion(done automatically by python) and type casting(needed to do manually): syntax= datatype(identifier)


a=2 #int value
b=2.5 #float value
sum=a+b # when int and float are added then it will convert int into float automatically  i.e. 2.0=2.5 is done
print(sum) # and output printed will be float too

a= int("2") #string or a=int("2")
b=2.5 #float value
# if we want to add a and b we need to convert a into float/int so addtion/mathematical operations can be performed 

print(type(a))
print(sum) # and output printed will be float too

#float/int to string
a=3.14
a=str(a)
print(type(a))

#input from user
name=input("enter your name:")  #input by default returns every input as string even if we enter input as int or float untill datatype is not mentioned
print(name)
print(type(name))
# if we want that it returns diffrent datatype then we tell it like this:
age=int(input("enter your age:"))
print(age)
print(type(age))


#wap to input side of a square and print its area
side=float(input("enter the value of side: "))
print("area = ",side*side)

#wap to give avg of 2 floating point no.s
num1=float(input("enter the value of num1:"))
num2=float(input("enter the value of num2:"))

avg=(num1+num2)/2
print("avg=",avg)