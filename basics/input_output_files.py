''' python can be used to perform operations on a file(read or write data)
    types of files: i> text files:.txt, .docs, .log  etc...
                    ii> binary files:  .mp4, .mov, .png ect ect..  '''

'''open, read and close file
    open:
        f=open("file_name","mode")
        file_name is name of the file
        mode: r(read mode) or w(write mode)

    read:
        data=f.read()
    close:
        f.close()
        '''


# reading a file 
f = open("demo.txt","r")

# data=f.read()  # reads the entire file
# data=f.read(20)  # reads only first 20 chars of the file
# print(data)

line1=f.readline()
print(line1)

line2=f.readline()
print(line2)

f.close()


# writing a file 
# in write(w) or append(a) mode it creates the file automatcially in the folder 
f=open("sample.txt","w") # this will create sample.txt in the folder automatically when code is executed 


f = open("demo.txt","w") #this will over write the whole data i.e. replace the previous data with then new one 

f = open("demo.txt","a") #this will append new data with the previous data 

f.write(" hello")


f.close()

# ==========================================
# FILE MODES IN PYTHON (open() function)
# ==========================================

# Syntax:
# file = open("filename", "mode")


# ------------------------------
# 'r' → READ MODE (default)
# ------------------------------
# Opens file for reading only
# Error if file does NOT exist

# Example:
f = open("data.txt", "r")
content = f.read()
print(content)
f.close()


# ------------------------------
# 'w' → WRITE MODE
# ------------------------------
# Opens file for writing
# Creates file if it does not exist
# Deletes (overwrites) old content if file exists

# Example:
f = open("data.txt", "w")
f.write("Hello world")
f.close()


# ------------------------------
# 'x' → CREATE MODE
# ------------------------------
# Creates a new file and opens for writing
# Error if file already exists

# Example:
f = open("newfile.txt", "x")
f.write("New file created")
f.close()


# ------------------------------
# 'a' → APPEND MODE
# ------------------------------
# Adds data at the END of file
# Does NOT delete old content
# Creates file if it does not exist

# Example:
f = open("data.txt", "a")
f.write("\nThis is new line added")
f.close()


# ------------------------------
# 'b' → BINARY MODE
# ------------------------------
# Used for binary files (images, videos, etc.)
# Example modes: "rb", "wb"

# Example (reading image):
f = open("photo.jpg", "rb")
data = f.read()
f.close()


# ------------------------------
# 't' → TEXT MODE (default)
# ------------------------------
# Used for text files (normal reading/writing)
# Example: "rt", "wt"

# Example:
f = open("data.txt", "rt")
print(f.read())
f.close()


# ------------------------------
# '+' → READ AND WRITE MODE
# ------------------------------
# Allows both reading AND writing
# Used with other modes: r+, w+, a+

# Examples:

# r+ → read + write (file must exist)
f = open("data.txt", "r+")
print(f.read())
f.write("\nAdded using r+")
f.close()

# w+ → read + write but deletes old content
f = open("data.txt", "w+")
f.write("Fresh start")
f.close()

# a+ → read + append
f = open("data.txt", "a+")
f.write("\nAppending again")
f.close()


# ==========================================
# BEST PRACTICE (recommended)
# ==========================================
# Use "with" → automatically closes file

with open("data.txt", "r") as f:
    print(f.read())

# with syntax:
#   with open("demo.txt","a") as f:
#       data=f.read()

with open("demo.txt", "r") as f :
    data=f.read()
    print(data)
#with syntax automatically closes the file for us 

with open("demo.txt","w") as f:
    data=f.write("new data")  # "new data" will be overwritten in demo.txt file

#=======================================================================================================================

# deleting a file : done using a module (os module)
# module: (like a code library) is a file written by another programmer that generally has a function we can use.
# syntax: import os
#         os.remove("filename")

import os
os.remove("demo.txt") # deletes demo.txt from our system