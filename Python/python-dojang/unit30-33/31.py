def fib(num:int):
    a, b = 1, 0
    for i in range(num):
        a, b = b, a + b
    
    return b
    
n = int(input())
print(fib(n))