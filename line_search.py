def lsearh(lst, item):
    found = False
    index = 0
    while not found and index<=len(lst)-1:
        if lst[index] == item:
            found = lst[index]
            return found
        else:
            index+=1
    return found

x = 43
_list = [7,6,4,3,2,42]
result = lsearh(_list,x)
print(result)


def binary_search(lst, item):
    first = 0
    last = len(lst)-1
    found = False
    while first <= last and not found:
        mid = (first + last)//2
        if lst[mid] == item:
            found = True
            return found
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    print(found)

some_list = [1,2,3,4,5,6,7,8,9,10]
item=10
binary_search(some_list, item)
