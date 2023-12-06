N, S, M, L = [int(x) for x in input().split()]

min_price = None

for s_c in range(101):
    for m_c in range(101):
        for l_c in range(101):
            price = S * s_c + M * m_c + L * l_c
            if 6 * s_c + 8 * m_c + 12 * l_c < N:
                continue
            min_price = price if min_price is None or min_price > price else min_price

print(min_price)
