def xz():
    s = input("do you want to DO coordinate graphik: yes or no ")
    while True:
        if s == "yes":
            x = int(input("vertical high"))
            c = 1
            while c <= x:
                yield c
                c += 1
            break
        else:
                print("go away I.F.Y.M.B.D.F.G.H.A")
                continue
f = xz()
for i in range(int(input("horizontal high"))):
    print(f.__next__())
print(list(f))