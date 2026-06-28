s = input()
e_count = 0
for ch in s:
    if ch == "E":
        e_count += 1
if e_count > len(s) - e_count:
    print("East")
else:
    print("West")
