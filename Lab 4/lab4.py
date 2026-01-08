def myTest():
    yield 1
    yield 5
    yield 6
    yield 99

a = myTest()
b = myTest()

print( a.__next__())
print( a.__next__())

print(b.__next__())
print(b.__next__())

print(a.__next__())


print("""Lab Task""")

def fibonacci(maxNo):
    x, y = 0, 1
    while y < maxNo:
        yield y
        x, y = y, x+y

for i in fibonacci(1000000):
    print(" ",i)