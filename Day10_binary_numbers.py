n = int(input())

bi = []
# prev = 0
c_m = 0
c = 0
while n > 0:
    if n % 2 == 0:
        bi.append(0)
        c_m = max(c, c_m)
        c = 0
    else:
        bi.append(1)
        c += 1
    n = n//2
print(max(c, c_m))

