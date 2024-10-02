S = input()
key_dict = dict()

for i in range(26):
    key_dict[S[i]] = i

alphabet_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
answer = 0
for i in range(1, 26):
    answer += abs(key_dict[alphabet_list[i]] - key_dict[alphabet_list[i - 1]])

print(answer)