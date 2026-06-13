# Q1️⃣ Take a list of numbers and print: sum and avg

lst=[2,3,1,7]
total= sum(lst)
avg= total/len(lst)
print("sum=",total)
print("avg=", avg)

#Q2 wap to ask user their 3 fav movies and store them in list
movies=[]
movies.append(input("enter 1st movie:"))
movies.append(input("enter 2nd movie:"))
movies.append(input("enter 3rd movie:"))

print(movies)

#Q3 wap to check if a list contains palindrome of elements.
lst = [1, 2, 3, 2, 1]

rev_lst = lst.copy()
rev_lst.reverse()

if lst == rev_lst:
    print("palindrome is present")
else:
    print("palindrome not present")

#Q4 wap to count the number of students with "A" grade in a tuple

grades=("A", "C" ,"A", "B", "D", "C","A", "C","D")
print(grades.count("A"))

#Q5 Store the above values in list and sort that list from A->D 
grade_lst=list(grades)
grade_lst.sort()
print(grade_lst)

#Q6 Find max & min in a list (NO max() / min())
lst = [5, 2, 9, 1, 7]

minnum = lst[0]
maxnum = lst[0]

for num in lst:
    if num > maxnum:
        maxnum = num
    if num < minnum:
        minnum = num

print("Maximum:", maxnum)
print("Minimum:", minnum)
