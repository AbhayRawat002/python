# wap to print the length of a list.(list is the parameter)
def length_list(lst):
    print("List:", lst)
    print("Length:", len(lst))

length_list([4,2])


# wap to print the content of a list in same line.

def list_items(lst):
    for i in lst:
        print(i,end=" ")

list_items(["acba","asdfja","sdfha"])



#wap to print the factorial of n.(n is parameter)
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("factorial of",n,"=",fact)
factorial(5)

# Wap to function to print if a num is odd or even 
def checker(num):
    if (num%2==0):
        print(num,"is a even number")
    else:
        print(num,"is odd number")
    return num

checker(num=int(input("enter a number: ")))

# Create a program that: Takes student name, Takes marks of 3 subjects, Calculates total, Calculates average, Assigns grade, Prints full report, everything must be done using functions

def marks():
    sub1 = float(input("Enter marks of subject 1: "))
    sub2 = float(input("Enter marks of subject 2: "))
    sub3 = float(input("Enter marks of subject 3: "))
    return sub1, sub2, sub3


def calc_total(sub1, sub2, sub3):
    return sub1 + sub2 + sub3


def calc_avg(total):
    return total / 3


def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    elif avg >= 40:
        return "E"
    else:
        return "Fail"


def report():
    name = input("Enter student name: ")

    s1, s2, s3 = marks()
    total = calc_total(s1, s2, s3)
    avg = calc_avg(total)
    g = grade(avg)

    print("\n----- REPORT CARD -----")
    print("Name:", name)
    print("Total:", total)
    print("Average:", avg)
    print("Grade:", g)


report()
