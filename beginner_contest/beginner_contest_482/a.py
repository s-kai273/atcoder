s = input()
count = 0
for ch in s:
    if ch == "o":
        count += 1
answer = "even" if count % 2 == 0 else "odd"
print(answer)
