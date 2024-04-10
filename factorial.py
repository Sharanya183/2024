def fac(n):
    if n == 0:
        return 1
    else:
        return n*(fac(n-1))
#user input#
n=int(input("enter a non-negative integer"))
print("factorial of "+ n+ "is "+ fac(n))
