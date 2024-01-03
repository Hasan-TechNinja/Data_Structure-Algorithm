def Binary_search(list, target):
    l = 0
    u = len(list) - 1
    while l < u:
        mid = (l + u) // 2
        if list[mid] == target:
            return mid
        elif list[mid] > target:
            u = mid - 1
        elif list[mid] < target:
            l = mid + 1

    return -1

# Test case
my_list = [1, 3, 4, 6, 8, 12, 14, 15, 16, 18, 19, 20, 23, 25, 27, 30]
test = int(input("Find the number: "))
result = Binary_search(my_list, test)

if result != -1:
    print(f"Element {test} is present index number: {result}")
else: 
    print(f"Element {test} is not present")