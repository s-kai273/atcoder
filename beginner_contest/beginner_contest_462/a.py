s = input()
filtered_list = list()
for ch in s:
    if "0" <= ch <= "9":
        filtered_list.append(ch)
print("".join(filtered_list))
