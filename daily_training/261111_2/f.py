s = input()
zero_induces = list()
for i, ch in enumerate(s):
    if ch == "0":
        zero_induces.append(i)

count = len(s)

pi = None
for i in zero_induces:
    if pi is not None and i == pi + 1:
        count -= 1
        pi = None
    else:
        pi = i

print(count)
