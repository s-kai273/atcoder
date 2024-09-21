s_ab, s_ac, s_bc = input().split()
score = {
    "A": 0,
    "B": 0,
    "C": 0,
}

comparisons = [
    (s_ab, "A", "B"),
    (s_ac, "A", "C"),
    (s_bc, "B", "C"),
]

for symbol, lesser, greater in comparisons:
    if symbol == "<":
        score[greater] += 1
    else:
        score[lesser] += 1

for key in score.keys():
    if score[key] == 1:
        print(key)
        break