data_str = '''tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481
'''

S = input().strip()

for line in data_str.strip().split('\n'):
    username, rating = line.split()
    if username == S:
        print(rating)
        break
