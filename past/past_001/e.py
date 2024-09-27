N, Q = map(int, input().split())

follow_matrix = [['N'] * N for _ in range(N)]

for _ in range(Q):
    S = list(map(int, input().split()))
    update_points = []

    if S[0] == 1:
        a = S[1] - 1
        b = S[2] - 1
        update_points.append((a, b))
    elif S[0] == 2:
        a = S[1] - 1
        for i in range(N):
            if i == a:
                continue
            if follow_matrix[i][a] == 'Y':
                update_points.append((a, i))
    elif S[0] == 3:
        a = S[1] - 1
        for i in range(N):
            if i == a:
                continue
            if follow_matrix[a][i] == 'Y':
                for j in range(N):
                    if j == a:
                        continue
                    if follow_matrix[i][j] == 'Y':
                        update_points.append((a, j))
    
    for point in update_points:
        follow_matrix[point[0]][point[1]] = 'Y'

for i in range(N):
    print(''.join(follow_matrix[i]))
