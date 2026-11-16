s = list(input())
t = list()

prev = None
sharp_exist = True
for ch in s:
    current = "o"
    if ch == "#":
        current = "#"
        sharp_exist = True
    elif prev == "o" or not sharp_exist:
        current = "."
    else:
        current = "o"
        sharp_exist = False
    prev = current
    t.append(current)

print("".join(t))
