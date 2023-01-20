def gen_fibonacci(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b

for number in gen_fibonacci(100):
    print(number)
    