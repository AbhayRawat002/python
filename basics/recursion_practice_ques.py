#1️⃣ Print numbers from 1 to n using recursion
def nums(n):
    if(n==0):
        return
    nums(n-1)
    print(n)
nums(5)


#2️⃣ Print numbers from n to 1 using recursion
def nums(n):
    if(n==0):
        return
    print(n)
    nums(n-1)
nums(5)


#3️⃣ Calculate sum of even numbers from 1 to n
def even_sum(n):
    if n == 0:
        return 0
    
    if n % 2 == 0:
        return n + even_sum(n-1)
    else:
        return even_sum(n-1)

print(even_sum(5))


# 4️⃣ Factorial of n
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(5))


# 5️⃣ Count digits of a number