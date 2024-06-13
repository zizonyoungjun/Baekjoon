def apt():
    T = int(input())
    for _ in range(T):
        k = int(input())
        n = int(input())
        result = people(k, n)
        print(result)


def people(k, n):
    if k == 0:
        return n
    elif n == 1:
        return 1
    result = people(k, n-1) + people(k-1, n)
    return result


apt()
