a = 0
while a < 10
    a += 1
    if a % 7 == 0 and a % 10 == 7:
        continue
    else:
        print(a)

