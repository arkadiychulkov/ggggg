def xz(x):
    c = 1
    while c <= x:
        yield c
        c += 1
f = xz(1333)
for i in range(200):
    print(f.__next__())
print(list(f))