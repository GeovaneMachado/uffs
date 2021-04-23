a = [1, 1, 2, 3, 5, 6, 6, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for j in b:
        if i == j:
            if c.count(j) >= 1:
                pass
            else:
                c.append(j)
print(c)