n = int(input())
s = input()
t = input()

similar = "Yes"
for i in range(n):
    if (
        s[i] != t[i]
        and sorted([s[i], t[i]]) != ["1", "l"]
        and sorted([s[i], t[i]]) != ["0", "o"]
    ):
        similar = "No"
        break
print(similar)
