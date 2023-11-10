X, Y = [int(x) for x in input().split()]

if (Y - X <= 2 and Y - X > 0) or (Y - X >= -3 and Y - X < 0):
    print("Yes")
else:
    print("No")
