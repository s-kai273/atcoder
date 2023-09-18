A, B = [int(x) for x in input().split()]

i = 0
while A != B:
    if A > B:
        A = A - B
    else:
        B = B - A
    i += 1

print(i)
