def fun_yeld(lst: list = []):
    for i in lst:
        yield i

a = fun_yeld([3,32,3,3,2,3,3,4,234,24,23,423,4])

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

for i in a:
    print(i)

