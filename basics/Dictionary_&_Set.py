#Dictionary: used to store data values in key:value pair

info={
    "Name":"Abhay", 
    "Age": 18,
    "CGPA": 7.73,
    "Grades": ['A','A','B','C'],
    "Subjects":("Cpp","Python", "java")
}

print(info)
print(type(info))
print(info["Age"])
print(type(info["Subjects"]))
info["Age"]=22 # age will be updated 
info["Address"]= "Dehradun" # new key named address will be added to dict 
print(info)

null_dict={}
null_dict["name"]="abhay"
print(null_dict)

#nested dictionary
student={
    "name":"Abhay",
    "subjects_marks":{
        "chem":78,
        "physics":84,
        "maths":56
    }
}
print(student) #prints whole dictionary 
print(student["subjects_marks"]) #prints nested dict 
print(student["subjects_marks"]["maths"]) #prints the elemnents of the suject_marks dict


# Dictionary methods 
info={
    "Name":"Abhay", 
    "Age": 18,
    "CGPA": 7.73,
    "Grades": ['A','A','B','C'],
    "Subjects":("Cpp","Python", "java")
}

print(info.keys()) #will print all keys present in info dictionary
print(info.values()) #will print all values present in info dictionary
print(len(info.keys())) #will tell all the keys present in dictionary 
print(list(info.keys())) #will typecast dict into list
print(info.items()) #will return key:value pair as tuple
print(info.get("Name")) #will return key according to value

new_dict={"address":"doon",18:18}
info.update(new_dict) #will add new dictionary or key:values to info dict
print(info)

# set: is a built-in data type that stores: Unique values only (no duplicates), Unordered collection, Mutable (you can add/remove items) *impo-sets are mutable but the values/elements present in set are immutable i.e. we can add or remove elements but cannot change values of those elements 

collection={1,2,3}
print(type(collection))
print(collection)

collection={1,2,2,3,"hello"} # will ignore repeated elements
print(len(collection)) #will tell total no of elements repeated ones not included
print(collection)

collection={} # this is empty dictionary not empty set
print(type(collection))

collection=set() # this is syntax for empty set
print(type(collection))

#set methods 
collection=set() 
collection.add(1) #add method: add an element to set
collection.add(2)
# collection.add("abhay") #we can add strings too
# collection.add((1,2,3)) # we can add tuple too
# # collection.add([1,2,3]) # we cannot add list..this will give error

# collection.add(2) # will ignore this one caus 2 is already added
# collection.remove(2) #remove method: removes the element from set
collection.pop() # this pops random elements
# collection.clear() #this will remove all elements from set
print(collection)

set1={1,2,3}
set2={1,2,4,5}
print(set1.union(set2)) #will make a new set with elements of both sets(not incude repeated elements)
print(set1) #their will be no change in set1 and 2
print(set2)

set1={1,2,3}
set2={1,2,4,5}
print(set1.intersection(set2)) # will make a new set with common values/elements