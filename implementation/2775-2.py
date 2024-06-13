def apt():
    T = int(input())
    for _ in range(T):
        k = int(input())
        n = int(input())
        result = people(k, n)
        print(result)


def people(k, n):
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    # 0층에 사는 사람은 i호에 i명
    for i in range(1, n + 1):
        dp[0][i] = i

    # 나머지 층의 사람 수 계산
    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            dp[floor][room] = dp[floor][room - 1] + dp[floor - 1][room]

    return dp[k][n]


apt()
