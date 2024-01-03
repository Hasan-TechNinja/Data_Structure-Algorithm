#Main logic
def Linear_Search(list, target):
    l = 0
    length = len(list)
    while l < length:
        if list[l] == target:
            return l
        else: 
            l = l + 1

    return -1

#Test Case     
my_list = [1,2,6,3,8,5,0,2,5,7,4,3]
my_target = int(input("Find the element: "))
result = Linear_Search(my_list, my_target)

#print(result)
if result != -1:
    print(f"Element {my_target} is present index number: {result}")
else:
    print(f"Element {my_target} is not found")