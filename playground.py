def insertion(lst):
    for i in range(1, len(lst)):
        item = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > item:
            lst[j+1] = lst[j]
            j -= 1
        lst[j + 1] = item

    return lst


print(insertion([5,4,3,2,1]))

def selection(lst):
    for i in range(len(lst)):
        smallest = i
        for j in range(i+1, len(lst)):
            if lst[j] > lst[smallest]:
                smallest = j
            lst[j], lst[smallest] = lst[smallest], lst[j]
    return lst

print(selection([5,4,3,2,1]))


