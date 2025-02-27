def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)

print(fact(4))

def fib(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(6))
# 0 1 1 2 3 5 