# Recursion: when a function calls itself repeatedly.
def show(n):  # this function is like loop it will check if n is equal to 0 if not it will print n then decrement n i.e. (n-1) then again repeat till n==0 when n becomes 0 then it returns 
    if(n==0):  # this is called base case its needed to stop the code or it will go into infinite loop, it is the stoping condtion of the program
        return
    print(n)
    show(n-1)
    print("end")  # this will be printed n times(5times in this case),when n becomes 0 it prints end for n=1 then n=2 then n=3...like this till n=5
show(5)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))

# write a recursive function to calculate the sum of first n numbers 
def sum_n(n):
    if(n==1):
        return 1
    else:
        return n+sum_n(n-1)
print(sum_n(3))

# write a recursive function to print all elememts in a list 
def print_list(list,indx=0):
    if(indx==len(list)):
        return
    print(list[indx])
    print_list(list,indx+1)

lst=[1,2,3,4]
print_list(lst)