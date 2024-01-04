def merge_sort(list1):
    if len(list1) > 1: 
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merge_sort(left_list)
        merge_sort(right_list)

        i, j, k = 0, 0, 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[1]
                i += 1
                k += 1
            else:
                list1[k] = right_list[j]
                j += 1
                k += 1