#Binary Search Algorithm
def Binary_Search(list, target):
    l = 0
    u = len(list) - 1

    while l < u:
        mid  = (l + u) // 2     #index
        if list[mid] == target: 
            return mid          #value
        elif list[mid] < target:
            l = mid + 1
        else: 
            u = mid -1
    return -1
#Test code
my_list = [1,4,6,7,9,10,12,13,15,17,18,19,20]
test = int(input("Find the number: "))
result = Binary_Search(my_list, test)

if result != -1:
    print(f"Element {test} is present index number: {result}")
else:
    print(f"Element {test} is not present in the List")