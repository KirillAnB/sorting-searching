def merge_sort(_list):
    if len(_list) <= 1:
        return _list
    else:
        mid = len(_list) // 2
        left, right = _list[0:mid], _list[mid:]
        merge_sort(left), merge_sort(right)
        a, b, c = 0, 0, 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                _list[c] = left[a]
                a += 1
            else:
                _list[c] = right[b]
                b += 1
            c += 1
        while a < len(left):
            _list[c] = left[a]
            a += 1
            c += 1
        while b < len(right):
            _list[c] = right[b]
            b += 1
            c += 1
        return _list

some_list = [2,22,2,3,4,5,6]
sorted_list = merge_sort(some_list)
print(sorted_list)