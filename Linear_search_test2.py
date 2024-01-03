#Linear search algorithm
def Linear_Search(list, target):
    l = 0
    while l < len(list):
        if list[l] == target:
            return l
        else:
            l += 1
    return -1

#Test case 
my_list = [5, 8, 9, 3, 4, 2, 1, 5, 6, 10]
search = int(input("Find number: "))
result = Linear_Search(my_list, search)
if result != -1:
    print(f"Element {search} is present index no: {result}")
else: 
    print(f"Element {search} is not present")