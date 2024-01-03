def Merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left = list[:mid]
        right = list[mid:]
        Merge_sort(left)
        Merge_sort(right)


ls = [int(input("Enter a list: "))]
Merge_sort(ls)