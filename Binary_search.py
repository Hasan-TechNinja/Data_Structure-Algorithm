def binary(array, target):
    L = 0
    U = len(array) - 1

    while L < U:
        mid = (L + U) // 2
        if target == mid:
            print(mid)
        elif target < mid:
            U == mid - 1
        elif target >= mid:
            L == mid + 1

array = [3, 4, 7, 9, 10, 12, 14, 16, 18, 19, 20, 24, 27, 29, 30, 31, 37, 39, 40]
target = 18
print(binary(array, target))