# #strings 
# strg1="hello "
# len1=len(strg1)  #counts hello and that space therefore 6 output 
# print(len1)

# strg2="world"
# len2=len(strg2)
# print(len2)
# print(strg1+strg2) # concatination 

# #other way to concatinate
# strg1="hello "
# len1=len(strg1)  #counts hello and that space therefore 6 output 
# print(len1)

# strg2="world"
# len2=len(strg2)
# print(len2)
# final_strg=strg1+" "+strg2
# print(final_strg)
# print(len(final_strg))

#indexing (each charachter in string gets a position)
#example:
# h e l l o w
# 0 1 2 3 4 5 

str1="Abhay Rawat"
# ch1=str[0]
# print(ch1)  OR
print(str1[8])

#slicing 
#syntax:  str[starting_index:ending_index]
str2="ABHAY SINGH RAWAT"
print(str2[2:5]) # prints a perticular part 
print(str2[:5]) # prints from zero till asked 
print(str2[0:]) # prints whole len of string
#diffrent functions in slicing 
str3="my name is abhay rawat"
print(str3.endswith("at"))  #checks if string ends with a particular string give true/false as output (will give true)
print(str3.endswith("dy"))  #checks if string ends with a particular string give true/false as output (will give false)
str3=str3.capitalize() # string will start will capital latter 
print(str3) 

#replace function syntax: str.replace(old,new)

str4="oops"
print(str4.replace("o","a")) # we can replace not just characters but a whole string too

str5="im abhay"
print(str5.replace("abhay","jhon"))

#find function: syntax: str.find(word) # it returns 1st index of first occurence 
str6="hello world"
print(str6.find("o"))

#count function: syntax: str.count("xy") : counts the occurence of string
str7="abhay"
print(str7.count('a')) #output will be 2 as a comes 2 times

#Email validation using in
email=input("enter your email:")
if "@gmail.com" in email:
    print("valid email")
else:
    print("invalid email")


#Password strength using len()
password=input("enter password:")
if len(password)>=8:
    print("strong password")
else:
    print("weak password")

#: Check if name contains only letters
name=input("enter your name:")
if name.isalpha():
    print(f"welcome {name}")
else:
    print("invalid name")