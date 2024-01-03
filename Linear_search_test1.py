def Linear_Search(arr, target):
    l = 0
    while l < len(arr):
        if arr[l] == target:
            return l
        else:
            l += 1
    return -1

list = [8, 0, 6, 7, 1, 4, 6, 3, 2, 10]
find = int(input("Find the number: "))

result = Linear_Search(list, find)
if result != -1:
    print(f"Element {find} is present index number {result}")
else: 
    print(f"Element {find} is not present!")