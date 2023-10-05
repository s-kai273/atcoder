N, M = [int(x) for x in input().split()]
S = input()
T = input()

try:
    index = T.index(S)
    rindex = T.rindex(S)
    if index == 0:
        if rindex + N == M:
            print(0)
        else:
            print(1)
    else:
        if rindex + N == M:
            print(2)
        else:
            print(3)
except ValueError:
    print(3)
