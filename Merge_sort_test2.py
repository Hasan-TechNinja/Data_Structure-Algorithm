def merge_sort(a, b):
    merged_list = []
    len_a, len_b = len(a), len(b)
    index_a, index_b = 0, 0
    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            merged_list.append(a[index_a])
            index_a += 1
        else:
            merged_list.append(b[index_b])
            index_b += 1
    return merged_list

x = [1,2,4,5,6,7]
y = [3,4,8,6,5,4,3]
result = merge_sort(x, y)
print(result)