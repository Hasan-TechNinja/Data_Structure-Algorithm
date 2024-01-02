def Linear_search(L, x):
    n = len(L)
    i = 0

    while i < n:
        if L[i] == x:
            return i
        i = i + 1
    i = -1
    return i

def Linear_Search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i
    return -1

L = [1, 2, 3, 9, 8, 4, 3, 9]
x = int(input("Enter a integer: "))
Linear_search()