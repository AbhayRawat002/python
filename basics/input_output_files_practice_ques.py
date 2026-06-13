# Create a file using python and add some data in it
with open("practice.txt","w") as f:
    f.write("hi everyone\nwe are learning\n")
    f.write("File i/o using java \ni like programming in java")


# write a function that repleces all occurence of java with python
def replace():
    with open("practice.txt","r") as f:
        data= f.read()

    new_data=data.replace("java","python")
    print(new_data)

    with open("practice.txt","w") as f:
        f.write(new_data)

replace()


# search if word "learning" exists in our file
def check_for_word():
    word=input("enter the word you wanna find: ")
    with open("practice.txt","r") as f:
        data= f.read()
        if (word in data):
            print("found")
        else:
            print("not found")
check_for_word()


# wap to find in which line does the word "learning " occur first, print -1 of word not found
def check_for_line():
    word = input("enter the word you wanna find: ")
    line_no = 1

    with open("practice.txt", "r") as f:
        while True:
            data = f.readline()
            if data == "":
                break   # end of file

            if word in data:
                print(line_no)
                return

            line_no += 1

    print(-1)

check_for_line()

