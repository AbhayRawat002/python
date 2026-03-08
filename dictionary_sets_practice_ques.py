# Q1 wap to enter marks of 3 subs from user and store them in a dict. start with an empty set abd add one by one. use subbject  as keys and marks as values
marks={}

x=int(input("enter marks of physic:"))
marks.update({"physic":x})

y=int(input("enter marks of chem:"))
marks.update({"chem":y})

z=int(input("enter marks of maths:"))
marks.update({"maths":z})

print(marks)

#Q2 Figure out a way to store 9 and 9.0 as separate vales in set
s1={("float",9.0),("int",9)}

print(s1)

#Q3 Create a dictionary to store:name, age, city. Then: print only the values, update the city, add a new key "course"
d1 = {
    "name": "abhay",
    "age": 22,
    "city": "doon"
}

print(d1.values())

d1["city"] = "delhi"
d1["course"] = "python"

print(d1)

#Q4 in the given dictionary Print: physics marks, total number of subjects, add "english": 88 inside marks
student = {
    "name": "Rahul",
    "marks": {
        "maths": 78,
        "physics": 85,
        "chemistry": 69
    }
}
print(student["marks"]["physics"]) 
print(len(student["marks"]))
student["marks"]["english"] = 88

print(student)

#Q5 Create an empty dictionary. Take input for: subject name, marks and Add 3 subjects manually (no loop).
dic={}

sub1=input("enter subject1:")
marks1=int(input("enter marks of subject1:"))
dic[sub1]=marks1

sub2=input("enter subject2:")
marks2=int(input("enter marks of subject2:"))
dic[sub2]=marks2

sub3=input("enter subject3:")
marks3=int(input("enter marks of subject3:"))
dic[sub3]=marks3

print((dic))

#Q6 for the given dictinoary  Print all keys as a list, Print all key–value pairs, Check if key "d" exists (use get())
info = {"a": 10, "b": 20, "c": 30}
print(list(info.keys()))
print(info)
print(info.get("d"))

#Q7 Given a dictionary: Increase price of each item by 2 manuall, Print updated dictionary
prices = {"pen": 10, "pencil": 5, "eraser": 7}

prices["pen"] = prices["pen"] + 2
prices["pencil"] = prices["pencil"] + 2
prices["eraser"] = prices["eraser"] + 2

print(prices)

