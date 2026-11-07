s = input()
t = input()
matched = False

for left in range(len(s)):
    if s[left] != t[0]:
        continue
    for i in range(len(t)):
        if left + i > len(s) - 1 or s[left + i] != t[i]:
            break
        if i == len(t) - 1:
            matched = True
    if matched:
        break

if matched:
    print("Yes")
else:
    print("No")
