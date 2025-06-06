q = int(input())
e = []

for i in range(q):
    x, y = list(map(int, input().split()))
    e.append([x, y])


for t in e:
    x = t[0]
    y = t[1]

    if x >= 0 and y <= 0:
        print(x, 0, -y)

    elif x >= 0 and y > 0:
        print(x + y, y, 0)

    elif x < 0 and y <= 0:
        print(0, -x,-y-x)

    elif x <= 0 and y >= 0:
        if abs(x) == y:
            print(0, y, 0)
        if abs(x) < y:
            print(abs(x + y), max(abs(x), y), 0)
        elif abs(x) > y:
            print(0, max(abs(x), y), abs(x + y))
        
    else:
        print(0, 0, 0)

