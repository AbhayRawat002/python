#lists:it is a built in datatype that stores set of values, it can store elements of diffrent type[int,float,str..etc]

marks=[23.3, 43.6, 98.0, 87.8,99.6]
print(marks)
print(type(marks))

#indexing in list(Same as string)
print(marks[0]) # will print first element 
print(marks[-1]) # will print last element 
print(marks[1:3]) # will print from index 1 to (3-1)
print(marks[1: ]) # will print from index 1 to end of list
print(marks[-4:-1]) # will print from -4 to -2(-1 is not included)
#length of list(same as stting)
print(len(marks))

#can store elements of diffrent datatypes
student=["abhay", 22, "doon", 7.73 ]
print(student)
#diffrence b/w list and string is strings cannot be changes but lists can
student[0]="abhay rawat"
print(student[0])

#list methods
list=[3,2,1,2,4]
print("before:",list)

list.append(5) # will add/inculde value given(5,can be anything else) at the end of the list
print("after:",list)

list.sort()
print("ascending:",list)

list.sort(reverse=True)
print("descending:",list)

list=[3,2,1,2,4]
list.reverse()
print("reversed list:",list)

#sorting works on strings too
list=['a','z','e','l']
list.sort()
print(list)

list=[3,2,1,2,4]
list.insert(2,10) #will add 10 at index 2
print(list)

list=[3,2,1,2,4]
list.remove(2) # will remove the value 2 which comes first i.e. 2 from index 1 is removed 
print(list)

list=[3,2,1,2,4]
list.pop(2) # will remove the element which is given inside()..in this case 1 is removed which is present at index 2 
print(list)

list=[3,2,1,2,4]
print(list.count(2)) #will tell how many times the value given is present in list i.e. tells how many 2s are their in list 



#Tuples: built in datatypes that lets us create immutable sequence of values
tup=(2,3,6,5)
print(type(tup))
print(tup)
print(tup[0]) # will print first element of tuple
print(tup[-1]) # will print last element of tuple
tup[1]=5 # this is not allowed/ assigning values or changing values is not allowed in tuples

tup=(1) # python will assume its an integer if we need tuple we should put a coma (1,) like this
print(tup)
print(type(tup))
tup=(1,) 
print(tup)
print(type(tup))

#slicing is same as list

#tuple methods
tup=(3,2,1,2,4)
print(tup.index(2)) # will tell the index of element 2 

print(tup.count(2)) # will tell the count of element 2 i.e. how many times 2 is present in tuple