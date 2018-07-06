# Fibonacci 1,1,2,3,5,8,13
# n + n+n +
# a = 1, b = 1, a = a + b

def fib(n):
    a, b = 0,1
    while a < n:
        print(a)
        a, b = b, a+b
    print()

fib(1000)