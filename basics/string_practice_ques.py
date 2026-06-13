# 1️⃣ Take a string from user and: print its length, print first character, print last character

s = input("Enter a string: ")

if len(s) == 0:
    print("Empty string")
else:
    print ("length of string:",len(s))
    print("First character:", s[0])
    print("Last character:", s[-1])



#2️⃣ Take first name and last name from user and:combine them into one string, print full name and its length

first_name=input("enter your first name:")
last_name=input("enter your last name:")

if len(first_name)==0 and len(last_name)==0:
    print("names cannot be empty")
else:
    print("name:",first_name+" "+last_name)
    print(len(first_name+" "+last_name))



#3️⃣ Check if a string ends with "ing" Print:"verb" if true and "not a verb" if false

s2=input("enter your word:")
if s2.endswith("ing"):
    print("verb")
else:
    print("not a verb")



#4️⃣ Take a string and check:if it contains the word "python" Print: "Python found" "Python not found"

s3=input("enter a string: ")
if len(s3)==0:
    print("string cannot be empty")
elif "python" in s3:
    print("python found")
else:
    print("python not found")



#5️⃣ Take a string and: replace all spaces with -
s4=input("enter a string: ")
if len(s4)==0:
    print("string cannot be empty")
else:
   print(s4.replace(" ","_"))



#6️⃣ Count number of vowels in a string If vowels ≥5: print "vowel rich" Else: print "low vowels"
s5=input("enter a string: ").lower()
vowle_count=(
    s5.count("a")+
    s5.count("e")+
    s5.count("i")+
    s5.count("u")+
    s5.count("o")
             )
print("number of vowles= ",vowle_count)
if vowle_count >= 5:
    print("vowel rich")
else:
    print("low vowels")



#7️⃣Take a word and: check if its first letter is uppercase
s6=input("enter a string: ")
if s6[0].isupper():
    print("first letter is uppercase")
else:
    print("not uppercase")



#8️⃣Username validation: Rules: length ≥5 ,must not contain spaces
username=input("enter a username: ")
if len(username)>=5 and " " not in username:
    print("valid username")
else:
    print("invalid username")


# Given a string: print the middle character (if length is even, print middle two)
s7=input("enter a string: ")
total_characters= len(s7)
# print(total_characters)
middle_character= total_characters//2
if total_characters%2==0:
    print(s7[middle_character-1]+s7[middle_character])
else:
    print(s7[middle_character])



#Take a sentence and: find first occurrence of "a" if not found, print "not present"
s8 = input("enter a string: ")

index = s8.find('a')

if index == -1:
    print("not present")
else:
    print("first occurrence of 'a' is at index:", index)
