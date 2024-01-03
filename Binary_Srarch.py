def Binary_search(arr, target):
    l = 0
    u = len(arr) - 1

    while l <= u:
        mid = (l + u) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            u = mid -1
    return -1

#Test part
my_list = [1,2,4,6,8,9,10,13,14,16,17,18,19,20]
find = 14

result = Binary_search(my_list, find)

if result != -1:
    print(f"Element {find} is present index no {result}")
else:
    print(f"Element {find} is not present")