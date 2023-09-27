WIDTH_STR = 'abcdefgh'

for i in range(8):
    S = input()
    try:
        index = S.index('*')
        print(WIDTH_STR[index] + str(8 - i))
    except ValueError:
        continue
