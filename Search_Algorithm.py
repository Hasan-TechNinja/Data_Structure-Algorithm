def Linear_search(L, x):
    L = [1,5,7,3,5,2,3,9,8,7,4,5,4,3]
    x = int(input('Enter a number: '))
    n = len(L)
    i = 0

    while i < n:
        if L[i] == x:
            return i
        i = i + 1
    i = -1
    return i

Linear_search()

def Linear_Search(L, x):
    n = len(L)

    for i in range(n):
        if L[i] == x:
            return i
    return -1

def Binary_search(L, x):
    n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    m = 4

    left, right = 0, len(L) - 1
    